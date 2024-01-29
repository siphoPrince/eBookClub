from flask import Flask, render_template

app = Flask(__name__)

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