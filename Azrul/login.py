from wtforms import Form, StringField, SelectField, validators, EmailField,TelField, DateField
import wtforms.fields as fld

class loginpage(Form):
    phonenumber = TelField("Phone Number",[validators.Length(min=8,max=8), validators.data_required()])
    passwrd = fld.PasswordField('Password')