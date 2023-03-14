from flask import  jsonify, request, Blueprint #register a new user
#Organising related data   or code
# from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend.users.model import User
from backend.db import db

users = Blueprint('users', __name__, url_prefix='/users')

#get all users
@users.route("/")
def all_users():
    users= User.query.all()
    results = [
            {
                "name": user.name,
                "email": user.email,
                "contact": user.contact
                
            } for user in users]

    return users

# creating a new user
@users.route('/create', methods= ['POST',"GET"])
def create_user():
    user_name = request.json['name']
    user_email = request.json['email']
    user_contact = request.json['contact']
    user_address = request.json['address']
    user_type = 'author'
    user_password = request.json['password']
    hashed_password = generate_password_hash(user_password)
    # validations
    #username
    if not user_name:
        return jsonify({'Message':'Username is required'}),400  
    #email
    if not user_email:
        return jsonify({'Message':'Email is required'}),400  
      #contact
    if not user_contact:
        return jsonify({'Message':'Contact is required'}),400 
     #address
    if not user_address:
        return jsonify({'Message':'Address is required'}),400
    #password
    if not user_password:
        return jsonify({'message':'Password is required'}),400
    #password validation in length
    if len(user_password)< 6:
        return jsonify({'message': 'Password must be atleast 6 characters long'})
    
    #contraints
    if User.query.filter_by(email=user_email).first(): 
        return jsonify({'message':' This email is already in use'}),409
        #or
    existing_user_contact = User.query.filter_by(contact=user_contact).first()
    if existing_user_contact:
       return jsonify ({'message':'This contact is already in use'}),409


    #storing a new user
    new_user = User(name = user_name,email = user_email,contact=user_contact,address = user_address,usertype= user_type, password = hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success':True, 'message':'You have successfully created an account', 'data': new_user}),201






























#     elif request.method == "GET":
#         users= User.query.all()
#         results = [
#            {
#                 "name": user.name,
#                 "email": user.email,
#                 "contact": user.contact,
#                 "usertype":user.usertype,
#                 "password":user.password
#             } for user in users]

#         return {"count": len(results), "users": results}
      


# #update,get and delete user by id
# @users.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_user(user_id):
#     user = User.query.get_or_404(user_id)

#     if request.method == 'GET':
#         response = {
#             "name": user.name,
#             "email": user.email,
#             "contact": user.contact,
#             "password":user.password,
#             "address":user.address
#         }
#         return {"message": "success", "user": response}

#     elif request.method == 'PUT':
#         data = request.get_json()
#         user.name = data['name']
#         user.email = data['email']
#         user.contact = data['contact']
#         user.address = data['address']
#         user.password = data['password']
#         db.session.add(user)
#         db.session.commit()
#         return {"message": f"User details of {user.name} successfully updated"}

#     elif request.method == 'DELETE':
#         db.session.delete(user)
#         db.session.commit()
#         return {"message": f"User {user.name} successfully deleted."}   
  
        
  
   
