from app import app
from app import db

import view

if __name__ == '__main__':
	db.create_all()
	app.secret_key = "777"
	app.run()
