"""
Day 29: Introduction to Flask

    Set up a basic Flask application.
    Create a route that returns a simple "Hello, Flask!" message.

    Introduction to Flask, a web webframeowrk for Python.

"""

from flask import Flask

# Special variabel to represent name of current module
# Flask used it to determine the root path of the application
app = Flask(__name__)

#route
# route is a url pattern associated with a function
# called when this url is visited

#decorato associate '/' with the hello_flask
@app.route('/')
def hello_flask():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug = True)