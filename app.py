from flask import Flask,request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello user!"

@app.route('/upload')
def upload():
    return "Uploading Stuff"


if __name__ == '__main__':
    app.run('0.0.0.0')