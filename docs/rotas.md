# Rotas da API
Exportei o postman.json, e pedi ao chatGPT um código para converter o postman.json em Markdown

## Variaveis
* url = http://localhost/api
* TOKEN => Token obtido pelo /auth/token
* REFRESH_TOKEN => Refresh_token obtido junto com o token

Caso queira poderá usar a url que disponibilizei no servidor também:
* url = https://teste.mkverse.mkgcriacoes.com.br/api (observar que não subi como HTTPS)

---

## Gerar Token
**Método:** `POST`
**Endpoint:** `{{url}}/auth/token`
**Headers:**
- `Authorization`: `Basic YWxhZGRpbjpvcGVuc2VzYW1l`

---
## Renovar Token
**Método:** `POST`
**Endpoint:** `{{url}}/auth/refresh`
**Headers:**
- `Authorization`: `Bearer {{REFRESH_TOKEN}}`

---
## Pesquisar Usuários
**Método:** `GET`
**Endpoint:** `{{url}}/users?user=<username:string>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Informações do Usuário
**Método:** `GET`
**Endpoint:** `{{url}}/users/<user_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Salvar Usuário
**Método:** `POST`
**Endpoint:** `{{url}}/users`
**Headers:**
- `Authorization`: `Basic YWxhZGRpbjpvcGVuc2VzYW1l`

---
## Carregar Feed
**Método:** `GET`
**Endpoint:** `{{url}}/feed`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Carregar Imagem da Postagem
**Método:** `GET`
**Endpoint:** `{{url}}/feed/<feed_uuid:uuid>/img`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Criar Postagem
**Método:** `POST`
**Endpoint:** `{{url}}/feed`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Criar Postagem com Imagem
**Método:** `POST`
**Endpoint:** `{{url}}/feed`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Deletar Postagem
**Método:** `DELETE`
**Endpoint:** `{{url}}/feed/<user_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Listar curtidas
**Método:** `GET`
**Endpoint:** `{{url}}/likes/<feed_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Dar Like
**Método:** `POST`
**Endpoint:** `{{url}}/likes/<feed_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Remover Like
**Método:** `DELETE`
**Endpoint:** `{{url}}/likes/<feed_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Listar Seguidores do Usuário Logado
**Método:** `GET`
**Endpoint:** `{{url}}/followers`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Seguir Usuário
**Método:** `POST`
**Endpoint:** `{{url}}/followers/<user_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
## Deixar de Seguir
**Método:** `DELETE`
**Endpoint:** `{{url}}/followers/<user_uuid:uuid>`
**Headers:**
- `Authorization`: `Bearer {{TOKEN}}`

---
