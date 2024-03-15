from app.models.base import Base
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column
from app.models.account import Account
 

class User(Base):

    # Define table name
    __tablename__ = 'users'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(255), unique=True)
    email = mapped_column(String(255), unique=True)
    password_hash = mapped_column(String(255))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Add relationship to Account model
    accounts = relationship('Account', back_populates='user')

    # Return data user as a dictionary
    def to_dict(self):
        return{
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    # Return data user as a string
    def __repr__(self):
        return f"<User {self.username}>"