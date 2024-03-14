from app.models.user import User
from flask import Blueprint, request, jsonify
from app.connectors.mysql_connector import engine
from sqlalchemy.orm import sessionmaker

#Creating Blueprint
user_route = Blueprint('user_route', __name__)

#Get Method for Register
@user_route.route('/register', methods=['GET'])
def register():
    return {'message':'Successfully registered'}, 200
