# Documentation 📚


🔎 **_This is assignment for Week 19 Project Milestone 4 on Revou FSSE Section Seoul._** 🔎



*Theme Name :* Create A Flask Banking App for Managing A Bank With Python

*Author :* Sarra Nutrisia

*Created :* 15/03/2024 

*Python Version :* 3.12

*Flask Version :* 3.0.2

*Poetry Dotenv Plugin Version :* 0.2.0

*Sqlalchemy Version :* 2.0.28

*Mysql-connector-python Version :* 8.3.0

*Poetry-dotenv-plugin Version :* 0.2.0

*Bcrypt Version :* 4.1.2

*Flask-jwt-extended Version :* 4.6.0

*Pytest Version :* 8.1.1

*Pytest-cov Version :* 4.1.0



Python is a high-level programming language commonly used for web development, data analysis, artificial intelligence, and many other applications. It is known for its clean syntax and ease of understanding, as well as its great flexibility. Flask is one of the popular web frameworks for Python. It is designed to create web applications quickly and easily, with a focus on simplicity and flexibility. Flask does not require many external tools or libraries, making it suitable for small to medium-sized projects. Poetry is a dependency management tool for Python projects. It allows you to define your project's dependencies in a pyproject.toml file and manage their installation, updates, and configuration consistently. Poetry is often used in modern Python application development due to its intuitive abilities and seamless integration with other tools in the Python ecosystem. This week, I have build a Flask Banking App for Managing A Bank With Python and it's dependencies.


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
16. Install poetry together with pytest to manage project dependencies and run tests consistently in isolated environments : `poetry add pytest`, then run the tests by running on CLI : `poetry run pytest`.
17. Install pytest-cov to see how well your code is covered by tests, thus helping identify parts of the code that need improved test coverage : `poetry add pytest-cov`.


# Documentation API Link 🚀
You can check the Documentation API by clicking this link : [Link Postman](https://documenter.getpostman.com/view/29004934/2sA2xmWBZb) 
  
***

#### Theme by Sarra Nutrisia &#127776;
If you have any other questions that aren't covered in the documentation, feel free to e-mail &#128233; <sarra.nutrisia@gmail.com>.