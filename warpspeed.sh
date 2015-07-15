# warpspeed.sh
# Commands here will be run each time a pull or push deploy is successfully run.

# Activate your virtualenv.
source env/bin/activate

# Install dependencies.
pip install -r requirements.txt

# Run the database migrations.
python manage.py db upgrade

# Restart passenger.
touch tmp/restart.txt

# Deactivate the virtualenv.
deactivate
