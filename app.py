from flask import Flask, render_template, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

TRUMP_QUOTES = [
    "Despite the negative press covfefe.",
    "I will build a great wall and nobody builds walls better than me.",
    "I think I am actually humble. I think I'm much more humble than you would understand.",
    "I have a very good brain and I've said a lot of things.",
    "I know words, I have the best words.",
    "Nobody knew health care could be so complicated.",
    "I'm really rich. I'll show you that in a second.",
    "All of the women on The Apprentice flirted with me - consciously or unconsciously. That's to be expected.",
    "My IQ is one of the highest - and you all know it.",
    "Sorry losers and haters, but my IQ is one of the highest - and you all know it!"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quote')
def get_quote():
    return jsonify({'quote': random.choice(TRUMP_QUOTES)})

if __name__ == '__main__':
    app.run(port=5001)
