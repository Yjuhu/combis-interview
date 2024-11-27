#!/bin/bash

# Step 1: Create and activate a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Step 3: Configure PostgreSQL database
echo "Setting up PostgreSQL database..."
DB_NAME="comapp_db"
DB_USER="comapp_user"
DB_PASSWORD="securepassword"

# Step 3.1: Create the database and user with permissions
echo "Creating database and user..."
sudo -u postgres psql -c "CREATE DATABASE $DB_NAME;"
sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

# Update database settings in settings.py
echo "Configuring database in settings.py..."
sed -i "s/'NAME': '.*'/'NAME': '$DB_NAME'/g" combis_interview/settings.py
sed -i "s/'USER': '.*'/'USER': '$DB_USER'/g" combis_interview/settings.py
sed -i "s/'PASSWORD': '.*'/'PASSWORD': '$DB_PASSWORD'/g" combis_interview/settings.py
sed -i "s/'HOST': '.*'/'HOST': 'localhost'/g" combis_interview/settings.py
sed -i "s/'PORT': '.*'/'PORT': '5432'/g" combis_interview/settings.py

# Step 4: Run migrations and collect static files
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 5: Create Django superuser
echo "Creating Django superuser..."
python manage.py createsuperuser --email admin@combis.com --username admin

# Step 6: Run the development server
echo "Setup complete! Starting the server..."
python manage.py runserver