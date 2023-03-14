from backend import create_app
from backend.users.model import User
from flask_migrate import Migrate
from backend.db import db 
from backend.publishingcompanies.pubco import PublishingCompany
from backend.books.book import Book


app = create_app('development')
migrate =Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User,PublishingCompany=PublishingCompany,Book=Book)

