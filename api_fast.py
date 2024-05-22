# Escreva uma aplicação usando FastAPI que simule um serviço simples para gerenciar
# informações de clientes. Crie rotas para:
# - Adicionar um novo cliente (POST).
# - Obter detalhes de um cliente específico pelo ID (GET).
# As informações do cliente devem incluir 'ID', 'Nome', 'Email' e 'Telefone'.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

clientes = []

class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    
@app.post("/clientes/")
async def add_cliente(cliente:Cliente):
      clientes.append(cliente)
      return "Cliente adicionado!"
  
@app.get("/cliente/{cliente_id}")
async def get_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    return {"message": "Cliente não encontrado!"}
