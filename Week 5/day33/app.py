"Even though we kinda covered this earlier on. This allows Modularity, Code Reusability and Seperation of Concern"
"""
Without render_template: 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<html><body><h1>Hello, Flask!</h1></body></html>'

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Pass variable to the template
    greeting_message = 'Hello, Flask!'
    return render_template('home.html', message=greeting_message)

if __name__ == '__main__':
    app.run(debug=True)

