# RecipeRealm

## Introduction
RecipeRealm is an online platform that provides personalized recipe recommendations to users based on their dietary preferences, cooking skills, taste preferences, and ingredients on hand.

## Installation
### Project requirements
* Python version 3.8.10
* MySQL version 8.0.33

### Project setup (Local environment)
```
# clone repository
git clone https://github.com/leroysb/reciperealm.git

# change directory
cd RecipeRealm/

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
# app will not run without the required environment variables
echo "environmental variables" >> .env

# run server locally
python3 manage.py runserver
```

## Usage
* Users can search for recipes by entering ingredients, dietary restrictions, or cuisine type in the search bar
* Clicking on a recipe displays detailed information, including ingredients, instructions, and nutritional facts.

## Contributing
We welcome contributions from the community to enhance RecipeRealm. To contribute, please follow these steps:

* Fork the repository.
* Create a new branch: git checkout -b feature/your-feature
* Make your changes and commit them: git commit -m 'Add feature'
* Push to the branch: git push origin feature/your-feature
* Submit a pull request.
## Licensing
RecipeRealm is released under the [![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

