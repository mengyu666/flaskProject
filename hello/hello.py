from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/hi')
def say_hello():
    return '<h1>hj, Flask!</h1>'


@app.route('/hello')
def hello():
    return redirect('http://www.example.com')


if __name__ == '__main__':
    app.run(debug=True)