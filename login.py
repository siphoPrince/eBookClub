from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple hardcoded user credentials (replace with a proper database in a real-world application)
users = {
    "sipho": "123"
}


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        # Redirect to the main page or some other page after successful login
        return redirect(url_for('main'))
    else:
        # Redirect back to the login page if the credentials are invalid
        return redirect(url_for('login'))


@app.route('/main')
def main():
    return "You have successfully logged in!"


if __name__ == '__main__':
    app.run(debug=True)
