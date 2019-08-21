from sqlalchemy import BigInteger, Column, event
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

    @property
    def user_name(self):
        return decrypt(self.name)

    @property
    def user_birthday(self):
        return decrypt(self.birthday)

    @property
    def user_phone_number(self):
        return decrypt(self.phone_number)


@event.listens_for(
    User.phone_number, "init_scalar", retval=True, propagate=True
)
def _init_phone_number(target, dict_, value):
    pass


@event.listens_for(User, 'after_configured')
def receive_after_configured():
    pass


@event.listens_for(User, 'after_insert')
def receive_after_insert(mapper, connection, target):
    pass


@event.listens_for(User, 'after_update')
def receive_after_update(mapper, connection, target):
    pass


@event.listens_for(User, 'init')
def receive_init(target, args, kwargs):
    print(target)
