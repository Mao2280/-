from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('reg.html')

if __name__ == '__main__':
    app.run(debug=True)