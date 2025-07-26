from flask import Flask, request, jsonify
from bson import ObjectId
from pymongo import MongoClient

app = Flask("flask_mongo_todo_api")
client = MongoClient('mongodb://localhost:27017/')
db = client.todo_db
todo_collection = db.todos

# Convert ObjectId to string
def serialize(todo):
    todo['_id'] = str(todo['_id'])
    return todo

@app.route('/todo', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data.get("task"):
        return jsonify({"error": "Task is required"}), 400
    result = todo_collection.insert_one({"task": data["task"], "done": False})
    return jsonify({"message": "Todo added", "id": str(result.inserted_id)}), 201

@app.route('/todo', methods=['GET'])
def get_todos():
    todos = [serialize(todo) for todo in todo_collection.find()]
    return jsonify(todos)

@app.route('/todo/<id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    update = {}
    if "task" in data:
        update["task"] = data["task"]
    if "done" in data:
        update["done"] = data["done"]
    if not update:
        return jsonify({"error": "No fields to update"}), 400

    result = todo_collection.update_one({"_id": ObjectId(id)}, {"$set": update})
    if result.matched_count == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"message": "Todo updated"})

@app.route('/todo/<id>', methods=['DELETE'])
def delete_todo(id):
    result = todo_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"message": "Todo deleted"})

if __name__ == '__main__':
    app.run(debug=True)
