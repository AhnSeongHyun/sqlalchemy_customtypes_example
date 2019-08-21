from flask import Blueprint, jsonify, request

from .service import get_user, insert_user

bp = Blueprint('bp', __name__, url_prefix='/v1/users')


@bp.route('/<user_id>')
def get_user_route(user_id):
    user = get_user(user_id)
    return jsonify(
        {
            'user_name': user.name,
            'birthday': user.birthday,
            'phone_number': user.phone_number,
        }
    )


@bp.route('/', methods=['POST'])
def add_user_route():
    insert_user(**request.get_json())
    return jsonify({})
