from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.sql import func
from app.models.base import Base

class Account(Base):
    
    # Define table name
    __tablename__ = 'accounts'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey('users.id'))
    account_type = mapped_column(String(255))
    account_number = mapped_column(String(255), unique=True)
    balance = mapped_column(DECIMAL(10, 2), default=0.00)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.now())
    
    # Add relationship to User model
    user = relationship('User', back_populates='accounts')
    
    # Return data account as dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'account_type': self.account_type,
            'account_number': self.account_number,
            'balance': '{:.2f}'.format(self.balance),
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    # Return data account as string
    def __repr__(self):
        return f'<Account {self.account_number}>'