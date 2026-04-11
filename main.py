from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base, Payment

Base.metadata.create_all(bind=engine)

app = FastAPI()

products = []
orders = []


@app.get("/")
def home():
    return {"message": "API de pagamentos funcionando!"}


@app.post("/products")
def create_product(product: dict):
    product["id"] = len(products) + 1
    products.append(product)
    return product


@app.post("/orders")
def create_order(order: dict):
    order["id"] = len(orders) + 1
    orders.append(order)
    return order


@app.get("/orders")
def get_orders():
    return orders


@app.post("/payments")
def create_payment(payment: dict):
    db = SessionLocal()

    new_payment = Payment(
        order_id=payment["order_id"],
        method=payment["method"],
        status="pending"
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return {
        "id": new_payment.id,
        "order_id": new_payment.order_id,
        "method": new_payment.method,
        "status": new_payment.status
    }


@app.get("/payments")
def get_payments():
    db = SessionLocal()
    payments = db.query(Payment).all()

    return [
        {
            "id": payment.id,
            "order_id": payment.order_id,
            "method": payment.method,
            "status": payment.status
        }
        for payment in payments
    ]


@app.patch("/payments/{payment_id}/pay")
def pay_payment(payment_id: int):
    db = SessionLocal()
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if not payment:
        return {"error": "Pagamento não encontrado"}

    if payment.status == "paid":
        return {"error": "Pagamento já foi pago"}

    if payment.status == "canceled":
        return {"error": "Pagamento cancelado"}

    payment.status = "paid"
    db.commit()
    db.refresh(payment)

    return {
        "id": payment.id,
        "order_id": payment.order_id,
        "method": payment.method,
        "status": payment.status
    }


@app.patch("/payments/{payment_id}/cancel")
def cancel_payment(payment_id: int):
    db = SessionLocal()
    payment = db.query(Payment).filter(Payment.id == payment_id).first()

    if not payment:
        return {"error": "Pagamento não encontrado"}

    if payment.status == "paid":
        return {"error": "Pagamento já foi pago e não pode ser cancelado"}

    if payment.status == "canceled":
        return {"error": "Pagamento já está cancelado"}

    payment.status = "canceled"
    db.commit()
    db.refresh(payment)

    return {
        "id": payment.id,
        "order_id": payment.order_id,
        "method": payment.method,
        "status": payment.status
    }