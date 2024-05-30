from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! I am a Flask app running on a Docker container built using a Dockerfile!'

if __name__ == '__main__':
    app.run(debug=True)
