# Library Management System
Library management system (Final Year Project) for the course of B.Tech in Computer Science and Engineering at BP Poddar Institute of Management and Technology, Kolkata.

## Group Members

### Backend team
1. [Arkaprabha Chakraborty](https://www.github.com/ArkaprabhaChakraborty)
2. [Aniruddha Basak](https://www.github.com/aniruddha2000)
### Frontend team
1. [Debarghya Pal](https://www.github.com/DebarghyaPal)


# How to setup?

## Create .env file
For dev mode firstly we need an .env file in the core module directory of our project. The .env file should contain the following variables:

```
SECRET_KEY=e*lmb5ecg25e2ypq2%vcopg=6@30_+s#kj_#r17%zf!gcc42dm
```

## Install dependencies and setup project
After the creation of the .env file, run the following commands to setup the project in dev mode:

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

## Create Superuser

By default there is no superuser. To create a superuser, run the following command:

```bash
python3 manage.py createsuperuser
```

Fillup the details and you are good to go.

## Alternatives (Using dokcer and docker-compose)
Using docker and docker-compose is recommended for this project. To setup the project using docker and docker-compose, modify your .env file in this [step](#create-env-file) to include the following variables:

```
DJANGO_DEFAULT_SUPERUSER=True 
DJANGO_DEFAULT_SUPERUSER_USERNAME='admin'
DJANGO_DEFAULT_SUPERUSER_PASSWORD='password'
DJANGO_DEFAULT_SUPERUSER_EMAIL='admin@123'
```

This creates a default superuser with the username `admin` and password `password` when the docker container is created. You can change it to whatever you want and access the admin panel at `http://localhost:8000/admin/`.

Now run the following commands to setup and run the project:

```bash
sudo docker-compose up
``` 
