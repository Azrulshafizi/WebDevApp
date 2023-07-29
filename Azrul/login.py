from wtforms import Form, StringField, SelectField, validators, EmailField,TelField, DateField,SubmitField
import wtforms.fields as fld
from flask_wtf import FlaskForm
class loginpage(FlaskForm):
    phonenumber = TelField("Phone Number",[validators.Length(min=8,max=8), validators.data_required()])
    password = fld.PasswordField('Password')
    submit = SubmitField(label="Login now")