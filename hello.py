from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>hj, Flask!</h1>'


if __name__ == '__main__':
    app.run(debug=True)