from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy


import os
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask("FLASK_LAB_user_form", template_folder='MCAD/FLASK_LAB_user_form/templates')


# Connect to MySQL database

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:addm@localhost/FLASK_lab'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# User table

class User(db.Model):

   id = db.Column(db.Integer, primary_key=True)

   username = db.Column(db.String(100))

   password = db.Column(db.String(100))

   email = db.Column(db.String(100))


@app.route('/')

def home():

   return render_template('form.html')


@app.route('/submit', methods=['POST'])

def submit():

   username = request.form['username']

   password = request.form['password']

   email = request.form['email']


   new_user = User(username=username, password=password, email=email)

   db.create_all() # this creates table.

   db.session.add(new_user)

   db.session.commit()


   return 'User saved successfully!'



@app.route('/users')

def show_users():

   users = User.query.all()  # Get all users from database

   return render_template('users.html', users=users)




if __name__ == '__main__':

   app.run(debug=True)