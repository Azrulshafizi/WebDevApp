from flask import Flask, render_template, request, redirect, url_for,flash
import os

app = Flask(__name__)

image_folder = os.path.join('static','image')

app.config['UPLOAD_FOLDER'] = image_folder

@app.route('/')

def home():
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'shoes.png')
    print(img)
    return render_template("home.html", user_image=img)





if __name__ == '__main__':
    app.run()
