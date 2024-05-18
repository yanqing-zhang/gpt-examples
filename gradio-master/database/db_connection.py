import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from vendor.yamler import yml
"""
数据库连接配置
"""
db_username = os.getenv("DB_USER_NAME")
db_password = os.getenv("DB_USER_PWD")
db_host = yml.yaml_content['database']['db_host']
db_port = yml.yaml_content['database']['db_port']
db_name = yml.yaml_content['database']['db_name']

app = Flask(__name__)
"""
数据库连接 mysql://账号:密码@localhost:3306/数据库名
"""
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
db = SQLAlchemy()
db.init_app(app)

def config_app():
    return app
def config_db():
    return db
