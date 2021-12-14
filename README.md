# Teste Python - WishList

**Objetivo:**
API de avaliações para medir a experiência dos clientes.

**Requisitos:**

- Criar uma API para gerir uma WishList (Lista de Desejos);
- O usuário deve poder incluir um produto em sua lista de desejos;
- Título do Produto (obrigatório);
- Descrição (opcional);
- Link de onde encontrar (opcional);
- Foto (opcional);
- O usuário deve poder informar se já ganhou/comprou um item;
- Deve existir um endpoint para trazer um item da lista de forma randômica;
- Ter uma base de dados que armazene as informações.

**Dicas:**

- Não economize conhecimento, mas não precisa criar uma solução mirabolante.
- Para sua base de dados, temos essas sugestões:
  - https://www.elephantsql.com/ (PostgreSQL)
  - https://www.mongodb.com/pricing (MongoDB)
  - https://www.heroku.com/
  - Usar o docker-compose para subir um banco de dados junto com a aplicação

**Instruções:**

- Crie um repositório no Gitlab.com
- Instruções para execução da aplicação

**Seria legal se:**

- A documentação da solução esteja no repositório;
- Tenha um meio de testar os endpoints;
- Usamos o https://falconframework.org/;
- Utilizar docker e docker-compose para subir a aplicação.

**Diferencial:**

- Usar testes unitários
- A API tiver documentação OpenAPI 3.0
- Suportar múltiplos usuários
- Tiver um front-end simples

**O que será avaliado:**

- Prazo
- Requisitos realizados
- Legibilidade do código
- Boas práticas de desenvolvimento
- Performance

## Como executar a aplicação:

```bash

# Docker
$ docker-compose up --build -d

```

## API:

```bash
###
GET http://localhost:5000/getall HTTP/1.1
content-type: application/json

###
GET http://localhost:5000/get/38 HTTP/1.1
content-type: application/json

###
POST http://localhost:5000/add HTTP/1.1
content-type: application/json

{
    "title": "Televisão 444",
    "description": "Smart TV LG 43 4K UHD 43UP7500, com WiFi",
    "link": "https://rabelodigital.com/",
    "photo": "https://rabelodigital.com/foto.png"

}

###
PUT http://localhost:5000/update/56 HTTP/1.1
content-type: application/json

{
    "title": "Televisão 38",
    "description": "Smart TV LG 43 4K UHD 43UP7500, com WiFi",
    "link": "https://rabelodigital.com/",
    "photo": "https://rabelodigital.com/foto.png"

}

###
DELETE  http://localhost:5000/delete/56 HTTP/1.1
content-type: application/json

```
