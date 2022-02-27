## DJANGO-REST-FRAMEWORK simple user crud operations 

## Features
- Create a user
- Get all users
- Get user by id
- Delete user by id
- Update user by id


## Tech
- [Docker] - Using Dockerfile and docker compose
- [Djanog-rest-framework] - Rest API based framework for DJANGO
- [POSTGRES] - Relational Database

## Requirements
- Python 3.8
- postgresql 
- Docker 
- Docker compose

## Installation Standalone
```sh
python3 -m venv 3.8
source 3.8/bin/activate
git clone https://github.com/khushal123/django-rest-example.git
cd django-rest-example/
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 
```
## To run tests
```sh
python manage.py test
```

## Installation Docker
docker-compose contains both python and postgres images, so no need to install postgres if we are using these steps.
```sh
git clone https://github.com/khushal123/django-rest-example.git
cd django-rest-example/
docker build .
docker-compose up 
```

## Accessing the application
The application is available at [url](http://localhost:8000/api/users/)
Please check the postman [collection](https://www.getpostman.com/collections/f208255e2858480b569c)
To access via postman, create an env varialble in postman called <django> and add value -> [value](https://drf-assignment.herokuapp.com)

for testing on local, use [value](http://localhost:8000)
