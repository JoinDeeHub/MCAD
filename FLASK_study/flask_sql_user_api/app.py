from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("flask_sql_user_api")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# DB model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}

# Create tables
with app.app_context():
    db.create_all()
    print("Database created successfully!")
    
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask User API. Use /register to POST and /user/<username> to GET."})


# Register user
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get("username") or not data.get("email"):
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter((User.username == data["username"]) | (User.email == data["email"])).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(username=data["username"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# Get user by username
@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
