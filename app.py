from flask import Flask
import tkinter
app = Flask(__name__)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Caleb and Josh!'


if __name__ == '__main__':
    app.run()
