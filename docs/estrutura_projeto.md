# Estrutura do Projeto

```bash
Root/
├── .env/
├── db/
├── docs/
├── src/
│   ├── config/
│   ├── models/
│   ├── resources/
│   ├── tests/
│   ├── app_singleton.py
│   ├── app.py
│   ├── error_handler.py
│   ├── utils.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── estrutura.mwb
└── requirements.txt
```

### Onde
- .env/  => Ambiente do python
- db/  => Volume do docker para o banco
- docs/  => Documentação do projeto
- src/  => Pasta de código fonte do projeto
    - config/ => Configurações de ambiente do flask
    - models/ => DataModels do banco de dados
    - resources/ => Registros das rotas
    - tests/ => Pasta destinada a testes
    - app_singleton.py => Variaveis globais à execução da aplicação
    - app.py => Arquivo principal
    - error_handler.py => Tratamento de erros do flask
    - utils.py => Funções genericas e helpers
    - wsgi.py => Gateway para servidor de produção
- Docker-compose.yml => Configuração do Docker-compose
- Dockerfile => Arquivo para criação e preparação do ambiente Docker
- Estrutura.mwb => Modelo do Banco - Feito no MySQL Workbench
- Requirements.txt => Dependencias do python para o projeto


    