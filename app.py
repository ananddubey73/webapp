from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(_name_)

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data['content'], data['author']
    else:
        return "Failed to fetch the quote.", ""

@app.route('/')
def index():
    quote, author = get_random_quote()
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', quote=quote, author=author, current_time=current_time)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80)
