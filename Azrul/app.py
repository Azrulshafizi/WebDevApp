from flask import Flask, render_template, request, redirect, url_for,flash
import os
from form import CreateUserForm,loginpage
import shelve, member
app = Flask(__name__)

image_folder = os.path.join('static','image')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')

def home():
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'shoes.png')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'ladies.png')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'mens.png')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'kids.png')
    promo = os.path.join(app.config['UPLOAD_FOLDER'], 'promotion.jpg')
    return render_template("home.html", user_image=img,user_image1=img2,user_image2=img3,user_image3=img4, promo=promo)

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
                         create_user_form.last_name.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in storage.db successfully with user_id == ",user.get_user_id())
        db.close()
        return redirect(url_for('retrieve_users'))
    return render_template('CreateMember.html', form=create_user_form)

@app.route('/login', methods=['GET'])
def login():
    login = loginpage(request.form)

    return render_template('login.html',form=login)

@app.route('/admin')
def admin():
    return render_template('admin.html')



if __name__ == '__main__':
    app.run()
