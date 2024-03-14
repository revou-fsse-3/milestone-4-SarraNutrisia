## Step to Installation Python Project with Poetry

1. Check if Poetry was installed before by typing command to CLI : poetry --version
2. If poetry wasn't installed, then install it : pip install poetry
3. Install flask : poetry add Flask
4. Activate .venv : .venv\Scripts\activate
5. Create file .gitignore to hidden few folders such as .env, .venv, .__pycache__
6. Open app folder -> __init__.py -> type import flask from Flask (if Flask doesn't working then hover your mouse to text "flask", click Quick Fix and choose to select a different intrepreter : Python 3.12.2 (.venv : Poetry) .\venv\Scripts\python.exe Recommended) after that you can write code and running the route http://127.0.0.1:5000 : poetry run flask --app app run
7. Create file .env to activate debug mode
8. Install dotenv plugin : poetry add poetry-dotenv-plugin
9. Import dotenv to file __init__.py and then running : poetry run flask --app app run , to check if Debug Mode is on.
10. Install SQLAlchemy for creating database connection : poetry add sqlalchemy
11. Install 