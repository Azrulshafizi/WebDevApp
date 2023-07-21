from wtforms import Form, StringField, SelectField, validators, EmailField,TelField, DateField
import wtforms.fields as fld
class CreateMemberForm(Form):
    first_name = StringField("First Name",[validators.Length(min=1,max=30),validators.data_required()])
    last_name = StringField("Last Name", [validators.Length(min=1, max=30), validators.data_required()])
    email = EmailField("Email",[validators.data_required()])
    new_password = fld.PasswordField()
    confirm_password = fld.PasswordField(validators=[validators.EqualTo("new_password")])
    dob = DateField('Date',format='%Y-%m-%d')
    gender = SelectField('Gender', [validators.DataRequired()],choices=[('','Select'),('F','Female'),('M','Male')],default='')
    phonenumber = TelField("Phone Number",[validators.Length(min=8,max=8), validators.data_required()])
#
class loginpage(Form):
    phonenumber = TelField("Phone Number",[validators.Length(min=8,max=8), validators.data_required()])
    passwrd = fld.PasswordField('Password')
