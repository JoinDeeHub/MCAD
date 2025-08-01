import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:addm@localhost/configuration_data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ConfigData(db.Model):
    __tablename__ = 'configuration_data'

    id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.String(50), unique=True, nullable=False)
    config_json = db.Column(db.JSON, nullable=False)

    def __repr__(self):
        return f"<{self.section}: {self.config_json}>"