from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, DECIMAL
from app.models.base import Base
from sqlalchemy.sql import func

class Transaction(Base):

    # Define table name
    __tablename__ = 'transactions'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_account_id = mapped_column(Integer, ForeignKey('accounts.id'))
    to_account_id = mapped_column(Integer, ForeignKey('accounts.id'))
    amount = mapped_column(DECIMAL(10, 2))
    type = mapped_column(String(255))
    description = mapped_column(String(255))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    # Add relationship to Account model
    from_account = relationship('Account', foreign_keys=[from_account_id])
    to_account = relationship('Account', foreign_keys=[to_account_id])
    
    # Return data transaction as dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'from_account_id': self.from_account_id,
            'to_account_id': self.to_account_id,
            'amount': '{:.2f}'.format(self.amount),
            'type': self.type,
            'description': self.description,
            'created_at': self.created_at
        }
        
    # Return data transaction as string
    def __repr__(self):
        return f'<Transaction {self.id}>'