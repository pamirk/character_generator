from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world(name='Pamir'):
    name = request.args.get('name', name)
    return 'Hello {}!'.format(name)


if __name__ == '__main__':
    app.run()
