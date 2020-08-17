from flask import Flask

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return 'WorkManager'

if __name__ == '__main__':
    webapp.run(port=80)