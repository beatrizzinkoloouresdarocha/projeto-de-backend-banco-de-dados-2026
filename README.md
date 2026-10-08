Sistema de Gestão de Clientes e Contratos

Projeto de backend desenvolvido para praticar banco de dados, SQL, Python e automação.

Objetivo

O sistema foi criado para facilitar o gerenciamento de clientes que contrataram serviços de desenvolvimento de sites e outros serviços digitais.

O banco permite controlar:

Clientes
Empresas
Serviços contratados
Contratos
Pagamentos
Pagamentos pendentes
Pagamentos atrasados
Contratos ativos
Relatórios
Tecnologias
Python
SQLite
SQL
DBeaver
Git
GitHub
Windows Task Scheduler
Estrutura
sistema-clientes/
│
├── banco/
│   └── sistema_clientes.db
│
├── app.py
├── banco.py
├── atualizacao.py
├── relatorio.py
├── executar_sistema.bat
├── .gitignore
└── README.md
Banco de dados

O projeto possui as seguintes tabelas:

clientes
empresas
servicos
contratos
pagamentos
Funcionalidades

O sistema permite:

Cadastrar clientes.
Associar clientes a empresas.
Cadastrar serviços.
Registrar contratos.
Registrar pagamentos.
Identificar pagamentos pendentes.
Identificar pagamentos atrasados.
Consultar contratos ativos.
Calcular valores recebidos.
Calcular valores a receber.
Gerar relatórios.
Atualizar automaticamente pagamentos atrasados.
Automação

O Python verifica os pagamentos e identifica automaticamente pagamentos que passaram da data de vencimento e ainda não foram pagos.

A execução pode ser automatizada pelo Agendador de Tarefas do Windows.

Banco de dados

O banco utilizado neste projeto é SQLite e pode ser visualizado e administrado através do DBeaver.

Os dados utilizados inicialmente são fictícios para fins de estudo.

Objetivo de aprendizado

Este projeto faz parte dos estudos de backend e banco de dados, com foco em:

SQL
Relacionamentos entre tabelas
Chaves primárias
Chaves estrangeiras
JOIN
SELECT
INSERT
UPDATE
VIEW
Python
Automação
Git e GitHub