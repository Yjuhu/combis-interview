# combis-interview
Django application that retrieves data from a REST API (either simulated or real) of Cisco DNA Center, processes it, and stores it in a PostgreSQL database.

$ pip3 install django


Starting django server(ubuntu): python3 manage.py runserver

All info about starting and setting up postgresql database and server:
    placeholder(run on startup)

Entering shell sql: $ sudo -u postgres psql   # postgres is admin name

Database name: combisdb
Database user: combis_user(all permissions granted)
Database user password: combis


http://127.0.0.1:8000/admin/
Database superuser: supercombis
Database superuser e-mail: jakov.sarolic.1@gmail.com
Database superuser password: combis

Migrations(maybe future automatization):
$ python3 manage.py makemigrations (linux)
$ python3 manage.py migrate

Django rest framework:
$ sudo pip3 isntall djangorestframework


