from flask import Blueprint, request
from app.connectors.mysql_connector import engine
from sqlalchemy.orm import sessionmaker
from app.models.account import Account
from app.models.transaction import Transaction
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.account_routes import check_account_ownership


# Creating Blueprint
transaction_routes = Blueprint('transaction_routes', __name__)

# Function to Check if Account Has Sufficient Balance
def check_balance(account_id, amount, session):
    
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    account = session.query(Account).filter_by(id=account_id).first()
    
    try:
        # Check if Account Has Sufficient Balance
        if account and account.balance >= amount:
            return True
        else:
            return False
        
    except Exception as e:
        return False

# Function to Transfer Money
def transfer_money(from_account_id, to_account_id, amount, description, session):
    
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    
    # Request Data from Database
    from_account = session.query(Account).filter_by(id=from_account_id).first()
    to_account = session.query(Account).filter_by(id=to_account_id).first()
    
    try:
        # Update Balance
        from_account.balance -= amount
        to_account.balance += amount

        # Input New Transaction
        new_transaction = Transaction(from_account_id=from_account_id, to_account_id=to_account_id, amount=amount, type='transfer', description=description)

        # Adding New Transaction to Database
        session.add(new_transaction)
        session.commit()

        return True
    
    except Exception as e:
        # Error Transferring Balance
        session.rollback()
        print("Error occurred during transfer process:", str(e))
        return False

# Post Method for Transferring Balance
@transaction_routes.route('/transaction', methods=['POST'])
@jwt_required()
def transfer():
        
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()
    
    # Request Data
    data = request.json
    from_account_id = data.get('from_account_id')
    to_account_id = data.get('to_account_id')
    amount = data.get('amount')
    description = data.get('description')
    
    # Checking Owner of The Account
    if check_account_ownership(from_account_id, user_id) and check_account_ownership(to_account_id, user_id):
        
        # Check if Account Has Sufficient Balance
        if check_balance(from_account_id, amount, session):
            
            # Transfer Money
            if transfer_money(from_account_id, to_account_id, amount, description, session):
                return {'message': 'Successfully Transferred'}, 200
            else:
                return {'error': 'Error Has Occurred During Transfer Process'}, 500
        
        else:
            return {'error': 'Account Does Not Have Sufficient Balance'}, 400
    
    else:
        return {'error': 'User Not Allowed to Access This Account'}, 400


# Post Method for Withdrawal Money
@transaction_routes.route('/transaction/withdrawal', methods=['POST'])
@jwt_required()
def withdrawal():

    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()

    # Request Data
    data = request.json
    from_account_id = data.get('from_account_id')
    amount = data.get('amount')
    description = data.get('description')

    # Checking Owner of The Account
    if not check_account_ownership(from_account_id, user_id):
        return {'error': 'User Not Allowed to Access This Account'}, 400

    # Check if Account Has Sufficient Balance
    if not check_balance(from_account_id, amount, session):
        return {'error': 'Account Does Not Have Sufficient Balance'}, 400

    try:
        # Get Account
        from_account = session.query(Account).filter_by(id=from_account_id).first()

        # Update Balance
        from_account.balance -= amount

        # Input New Transaction
        new_transaction = Transaction(from_account_id=from_account_id, to_account_id=None, amount=amount, type='withdrawal', description=description)  # Indicate withdrawal

        # Adding New Transaction to Database 
        session.add(new_transaction)
        session.commit()

        return {'message': 'Successfully Withdrawn'}, 200

    except Exception as e:
        session.rollback()
        return {'error': f'Error Has Occurred During Withdrawn Process: {e}'}, 500
    

# Post Method for Deposit Money
@transaction_routes.route('/transaction/deposit', methods=['POST'])
@jwt_required()
def deposit():

    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()

    # Request Data
    data = request.json
    to_account_id = data.get('to_account_id')
    amount = data.get('amount')
    description = data.get('description')

    # Checking Owner of The Account
    if not check_account_ownership(to_account_id, user_id):
        return {'error': 'User Not Allowed to Access This Account'}, 400

    try:
        # Get Account
        to_account = session.query(Account).filter_by(id=to_account_id).first()

        # Update Balance
        to_account.balance += amount

        # Input New Transaction
        new_transaction = Transaction(from_account_id=None, to_account_id=to_account_id, amount=amount, type='deposit', description=description)  

        # Adding New Transaction to Database 
        session.add(new_transaction)
        session.commit()

        return {'message': 'Successfully Deposited'}, 200

    except Exception as e:
        session.rollback()
        return {'error': f'Error Has Occurred During Deposit Process: {e}'}, 500
    

# Get Method for Get All Data Transaction
@transaction_routes.route('/transaction', methods=['GET'])
@jwt_required()
def get_all_transaction():
        
    # Database Connection
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    user_id = get_jwt_identity()
    
    try:
        # Fetch transaction
        transactions = session.query(Transaction).join(Account, Transaction.from_account_id == Account.id).filter(Account.user_id == user_id).all()
        return {'transactions list': [transaction.to_dict() for transaction in transactions]}, 200
    
    except Exception as e:
        # Error getting data transaction
        return {'error': f'Error Has Occurred: {e}'}, 500


# Get Method for Get Data Transaction By ID
@transaction_routes.route('/transaction/<int:account_id>', methods=['GET'])
@jwt_required()
def get_transactions_by_account(account_id):
            
            # Database Connection
            connection = engine.connect()
            Session = sessionmaker(connection)
            session = Session()
            user_id = get_jwt_identity()
            
            # Checking Owner of The Account
            if check_account_ownership(account_id, user_id):
                
                try:
                    # Fetch transaction
                    transactions = session.query(Transaction).filter_by(from_account_id=account_id).all()
                    return {'transaction by ID': [transaction.to_dict() for transaction in transactions]}, 200
                
                except Exception as e:
                    # Error getting data transaction
                    return {'error': f'Error Has Occurred: {e}'}, 500
            
            else:
                return {'error': 'User Not Allowed to Access This Account'}, 400