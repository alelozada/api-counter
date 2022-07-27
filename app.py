from flask import Flask
from flask import request

from counter import *

app = Flask(__name__)

@app.route('/status')
def status():
    return {'msg': 'OK'}, 200

@app.route('/counter_common_word')
def counter_common_word():
    word = request.args.get('word', default = 'ey', type = str)
    f = openFile("msg.txt")
    words = counter(f, word)
    return {'counter': words}, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)