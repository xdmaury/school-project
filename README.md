# school-project

API utilzando Flask para geremencimento de cadastro de alunos e cursos.

| URL                      | Method | Description           |
|--------------------------|--------|-----------------------|
| /api/student             | GET    | List all students     |
| /api/student             | POST   | Create a new student  |
| /api/student/<id>        | GET    | Show a single student |
| /api/student/<id>        | POST   | Update a student      |
| /api/student/delete/'<id>' | GET    | Delete a student      |
| /api/course              | GET    | List all course       |
| /api/course              | POST   | Create a new course   |
| /api/course/<id>         | GET    | Show a single course  |
| /api/course/<id>         | POST   | Update a course       |
| /api/course/delete/<id>  | GET    | Delete a course       |


# Guia rápido

Crie um ambiente virtual Python, se ainda não tiver sido criado e ativa-lo.

`python3 -m venv env`

# Dependências de Instalação

`pip3 install -r requirements.txt`

# Inicie o aplicativo

Antes de iniciar a aplicação, execute os seguintes comandos para gerar o arquivo dump.db:
`pyhton3 run.py db init`
`pyhton3 run.py db migrate`
`pyhton3 run.py db upgrade`

Para executar a aplicação:
`python3 run.py runserver`
