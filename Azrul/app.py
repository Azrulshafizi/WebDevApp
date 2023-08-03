from flask import Flask, render_template, request, redirect, url_for,session
from form import CreateMemberForm
from login import loginpage
import shelve, member
from staff_login import Staff_Login
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



# app = Flask(__name__)
# app.secret_key = "any-string-12345"


# @app.route('/')
#
# def home():
#
#     return render_template("home.html")
#
#
#
# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = loginpage(request.form)
#     if request.method == "POST":
#         phonenumber = request.form["phonenumber"]
#         password = request.form["password"]
#         member_dict = {}
#         db = shelve.open('storage.db', 'r')
#         member_dict = db['member']
#         db.close()
#         member_list = []
#         for key in member_dict:
#             member = member_dict.get(key)
#             member_list.append(member)
#         for member in member_list:
#             if member.get_phone_number() == phonenumber:
#                 if member.get_password() == password:
#                     return render_template('successful.html', member=member)
#                 else:
#                     return render_template('login.html',login=form)
#
#     return render_template('login.html',login=form)
#
#
#
#
# @app.route('/successful/<int:id>/')
# def successful(id):
#     member_dict = {}
#     db = shelve.open('storage.db', 'r')
#     member_dict = db['member']
#     db.close()
#     member_list = []
#     for key in member_dict:
#         member = member_dict.get(key)
#         member_list.append(member)
#     for member in member_list:
#         if member.get_phone_number() == id:
#             return render_template('successful.html',member=member)
#     return render_template('login.html')
#
#
#
# @app.route('/CreateMember', methods=['GET','POST'])
# def create_member():
#     create_member_form = CreateMemberForm(request.form)
#
#     if request.method == 'POST' and create_member_form.validate():
#         member_dict = {}
#         db = shelve.open('storage.db', 'c')
#         try:
#             member_dict = db['member']
#         except:
#             print("Error in retrieving Users from storage.db.")

        # eList = []
        # iList = []
        # for key in member_dict:
        #     email = member_dict.get(key)
        #     eList.append(key)
        #     for i in member_dict:
        #         nid = member_dict[i].get_user_id()
        #         iList.append(nid)
        #         if str(email) == str(member_dict[i].get_email()):
        #              global typo
        #              typo = "Email already in use"
        #              return render_template('CreateMember.html', typo=typo, form=create_user_form)
        #     print(create_member_form.first_name.data)
    #         members = member.member(create_member_form.first_name.data,
    #                          create_member_form.last_name.data,create_member_form.email.data,create_member_form.new_password.data,
    #                              create_member_form.dob.data,create_member_form.phonenumber.data,create_member_form.gender.data,
    #                                 create_member_form.image.data)
    #         member_dict[members.get_user_id()] = members
    #         db['member'] = member_dict
    #         # Test codes
    #         member_dict = db['member']
    #         members = member_dict[members.get_user_id()]
    #         print(members.get_first_name(), members.get_last_name(), "was stored in storage.db successfully with user_id == ", members.get_user_id())
    #         db.close()
    #         return redirect(url_for('login'))
    #     return render_template('CreateMember.html', form=create_member_form)
    #
    # @app.route('/profile/<int:id>/', methods=['GET','POST'])
    # def profile(id):
    #     member_dict = {}
    #     db = shelve.open('storage.db', 'r')
    #     member_dict = db['member']
    #     db.close()
    #     member_list = []
    #     for key in member_dict:
    #         member = member_dict.get(key)
    #         member_list.append(member)
    #
    #     return render_template('profile.html', member_list=member_list,id=id)
    #         break
#




# @app.route('/profile/<int:id>/', methods=['GET','POST'])
# def profile():
#     return render_template('profile.html')


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

# @app.route('/StaffLogin', methods=['GET','POST'])
# def StaffLogin():
#     stafflogin = Staff_Login(request.form)
#
#     if request.method == 'POST':
#         admin_staff = request.form['admin']
#         passwordstaff = request.form['password']
#         admin = ['123456']
#         password = ['123456']
#         print(admin_staff)
#         print(passwordstaff)
#         if admin == str(admin_staff):
#             if password == str(passwordstaff):
#                 return redirect(url_for('retrieveMember'))
#             else:
#                 return render_template('StaffLogin.html', stafflogin=stafflogin)
#     return render_template('StaffLogin.html',stafflogin=stafflogin)
#
# @app.route('/admin')
# def admin():
#     return render_template('admin.html')
#
# @app.route('/retrieveMember')
# def retrieveMember():
#     member_dict = {}
#     db = shelve.open('storage.db', 'r')
#     member_dict = db['member']
#     db.close()
#     member_list = []
#     for key in member_dict:
#         member = member_dict.get(key)
#         member_list.append(member)
#     return render_template('retrieveMember.html', count=len(member_list), member_list=member_list)
#
# @app.route('/forgotpassword')
# def forgotpassword():
#     return render_template('forgotpassword.html')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# @app.route('/')
# def Catalogue():
#     return render_template('CArt.html')


@app.route('/Form')
def Form():
    return render_template('Form.html')

@app.route('/')
def Catalogue():
    return render_template('Catalogue.html')


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form['product-id']  # Assuming you have a hidden input with the product ID in your form
    product_name = request.form['product-name']  # Replace with your actual field names
    product_price = float(request.form['product-price'])
    # Add more fields as needed


    with shelve.open('cart.db') as cart:
        if product_id in cart:
            cart[product_id]['quantity'] += 1
        else:
            cart[product_id] = {
                'name': product_name,
                'price': product_price,
                'quantity': 1,
                # Add more fields as needed
            }

    return redirect('/CArt')

@app.route('/CArt')
def show_cart():
    with shelve.open('cart.db') as cart:
        cart_items = cart.values()
        total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    return render_template('CArt.html', cart_items=cart_items, total_price=total_price)


if __name__ == '__main__':
    app.run(debug=True)
