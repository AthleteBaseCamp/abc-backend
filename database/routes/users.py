from flask import request, jsonify, Blueprint
from database.db import execute_query, fetch_query

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    query = "SELECT * FROM users"
    users = fetch_query(query)
    return jsonify(users)

@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    query = "SELECT * FROM users WHERE id = %s"
    user = fetch_query(query, (id,))
    return jsonify(user)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    query = "INSERT INTO users (name, email, password, phone_number, is_coach) VALUES (%s, %s, %s, %s, %s)"
    user_id = execute_query(query, (data['name'], data['email'], data['password'], data['phone_number'], data['is_coach']))
    return jsonify({'id': user_id})

@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    query = "UPDATE users SET name = %s, email = %s, password = %s, phone_number = %s, is_coach = %s WHERE id = %s"
    execute_query(query, (data['name'], data['email'], data['password'], data['phone_number'], data['is_coach'], id))
    return jsonify({'id': id})

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    query = "DELETE FROM users WHERE id = %s"
    execute_query(query, (id,))
    return jsonify({'id': id})
