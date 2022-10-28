# Library Management System
Library management system (Final Year Project) for the course of B.Tech in Computer Science and Engineering at BP Poddar Institute of Management and Technology, Kolkata.

## Group Members

### Backend team
1. [Arkaprabha Chakraborty](https://www.github.com/ArkaprabhaChakraborty)
2. [Aniruddha Basak](https://www.github.com/aniruddha2000)
### Frontend team



# How to setup?

Run the following commands to setup the project in dev mode:

```bash
pip install -r requirements.txt
```

Now run the following commands to setup the database:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

If you are on windows, run the following commands instead:

```bash
python manage.py makemigrations
python manage.py migrate
```

Now run the following command to start the server:

```bash
python3 manage.py runserver
```
