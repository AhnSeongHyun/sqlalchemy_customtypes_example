from .repo import get, insert


def insert_user(user_name, birthday, phone_number):
    insert(user_name, birthday, phone_number)


def get_user(user_id: int):
    return get(user_id)
