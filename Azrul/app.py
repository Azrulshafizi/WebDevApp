from flask import Flask,flash, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    image_url = '/static/img/shoes.jpg'
    return render_template("home.html",image_url=image_url)

# @app.route('/', method=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)

if __name__ == '__main__':
    app.run()
