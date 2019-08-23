from sqlalchemy import BigInteger, Column
from sqlalchemy.types import VARCHAR, TypeDecorator

from .crypto import decrypt, encrypt
from .extension import db


class EncryptedField(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        print(f'process_bind_param : {value} {encrypt(value)}')
        return encrypt(value)

    def process_result_value(self, value, dialect):
        print(f'process_result_value : {value} {decrypt(value)}')
        return decrypt(value)


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(EncryptedField(128), nullable=False)
    birthday = Column(EncryptedField(128), nullable=False)
    phone_number = Column(EncryptedField(128), nullable=False)
