from flask import Flask, render_template, request, redirect, url_for,flash
import os

app = Flask(__name__)

imagefolder = os.path.join('static','image')

app.config['UPLOAD_FOLDER'] = imagefolder

@app.route('/')

def home():
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'shoes.jpg')
    return render_template("home.html", user_image=img1)



if __name__ == '__main__':
    app.run()
