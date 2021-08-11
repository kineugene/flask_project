from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["POST"])
def root():
    return 'Ok'


if __name__ == '__main__':
    app.run(host='192.168.0.31', port=80)
