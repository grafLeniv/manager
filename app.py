#import sqlite3
#import os

from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy


from flask_session  import  Session


#from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



#login_manager = LoginManager(app)
#login_manager.login_view = 'login'
#login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
#login_manager.login_message_category = "success"



#@login_manager.user_loader
#def load_user(user_id):
#    print("load_user")
#    return UserLogin().fromDB(user_id, dbase)


