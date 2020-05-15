from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/assignments')
def assignment_page():
    return render_template('assignment.html')


@app.route('/classes')
def class_page():
    return render_template('class.html')


if __name__ == '__main__':
    app.run(port=8000)
