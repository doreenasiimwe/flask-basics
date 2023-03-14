from backend.db import db

class User(db.Model):
   __tablename__ = 'users'
   id = db.Column( db.Integer, primary_key = True,autoincrement=True)
   name = db.Column( db.String(100),nullable = False)
   contact = db.Column(db.String(10),nullable = True, unique =True)  
   email = db.Column(db.String(200),unique = True,nullable = False)
   usertype = db.Column(db.String(10),nullable = False)
   password = db.Column(db.String(10),unique = True, nullable = False)
   books = db.relationship('Book', backref='users')
   publishing_companies = db.relationship('PublishingCompany', backref='users')
    
def __init__(self, name, contact, email,usertype,password):
   self.name = name
   self.contact = contact
   self.email = email
   self.usertype = usertype
   self.password = password  