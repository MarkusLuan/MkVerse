# Sobre o projeto

### Requisitos
- Python 3
- Com algum framework Web (Preferencia Django) *
- Autenticação com JWT
- Banco de Dados de preferencia PostgreSQL
- Sistema de cache
- Paginação
- Testes unitários
- Documentação com Swagger ou Postman **
- Docker com o Docker-compose

### Casos de uso
- Caso 1: Cadastro
    - Os usuários deverão ser capazes de se registrar usando email, nome e senha
    - A autenticação para login e gerenciamento de sessão deverá ser com JWT
- Caso 2: Postagens
    - Os usuários logados podem postar com texto e uma imagem
    - As postagens podem ser curtidas por outros usuários
- Caso 3: Seguidores
    - Os usuários logados podem Seguir ou Deixar de Seguir outros usuários
    - O Feed deve mostrar apenas postagens dos usuários que a pessoa segue
- Caso 3: Feed
    - O usuário pode visualizar uma lista de postagens dos usuários que segue de forma paginada
    - As postagens devem ser ordernadas pela data de criação, do mais recente ao mais antigo

### Bonus - Provavelmente não consiga concluir a tempo
- Limitador de banda nos endpoints para evitar abuso
- Prevenção de SQL Injection
- Tarefas async com Celery ou outra ferramenta
- Sistema de busca
- Continuos Integration (Github Actions para testes)

### Observações
<p>* Particulamente só tinha visto o Django por cima, normalmente uso o Flask, mas vou arriscar fazer esse projeto em Django por conta dos testes unitários ser melhor de se fazer. Caso, eu não consiga após 2 dias irei para o Flask que estou mais acostumado.</p>

<p>** Mesmo sendo familiarizado com as duas ferramentas, fiz a documentação no Postman já que era a ferramenta que estava usando para testes</p>