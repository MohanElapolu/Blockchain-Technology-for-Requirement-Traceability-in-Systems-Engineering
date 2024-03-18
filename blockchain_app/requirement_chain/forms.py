###Forms for the web page...

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from requirement_chain.models import User

#This will be used for user registration
class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists! Please try a different username")
    
    def validate_email_address(self, email_address_to_check):
        email_address=User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email Address already exists! Please try a different email address")
    
    username = StringField(label="User Name", validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label="Email Address:", validators = [Email(),  DataRequired()])
    password1 = PasswordField(label="Password", validators= [Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password", validators=[EqualTo("password1"), DataRequired()])
    submit    = SubmitField(label="Create Account")

#This will be used for login page
class WalletForm(FlaskForm):
    public_key = StringField(label="Public Key", validators=[DataRequired()])
    private_key  = StringField(label="Private Key", validators=[DataRequired()])
    submit   = SubmitField(label="Load Wallet")

#This will be used for node network
class AddNodeForm(FlaskForm):
    add_Node_URL = StringField(label="Add Node URL", validators=[DataRequired()])
    #private_key  = StringField(label="Private Key", validators=[DataRequired()])
    submit   = SubmitField(label="Add")

#This will be used for node network
class RemoveNodeForm(FlaskForm):
    remove_Node_URL = StringField(label="Remove Node URL", validators=[DataRequired()])
    #private_key  = StringField(label="Private Key", validators=[DataRequired()])
    submit   = SubmitField(label="Remove")

#This will be used for Adding Requirement Block
class AddBlockForm(FlaskForm):
    path_artifact = StringField(label="Enter Path to requirement artifact", validators=[DataRequired()])
    submit        = SubmitField(label="Add Requirement Block")

#This will be used for login page
class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit   = SubmitField(label="Sign in")