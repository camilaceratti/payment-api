esse é um projeto simples de api de pagamentos que fiz para estudo e prática.

a ideia foi treinar criação de api com python e entender melhor o fluxo de pagamentos (criar, listar e cancelar)

o que eu fiz:
- criação de endpoints básicos
- estrutura simples de api
- integração com banco sqlite
- organização inicial do projeto

dificuldades:
- apanhei um pouco na estrutura do projeto e no uso do ambiente virtual (venv)

o que faltou / melhorias:
- melhor organização das pastas
- adicionar autenticação
- melhorar tratamento de erros
- criar testes

como rodar:
```bash
venv\scripts\activate
uvicorn main:app --reload

___________

this is a simple payment api project that I built for study and practice, the idea was to practice building an api with python and better understand the payment flow (create, list and cancel).

what I did:
- created basic endpoints
- built a simple api structure
- integrated with sqlite database
- organized the project in a basic way

difficulties:
- I struggled a bit with project structure and virtual environment (venv)

what is missing / improvements:
- better folder organization
- add authentication
- improve error handling
- create tests

how to run:

```bash
venv\scripts\activate
uvicorn main:app --reload
