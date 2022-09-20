# MeuGénioLivraria
Loja Online - Ecommerce, inicialmente para a venda dos produtos da empresa Cortex Tecnologias, nomeadamente livros online e impressos...
Este projecto tem como objectivo criar o fornecimento de livros online para a leitura na aplicação MeuGénio Bibiotecário, considerando a protecção dos direitos autorais como essência para a gestão sustentável do serviço. 

# Development Enviroment

## Installation

Requirements:

- python 3.10
- PostgresSQL 13

Installing:

1. Run on Shell / Power Shell / or on your default CLI
   ````
    mkdir <project_dir>
    cd <project_dir>
    https://github.com/Cortextecnologias/MeuGenioLivraria.git 
    python -m venv .venv
    source .venv/bin/activate  # for linux
    .venv\bin\activate         # for windows
    cd src
    pip install -r requirements.txt
   ````
2. Make a **.env** file from **.env.tpl** and set basic variables. Remove or comment other variables.

3. Apply migrations
    ```
    python manage.py migrate
    ```
4. Runserver
    ```
    python manage.py runserver
    ```
5. Testing
    ```
    python manage.py test
    ```