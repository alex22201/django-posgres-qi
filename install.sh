#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    source .env
fi

base_python_interpreter=""
project_domain=""
project_path=$(pwd)

read -p "Python interpreter: " base_python_interpreter
read -p "Your domain without protocol (for example, google.com): " project_domain

# Create and activate virtual environment
$base_python_interpreter -m venv env
source env/bin/activate

# Install required packages
sudo apt-get install libpq-dev
pip install -U pip
pip install -r requirements.txt

# Install PostgreSQL
sudo apt-get install postgresql postgresql-contrib

# Create PostgreSQL database and user
sudo -u postgres psql -c "CREATE DATABASE $POSTGRES_DB;"
sudo -u postgres psql -c "CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';"
sudo -u postgres psql -c "ALTER ROLE $POSTGRES_USER SET client_encoding TO '$POSTGRES_ENCODING';"
sudo -u postgres psql -c "ALTER ROLE $POSTGRES_USER SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $POSTGRES_USER SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;"

# Create symbolic links and restart services
sudo ln -s $project_path/nginx/site.conf /etc/nginx/sites-enabled/
sudo ln -s $project_path/systemd/gunicorn.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo service nginx restart
