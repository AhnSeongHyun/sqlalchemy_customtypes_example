from typing import Optional

from .extension import db
from .model import User


def insert(user_name: str, birthday: str, phone_number: str) -> None:
    with db.session.begin():
        db.session.add(
            User(name=user_name, birthday=birthday, phone_number=phone_number)
        )


def get(user_id: int) -> Optional[User]:
    user = User.query.filter_by(user_id=user_id).scalar()
    return user
