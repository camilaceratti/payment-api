from sqlalchemy import Column, Integer, String
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    method = Column(String)
    status = Column(String)