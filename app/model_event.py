from sqlalchemy import BigInteger, Column, String, event

from .crypto import decrypt, encrypt
from .extension import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)
    birthday = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)


def encrypt_user(target: User) -> User:
    target.name = encrypt(target.name)
    target.phone_number = encrypt(target.phone_number)
    target.birthday = encrypt(target.birthday)
    return target


def decrypt_user(target: User) -> User:
    target.name = decrypt(target.name)
    target.phone_number = decrypt(target.phone_number)
    target.birthday = decrypt(target.birthday)
    return target


@event.listens_for(User, 'before_insert')
def handler_before_insert(mapper, connection, target):
    return encrypt_user(target)


@event.listens_for(User, 'before_update')
def handler_before_update(mapper, connection, target):
    return encrypt_user(target)


@event.listens_for(User, 'load')
def handler_load(target, context):
    return decrypt_user(target)
