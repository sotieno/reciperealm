# RecipeRealm

## Project requirements
* Python version 3.8
* MySQL version 8.0

## Project setup (Local environment)
```
# clone repository
git clone https://github.com/leroysb/group-challenges.git

# change directory
cd group-challenges/django_projects/RecipeRealm

# activate virtual environment
source virtualenv/bin/activate

# install python3 packages
pip install -r requirements.txt

# setup database
cat setup_mysql.sql | mysql -h localhost -u root -p

# migrate accounts models
python3 manage.py makemigrations

# run serever locally
python3 manage.py runserver 
```
