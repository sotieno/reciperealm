# RecipeRealm

## Project requirements
* Python version 3.8
* MySQL version 8.0

## Project setup (Local environment)
```
# clone repository
git clone https://github.com/leroysb/group-challenges.git

# change directory
cd RecipeRealm

# make a virtual environment
python3 -m venv virtualenv

# activate virtual environment
source virtualenv/bin/activate # For Linux
source virtualenv/scripts/activate # For Windows

# install python3 packages
pip install -r requirements.txt

# setup database
cat setup_mysql.sql | mysql -h localhost -u root -p

# migrate database
python3 manage.py migrate

# reach out to one of the collaborators and request for the environment variables
# run server locally
python3 manage.py runserver