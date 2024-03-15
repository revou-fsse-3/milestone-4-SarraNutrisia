from app.models.user import User
from flask import Blueprint, request, jsonify
from app.connectors.mysql_connector import engine
from sqlalchemy.orm import sessionmaker
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies

#Creating Blueprint
user_routes = Blueprint('user_routes', __name__)

#Get Message Method for Register
@user_routes.route('/register', methods=['GET'])
def get_data_register():
    return {'message':'Successfully registered'}, 200

#Post Method for Register
@user_routes.route('/register', methods=['POST'])
def create_register():
    
    # Database connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    session.begin()
   
    # Request data
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password_hash')
    
    # Hashing password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(username=username, email=email, password_hash=hashed_password)
    
    try:
        # Successfully add new user to database
        session.add(new_user)
        session.commit()
        
        return {'message': 'User has created successfully'}, 201
    
    except Exception as e:
        # Error adding new user to database
        session.rollback()
        return {'error': f'Error has occured: {e}'}, 500


# Get Method for Login Page
@user_routes.route('/login', methods=['GET'])
def get_login_page():
    return {'message': 'User login page'}, 200

# Post Method for Input Data Login
@user_routes.route('/login', methods=['POST'])
def input_login():
        
        # Database connection
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        
        # Request data
        data = request.json
        email = data.get('email')
        password = data.get('password_hash')
        
        # Get user from database
        user = session.query(User).filter_by(email=email).first()
        
        try:
            # Checking if username already registered and the password is correct
            if user:
                if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                    access_token = create_access_token(identity=user.id)
                    return {'access_token': access_token}, 200
                else:
                    return {'message': 'Incorrect Password'}, 401
            else:
                return {'message': 'User was not registered'}, 404
        
        except Exception as e:
            return {'error': f'Error has occured: {e}'}, 500


# Get Method from All User's Data       
@user_routes.route('/users', methods=['GET'])
def get_all_users():
    
    # Database connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    
    try:
        # Fetching users from database
        users = session.query(User).all()
        
        # Convert users to dictionary
        user_data = [user.to_dict() for user in users]
        
        return {'users': user_data}, 200
    
    except Exception as e:
        # Error getting all user's data
        return {'error': f'Error has occured: {e}'}, 500


# Get Method from User By ID
@user_routes.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    
    # Database connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    
    try:
        # Fetching users from database
        user = session.query(User).filter_by(id=user_id).first()
        
        if user:
            # Checking if user was registered
            return user.to_dict(), 200
        else:
            # Checking if user was not registered
            return {'message': 'User was not registered'}, 404
        
    except Exception as e:
        # Error getting user by ID
        return {'error': f'Error has occured: {e}'}, 500
    
@user_routes.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_by_id(user_id):
        
        # Database connection
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        session.begin()
        
        # Request Data
        data = request.json
        username = data.get('username')
        email = data.get('email')
        
        try:
            # Fetching users from database
            user = session.query(User).filter_by(id=user_id).first()
            
            if user:
                # Checking if user was registered
                user.username = username
                user.email = email
                session.commit()
                return {'message': 'Successfully updated'}, 200
            else:
                # Checking if user was not registered
                return {'message': 'User was not registered'}, 404
            
        except Exception as e:
            # Error update user by ID
            session.rollback()
            return {'error': f'Error has occured: {e}'}, 500
        
@user_routes.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_by_ID(user_id):
        
        # Database connection
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        session.begin()
        
        try:
            # Fetching users from database
            user = session.query(User).filter_by(id=user_id).first()
            
            if user:
                # Checking if user was registered
                session.delete(user)
                session.commit()
                return {'message': 'Successfully deleted'}, 200
            else:
                # Checking if user was not registered
                return {'message': 'User was not registered'}, 404
            
        except Exception as e:
            # Error deleting user by ID
            session.rollback()
            return {'error': f'Error has occured: {e}'}, 500
        

# Post Method for User Logout
@user_routes.route('/logout', methods=['POST'])
def logout_user():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)
    return response
