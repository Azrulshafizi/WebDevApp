from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')

def home():
    return render_template("home.html")
@app.route('/transaction')
def contact():
    return render_template('transactions.html')

if __name__ == '__main__':
    app.run()
