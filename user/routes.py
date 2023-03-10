from flask import Flask
from app import app 
#from app.py imports the app instance
import user.models as models
#from thr user folder from modeld file imports User class
User=models.User
@app.route('/user/signup', methods=['GET'])
def signup():
    return User().signup() 
#creates new class instance 