from flask import Flask, render_template, request, redirect, url_for,flash
import os
from form import CreateUserForm,loginpage
import shelve, member, random
# from twilio.rest import Client
app = Flask(__name__)

image_folder = os.path.join('static','image')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/CreateMember', methods=['GET','POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")
        user = member.member(create_user_form.first_name.data,
                         create_user_form.last_name.data,create_user_form.email.data,create_user_form.new_password.data,
                             create_user_form.confirm_password.data,create_user_form.gender.data,None,None)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in storage.db successfully with user_id == ",user.get_user_id())
        db.close()
        return redirect(url_for('retrieve_users'))
    return render_template('CreateMember.html', form=create_user_form)

# def getOTP():
#     number = request.form[]
#     getOTPApi(number)
#     return number
#
# def generateOTP():
#     return random.randrange(100000,999999)
#
# def getOTPApi(number):
#     account_sid = 'ACf9b4b88a7f93c743ee05e26ea74363ad'
#     auth_token = '5b29488742a7a0ba954479380dd5bcae'
#     client = Client(account_sid,auth_token)
#     otp = generateOTP()
#     body = "your OTP is" +str(otp)
#     message = Client.messages.create(from='+6582054349',body=body,to=number)
#
#
#     if message.sid:
#         return True
#     else:
#         return False

@app.route('/login', methods=['GET'])
def login():
    login = loginpage(request.form)

    return render_template('login.html',form=login)

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
