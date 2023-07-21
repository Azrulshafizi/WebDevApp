from flask import Flask, render_template, request, redirect, url_for
from form import CreateMemberForm
from login import loginpage
import shelve, member


app = Flask(__name__)


@app.route('/')

def home():
    return render_template("home.html")

@app.route('/login')
def login():
    login = loginpage(request.form)

    return render_template('login.html',form=login)

@app.route('/CreateMember', methods=['GET','POST'])
def create_user():
    create_member_form = CreateMemberForm(request.form)
    if request.method == 'POST' and create_member_form.validate():
        member_dict = {}
        db = shelve.open('storage.db', 'c')
        try:
            member_dict = db['member']
        except:
            print("Error in retrieving Users from storage.db.")

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
        #         break
        members = member.member(create_member_form.first_name.data,
                         create_member_form.last_name.data,create_member_form.email.data,create_member_form.new_password.data,
                             create_member_form.dob.data,create_member_form.phonenumber.data,create_member_form.gender.data)
        member_dict[members.get_user_id()] = members
        db['member'] = member_dict
        # Test codes
        member_dict = db['member']
        members = member_dict[members.get_user_id()]
        print(members.get_first_name(), members.get_last_name(), "was stored in storage.db successfully with user_id == ", members.get_user_id())
        db.close()
        return redirect(url_for('login'))
    return render_template('CreateMember.html', create_member_form=create_member_form)

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



@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/retrieveMember')
def retrieveMember():
    member_dict = {}
    db = shelve.open('storage.db', 'r')
    member_dict = db['member']
    db.close()
    member_list = []
    for key in member_dict:
        member = member_dict.get(key)
        member_list.append(member)
    return render_template('retrieveMember.html',count=len(member_list), member_list=member_list)


if __name__ == '__main__':
    app.run()
