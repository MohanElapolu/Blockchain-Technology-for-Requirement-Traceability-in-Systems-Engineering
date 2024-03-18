### Models file for web app...

from requirement_chain import db
from requirement_chain import bcrypt
from requirement_chain import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Initializing the database class to store Users
class User(db.Model, UserMixin):
    id   = db.Column(db.Integer(), primary_key=True, )
    username =  db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    public_key    = db.Column(db.String())
    private_key   = db.Column(db.String())

    #@property
    #def prettier_budget(self):
    #    if len(str(self.budget)) >= 4:
    #        return "${},{}".format(str(self.budget)[:-3], str(self.budget)[-3:])
    #    else:
    #        return "${}".format(self.budget)


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode("utf-8")

    @property
    def privatekey(self):
        return self.privatekey
    
    @privatekey.setter
    def privatekey(self, real_privatekey):
        self.privatekey = bcrypt.generate_privatekey(real_privatekey).decode("utf-8")
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    #def can_purchase(self, item_obj):
    #    return self.budget >= item_obj.price
    
    #def can_sell(self, item_obj):
    #    return item_obj in self.items

