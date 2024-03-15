# Documentation 📚


🔎 **_This is assignment for Week 19 Project Milestone 4 on Revou FSSE Section Seoul._** 🔎



*Theme Name :* Create A Flask Banking App for Managing A Bank With Python

*Author :* Sarra Nutrisia

*Created :* 15/03/2024 

*Python Version :* 3.12

*Flask Version :* 3.0.2

*Poetry Dotenv Plugin Version :* 0.2.0

*Flask SQL Alchemy Version :* 3.1.1

*Psycopg2 Version :* 2.9.9






## Step to Create Python Project with Poetry

1. Check if Poetry was installed before by typing command to CLI : `poetry --version`.
2. If poetry wasn't installed, then install it : `pip install poetry`.
3. Install flask : `poetry add Flask`.
4. Activate .venv : `.venv\Scripts\activate`.
5. Create file .gitignore to hidden few folders such as `.env, .venv, .__pycache__` .
6. Open app folder -> __init__.py -> type import flask from Flask (if Flask doesn't working then hover your mouse to text "flask", click Quick Fix and choose to select a different intrepreter : `Python 3.12.2 (.venv : Poetry) .\venv\Scripts\python.exe Recommended`) after that you can write code and running the route http://127.0.0.1:5000 : `poetry run flask --app app run`.
7. Create file .env to activate the debug mode.
8. Install dotenv plugin : `poetry add poetry-dotenv-plugin`.
9. Import dotenv to file __init__.py and then running : `poetry run flask --app app run` , to check if Debug Mode is on.
10. Install SQLAlchemy for creating database connection : `poetry add sqlalchemy`.
11. Then you can create database and tables at MySQL Server. Don't forget to make getenv for your database information key.
12. Install MySQL connector : `poetry add mysql-connector-python`.
13. You can create CRUD operation according to project's requirement.
14. Install bcrypt for securely storing passwords in web applications : `poetry add bcrypt`.
15. Install flask-jwt-extended for securely transmitting information between parties as a JSON object : `poetry add flask-jwt-extended`.