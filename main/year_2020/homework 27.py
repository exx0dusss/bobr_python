from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
Bootstrap(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    print(f'We get index request: {request}')
    return render_template('test.html')

if __name__ == '__main__':
    app.run() 