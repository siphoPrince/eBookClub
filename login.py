<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from Models.User_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from Models import storage
from flask_login import login_user, login_required, logout_user, current_user

app_login = Blueprint('app_login', __name__)
>>>>>>> 1facef02707e4fc6f29ad81f631503c5a9f66ffd


<<<<<<< HEAD
=======
users = {
    "sipho": "123"
}


>>>>>>> 1facef02707e4fc6f29ad81f631503c5a9f66ffd
@app.route('/')
def index():
    return render_template("index.html")

@app.route('register', methods=['GET', 'POST'])
def register():
    if register.method == 'POST':
        pass
    return render_template(register.html)


if __name__ == '__main__':
    app.run(debug=True)