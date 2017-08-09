# encoding:utf-8

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9092, debug=True)
