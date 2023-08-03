from wtforms import Form, StringField, SelectField, validators, EmailField,TelField, DateField,FileField, SubmitField,RadioField
import wtforms.fields as fld
class addressform(Form):
    country = RadioField("country", choices=[('Singapore'),('Malaysia')])
    company = StringField("company", [validators.Length(min=1, max=30), validators.Optional()])
    address = StringField("address",[validators.data_required()])
    house = StringField("house", [validators.Length(min=1, max=30), validators.Optional()])
    postal_code = StringField("postal code", [validators.Length(min=1, max=10), validators.Optional()])
    submit = SubmitField()


