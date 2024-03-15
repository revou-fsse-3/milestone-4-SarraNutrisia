from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.account import Account
from app.models.user import User
from app.connectors.mysql_connector import engine
from sqlalchemy.orm import sessionmaker

# Creating Blueprint
account_routes = Blueprint('account_routes', __name__)

# Function to get user's accounts
def check_account_ownership(account_id, user_id):
    
    # Database connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    account = session.query(Account).filter_by(id=account_id).first()
    
    try:
        # Check account belonging
        if account.user_id == user_id:
            return True
        else:
            return False
        
    except Exception as e:
        return False
    

# Post Method to Creating Account By User
@account_routes.route('/account', methods=['POST'])
@jwt_required()
def create_account():
    
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()
    
    # Request Data
    data = request.json
    account_type = data.get('account_type')
    account_number = data.get('account_number')
    balance = data.get('balance')
    
    # Creating New Account
    new_account = Account(user_id=user_id, account_type=account_type, account_number=account_number, balance=balance)
    
    try:
        # Input New Account to Database
        session.add(new_account)
        session.commit()
        return {'message': 'Successfully created'}, 201
    
    except Exception as e:
        # Error Input New Account to Database
        session.rollback()
        return {'error': f'Error has occurred: {e}'}, 500


# Get Method for Get All Data Account from All User
@account_routes.route('/account', methods=['GET'])
@jwt_required()
def get_all_account():
    
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()
    
    # Get Accounts from Database
    user = session.query(User).filter_by(id=user_id).first()
    accounts = user.accounts
    
    # Return Account to Dictionary
    return jsonify([account.to_dict() for account in accounts])


# Get Method for Get Data Account by ID
@account_routes.route('/account/<int:account_id>', methods=['GET'])
@jwt_required()
def get_account_by_ID(account_id):
    
    # Get JWT from user id
    user_id = get_jwt_identity()
    
    # Checking Owner of The Account
    if check_account_ownership(account_id, user_id):
        
        # Database Connection
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        
        # Get Account by ID from Database
        account = session.query(Account).filter_by(id=account_id).first()
        
        # Return Account to Dictionary
        return jsonify(account.to_dict())
    else:
        return {'error': 'User Is Not Allowed'}, 401
    

# Put Method to Update Account by ID
@account_routes.route('/account/<int:account_id>', methods=['PUT'])
@jwt_required()
def update_account_by_ID(account_id):
    
    # Get JWT from user id
    user_id = get_jwt_identity()
    
    # Checking Owner of The Account
    if check_account_ownership(account_id, user_id):
        
        # Database Connection
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        session.begin()
        
        # Request Data
        data = request.json
        account_type = data.get('account_type')
        account_number = data.get('account_number')
        balance = data.get('balance')
        
        # Get Data Account By ID
        account = session.query(Account).filter_by(id=account_id).first()
        
        try:
            # Updating Account
            account.account_type = account_type
            account.account_number = account_number
            account.balance = balance
            session.commit()
            return {'message': 'Successfully Updated'}, 200
        
        except Exception as e:
            # Error Update Account
            session.rollback()
            return {'error': f'Error Has Occurred: {e}'}, 500
    else:
        return {'error': 'User Is Not Allowed'}, 401


# Delete Method for Deleting Account By ID   
@account_routes.route('/account/<int:account_id>', methods=['DELETE'])
@jwt_required()
def delete_account(account_id):
    
    # Get JWT from user id
    user_id = get_jwt_identity()
    
    # Checking Owner of The Account
    if check_account_ownership(account_id, user_id):
        connection = engine.connect()
        Session = sessionmaker(connection)
        session = Session()
        session.begin()
        
        # Get Data Account By ID
        account = session.query(Account).filter_by(id=account_id).first()
        
        try:
            # Deleting Account
            session.delete(account)
            session.commit()
            return {'message': 'Successfully Deleted'}, 200
        
        except Exception as e:
            # Error Delete Account By ID
            session.rollback()
            return {'error': f'Error Has Occurred: {e}'}, 500
    else:
        return {'error': 'User Is Not Allowed'}, 401
