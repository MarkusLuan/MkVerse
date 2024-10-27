# Projeto para uma Vaga de Programador Python - B2Bit

O projeto possui 3 Branchs:
- A master - Que possui a documentação e a inicialização do projeto
- Django - A primeira versão do projeto que iniciei em Django, porém tive alguns problemas
- Flask - A versão mais recente e mais finalizada do projeto

Ao final do projeto irei fazer o merge com a Master

---

### Descrição
O projeto se trata de uma API RESTFUL para um sistema de midia social, onde os usuários poderão:
- [x] Registrar e Autenticar
- [x] Criar, Editar e Deletar Postagem
- [x] Curtir Postagens
- [x] Postar imagem
- [x] Seguir e Deixar de Seguir Outros Usuários
- [x] Visualizar o Feed
- [x] Mostrar apenas postagens dos usuários seguidos

As Views e Models foram separados em vários arquivos nas suas respectivas pastas para garantir um código mais limpo.

Infelizmente, por motivos da correria de trabalho e tempo tive que migrar o projeto para o flask, pois no Django estava dando alguns problemas que não estava conseguindo resolver e como sou mais familiarizado com o flask, para não perder a oportunidade a solução foi essa.

---

### Banco de Dados
O banco de dados está em Postgresql 16, porém a estrutura foi desenhada usando o MySQL Workbench
![Estrutura do Banco de Dados](./docs/estrutura_db.png)

### Fake-migrate - Apaga o banco e sobe uma cópia
* Queria usar o flask-migrate, mas deu um bug e estou sem tempo para resolver

Para iniciar o banco basta ir na pasta [src](./src/) e executar o comando
```shell
python3 migrate.py ["config.development"]
```
O ultimo parametro é opcional e são aceitos:
- "config.development"
- "config.production"

---

### Documentações
- [Sobre o Projeto](./docs/README.md)
- [Documentação em Postman](./docs/postman.json)
- [Rotas - Extraido do Postman](./docs/rotas.md)
- [Estrutura do Projeto](./docs/estrutura_projeto.md)

---

### Execução
#### Docker
1. Acessar a pasta raiz do projeto (Onde está localizado o [dockerfile](./dockerfile) e o [docker-compose.yml](./docker-compose.yml))
2. Abrir o terminal e Digitar o comando
```shell
docker-compose up
```
3. Feito isso o sistema já estará funcionando nas portas 80 para o servidor da aplicação e 5432 para o DB PostgresSQL.
4. Caso deseje mudar a porta, basta editar o arquivo [docker-compose.yml](./docker-compose.yml) alterando a porta da esquerda no atributo ports, exemplo se quiser mudar a porta do servidor para a porta 50...
```yml
mkverse_server:
    build: "."
    depends_on: 
        - mkverse_db
    container_name: mkverse_server
    ports:
        - "50:80"
    networks: 
        - mkverse_network
```

#### Python
Para executar diretamente no python é necessário ter um banco de dados Postgres ou MySQL rodando na maquina

1. Acessar a pasta raiz do projeto (onde está localizado o [requirements.txt](./requirements.txt))
2. Abrir o terminal e digitar (a parte do ambiente é opcional)
##### Windows
```shell
python -m venv .env
.env\scripts\activate
python -m pip install -U pip
pip install -r requirements.txt
```
##### Linux ou Mac
```shell
python -m venv .env
source .env/scripts/activate
python -m pip install -U pip
pip install -r requirements.txt
```
3. Acessar a pasta [src](./src/) (onde fica o codigo fonte do projeto) e executar o seguinte comando no terminal
```shell
python app.py
```
4. Caso deseje alterar alguma configuração do banco (como porta, senha, ou host) ou a chave da API basta acessar a pasta [config](./src/config/) e alterar o arquivo [base.py](./src/config/base.py) ou [development.py](./src/config/development.py)

### Observação
- No meio do projeto fui atacado por RANSON, graças a Deus o projeto estava no outro HD e tinha commitado algumas coisas. Pena que vou perder um tempo reconfigurando algumas coisas no outro PC.
