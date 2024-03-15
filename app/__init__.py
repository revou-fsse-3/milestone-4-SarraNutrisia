from flask import Flask
from dotenv import load_dotenv
from app.controllers.user_routes import user_routes
from app.controllers.account_routes import account_routes
from flask_jwt_extended import JWTManager
import os

# Load .venv
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Define JWT secret key
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

#Register Blueprint
app.register_blueprint(user_routes)
app.register_blueprint(account_routes)

#Set the root route
@app.route('/')
def index():
    return "Hello, World!"
