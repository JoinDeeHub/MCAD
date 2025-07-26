from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello, Flask with MongoDB!'

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({'username': user['username'], 'email': user['email']})
    return jsonify(result)

@app.route('/users', methods=['POST'])
def add_user():
    user_data = request.get_json()
    mongo.db.users.insert_one(user_data)
    return 'User added to the database!'

if __name__ == '__main__':
    app.run()
