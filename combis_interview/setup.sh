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

# Step 4: Run migrations and collect static files
echo "Running migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Step 5: Create Django superuser
echo "Creating Django superuser..."
python3 manage.py createsuperuser --email admin@combis.com --username admin

# Step 6: Run the development server
echo "Setup complete! Starting the server..."
python3 manage.py runserver