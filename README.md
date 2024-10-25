# Projeto para uma Vaga de Programador Python

O projeto se trata de uma API RESTFUL para um sistema de midia social, onde os usuários poderão:
- [x] Registrar e Autenticar
- [ ] Criar, Editar, Deletar e Curtir Postagens
- [ ] Seguir e Deixar de Seguir Outros Usuários
- [ ] Visualizar o Feed

As Views e Models foram separados em vários arquivos nas suas respectivas pastas para garantir um código mais limpo
[Sobre o Projeto](./docs/README.md)

Infelizmente, por motivos da correria de trabalho e tempo tive que migrar o projeto para o flask, pois no Django estava dando alguns problemas que não estava conseguindo resolver e como sou mais familiarizado com o flask, para não perder a oportunidade a solução foi essa.

### Banco de Dados
O banco de dados está em Postgresql 16, porém a estrutura foi desenhada usando o MySQL Workbench
![Estrutura do Banco de Dados](./docs/estrutura_db.png)