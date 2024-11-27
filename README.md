# ComApp
ComApp is a Django application for managing and displaying devices. It includes functionality to fetch device data through a simulated API endpoint, store it in a database, and filter devices by status (active/inactive). This app uses PostgreSQL as its database.

## Features
- Fetch device data.
- Store device data in the database.
- Retrieve all devices or filter by status.
- Manage devices via the Django Admin interface.
- Assisted setup via provided shell scripts.

## Requirements
- Python 3.8+(how to install it...https://www.python.org/downloads/)
- pip (Python package manager)
- PostgreSQL 12+(how to install it...https://www.postgresql.org/download/)
- PostgreSQL server up and running(- You will need server login credentials(Windows).
- psql command added to the PATH(Windows)

## Setup Instructions
### 1. Clone the Repository
Clone the project from GitHub:
- $ git clone https://github.com/Yjuhu/combis-interview
- $ cd combis-interview

### 2. Start setup script that will create virtual environment and install all dependencies(located in Django project directory).
#### Linux/Mac
Run the setup.sh script:
- $ chmod +x setup.sh
- $ ./setup.sh

#### Windows
Run the setup.bat script:
- $ setup.bat

### 3. Access the aplication.
Start the Django development server:
- $ python manage.py runserver

Open the app in your browser
- http://127.0.0.1:8000/
Open the admin panel in your browser
- http://127.0.0.1:8000/admin/

### 4. Using the App
- Fetch Devices: Use the "Fetch Devices" button on the homepage to fetch and display data.

- Fetch and Store Devices: Use the "Fetch and Store Devices" button to save the data into the database.

- Get All Devices: Retrieve all stored devices.

- Filter Devices: Use "Get Active Devices" or "Get Inactive Devices" to filter the data by status.

- Admin Panel: Visit /admin to manually manage devices. Log in using the superuser credentials created during setup.

- Changing mock device data for testing purposes in view.py file of comapp directory. Change the data by finding mock_devices method and change values to your needs. 

## Default Credentials for Admin Panel
- Username: admin
- Email: admin@combis.com
- Password: Set during script execution.

#### Forgotten password?
Change it with:
- $ python manage.py changepassword admin

Database credentials:
- Username: comapp_user
- Password: securepassword

#### This project is licensed under the MIT License.

