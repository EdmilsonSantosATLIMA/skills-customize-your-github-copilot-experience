# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Aprender a criar uma API RESTful usando o framework FastAPI, incluindo rotas CRUD, validação com Pydantic e execução local com Uvicorn.

## 📝 Tasks

### 🛠️ Criar endpoints básicos (GET / POST)

#### Description
Implemente rotas para listar e criar recursos simples (ex.: `items`).

#### Requirements
Completed program should:

- Expor rota `GET /items` para listar itens
- Expor rota `POST /items` para criar um novo item


### 🛠️ Adicionar endpoints de detalhe e atualização (GET / PUT / DELETE)

#### Description
Implemente rotas para recuperar, atualizar e remover um item por ID.

#### Requirements
Completed program should:

- Expor `GET /items/{id}`, `PUT /items/{id}`, `DELETE /items/{id}`
- Retornar códigos de status adequados (404 para não encontrado, 400 para requisições inválidas)


### 🛠️ Validar dados com Pydantic

#### Description
Defina modelos Pydantic para validar entrada e saída (por exemplo, `Item` com `id`, `name`, `description`).

#### Requirements
Completed program should:

- Usar classes `BaseModel` do Pydantic para validar payloads
- Garantir que respostas sigam o modelo declarado


### 🛠️ Rodar e testar localmente

#### Description
Execute a aplicação com Uvicorn e teste as rotas usando `curl`, `httpie` ou o Swagger UI automático.

#### Requirements
Completed program should:

- Instruções para instalar dependências (`fastapi`, `uvicorn`)
- Comando para iniciar o servidor: `uvicorn starter-code:app --reload --port 8000`
- Mostrar onde encontrar a documentação interativa (`http://localhost:8000/docs`)

---

**Dificuldade:** Intermediário

**Anexos:** `starter-code.py` (arquivo inicial fornecido)

**Due Date:** 2025-11-28
