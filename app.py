# app.py
from flask import Flask, render_template
import requests

app = Flask(_name_)

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return f"{data['content']} - {data['author']}"
    else:
        return "Failed to fetch the quote."

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5001)