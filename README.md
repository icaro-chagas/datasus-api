# Sistema de Disponibilização de Dados do DATASUS

Este projeto consiste em um sistema para extração, armazenamento e disponibilização de dados do DATASUS por meio de uma API RESTful desenvolvida com Django REST Framework. A API permite aos usuários acessar e analisar dados de saúde pública do Brasil de forma simplificada.

O o sistema só pode ser executado localmente em ambientes Linux devido ao uso da biblioteca `pysus`. Adcionalmete, para a realizar a execução local deve-se ter o PostgreSQL instalado na sua máquina. 

Para execução do sistema utlizando Docker, esse repositório disponibiliza um arquivo `docker-compose.yml` e um arquivo `Dockerfile`.

## Execução Sem Docker

### Instalação e Configuração

Para executar o sistema localmente, siga as instruções abaixo:

1. Clone este repositório:
`git clone <url_do_repositorio>`
<br/>

2. Navegue para o diretório raiz do projeto: 
`cd datasus_api`
<br/>

3. Gere um arquivo `.env` no diretório raiz (existe um arquivo `.env.example` no diretório raiz exemplificando as constantes que devem ser definidas).
<br/> 

4. Gere um ambiente python:
`python3 -m venv .venv`
<br/>

5. Ative o ambiente python:
`source .venv/bin/activate`
<br/>

6. Instale as dependências:
`pip install -r requirements.txt`

### Uso

1. Execute as migrações do banco de dados:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
<br/>

2. Inicie o servidor:
`python3 manage.py runserver`
<br/>

3. Acesse a API em:
`http://localhost:8000`

## Execução com Docker

Assegure-se que você tem o Docker instalado na sua máquina. Se não for o caso, você pode baixar e instalar o Docker seguindo as instruções do [website oficial](https://docs.docker.com/engine/install/).

### Instalação e Configuração

Para executar o sistema com Docker, siga as instruções a seguir:

1. Clone este repositório:
`git clone <url_do_repositorio>`
<br/>

2. Navegue para o diretório raiz do projeto: 
`cd datasus_api`
<br/>

3. Descomente os paths utilizados para execução do docker nos arquivos `./datasus_api/util/datasus_util.py` e `./datasus_api/util/postgresql_util.py`.

4. Gere um arquivo `.env` no diretório raiz (existe um arquivo `.env.example` no diretório raiz exemplificando as constantes que devem ser definidas).

### Uso

1. Execute o seguinte comando para construir as imagens e iniciar os contêineres:
`sudo docker-compose up --build`
<br/>

2. Após a conclusão do processo de construção, você poderá acessar o sistema em seu navegador: `http://localhost:8000`

#### Parando a Execução
Para parar a execução do sistema, pressione `Ctrl + C` no terminal onde o `docker-compose up` está sendo executado.

#### Limpeza

Para remover os contêineres e criados durante a execução do sistema, execute o seguinte comando:
`sudo docker-compose down`

Caso queira remover também os volumes criados executo o mesmo comando anterior com a flag `-v`:
`sudo docker-compose down -v`

