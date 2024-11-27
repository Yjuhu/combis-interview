@echo off

REM Step 1: Create and activate a virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Step 2: Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Step 3: Configure PostgreSQL database
echo Setting up PostgreSQL database...
set DB_NAME=comapp_db
set DB_USER=comapp_user
set DB_PASSWORD=securepassword

REM Step 3.1: Create the database and user with permissions
echo Creating database and user...
psql -U postgres -c "CREATE DATABASE %DB_NAME%;"
psql -U postgres -c "CREATE USER %DB_USER% WITH PASSWORD '%DB_PASSWORD%';"
psql -U postgres -c "ALTER USER %DB_USER% WITH SUPERUSER;"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE %DB_NAME% TO %DB_USER%;"

REM Step 4: Run migrations and collect static files
echo Running migrations...
python manage.py makemigrations comapp
python manage.py migrate

echo Collecting static files...
python manage.py collectstatic --noinput

REM Step 5: Create Django superuser
echo Creating Django superuser...
python manage.py createsuperuser --email admin@combis.com --username admin

REM Step 6: Run the development server
echo Setup complete! Starting the server...
python manage.py runserver
pause