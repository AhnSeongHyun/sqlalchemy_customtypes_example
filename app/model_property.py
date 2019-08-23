from sqlalchemy import BigInteger, Column, String

from .crypto import decrypt
from .extension import db


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True, "mysql_engine": "InnoDB"}

    user_id = Column(BigInteger, primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)
    birthday = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False)

    @property
    def user_name(self):
        return decrypt(self.name)

    @property
    def user_birthday(self):
        return decrypt(self.birthday)

    @property
    def user_phone_number(self):
        return decrypt(self.phone_number)
