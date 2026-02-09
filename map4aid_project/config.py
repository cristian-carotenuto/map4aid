from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

#accesso per admin 
ADMIN_EMAIL = "map4aid01@gmail.com" 
ADMIN_CODE = "adminadmin"