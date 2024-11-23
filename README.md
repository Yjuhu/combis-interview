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

Mocky Mocks:
m1: https://run.mocky.io/v3/8241be7d-638b-4700-819e-f49a97395ff0
m2: https://run.mocky.io/v3/11e0b870-b3fc-490b-9de1-5701c2da90cf
m3: https://run.mocky.io/v3/0c2665f1-0bf4-4b3e-89a8-43eaa70ca3bb
m4: 


