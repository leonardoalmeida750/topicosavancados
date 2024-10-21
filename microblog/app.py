#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Olá Mundo!'

@app.route('/contato')
def contato():
    return 'exemplo@email.com'

if __name__ == '__main__':
    app.run()