# Aplicação FastAPI

## Descrição

Esta é uma aplicação FastAPI simples para gerenciar clientes. A aplicação permite adicionar um cliente e recuperar detalhes de um cliente pelo ID.

## Pré-requisitos

Você precisa ter o seguinte software instalado:

- Python 3.6 ou superior
- FastAPI
- Pydantic
- uvicorn

Você pode instalar as dependências com o seguinte comando:

```bash
pip install fastapi pydantic uvicorn
```

## Execução

Para executar a aplicação, use o seguinte comando:

```bash
uvicorn api_fast:app --reload
```

## Testes

Os testes podem ser executados usando o seguinte comando no diretório com os aruivos da aplicação:

```bash
pytest
```
