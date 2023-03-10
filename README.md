# Cinema API

API service for cinema management written on DRF

## Endpoints in Swagger
![1 screenshots](https://raw.githubusercontent.com/Glasis9/cinema-api-on-drf-2/main/1%20screenshots.jpg)
![2 screenshots](https://raw.githubusercontent.com/Glasis9/cinema-api-on-drf-2/main/2%20screenshots.jpg)
![3 screenshots](https://raw.githubusercontent.com/Glasis9/cinema-api-on-drf-2/main/3%20screenshots.jpg)

## Installing using GitHub
Install PostgresSQL and create db
```shell
git clone https://github.com/Glasis9/cinema-api-on-drf.git
cd cinema_API
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```

# Run with docker
Docker should be installed
```shell
docker-compose build
docker-compose up
```

# Getting access
* create user via /api/user/register/
* get access token via /api/user/token/

You can also get the token of the created user:
* email: admin.user@admin.com
* password: admin12345

## Features

* JWT authenticated
* Admin panel /admin/
* Documentation is located at /api/doc/swagger/
* Managing orders and tickets
* Creating movies with genres, actors
* Creating cinema halls
* Adding movies and movie sessions
