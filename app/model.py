from sqlalchemy import BigInteger, Column
from sqlalchemy.types import VARCHAR, TypeDecorator

from .crypto import decrypt, encrypt
from .extension import db


class EncryptedField(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        return encrypt(value)

    def process_result_value(self, value, dialect):
        return decrypt(value)


class MaskingPhoneNumberField(TypeDecorator):
    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        return encrypt(value)

    def process_result_value(self, value, dialect):
        v = decrypt(value)
        return f'{v[:3]}****{v[7:]}'


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(EncryptedField(128), nullable=False)
    birthday = Column(EncryptedField(128), nullable=False)
    phone_number = Column(MaskingPhoneNumberField(128), nullable=False)
