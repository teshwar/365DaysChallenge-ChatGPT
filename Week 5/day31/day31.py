"""
Day 31: Flask Forms

    Extend your Flask application to handle form submissions.
    Implement a route that processes the form data and displays it on another page.
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a simple form with a single text input
class SimpleForm:
    def __init__(self):
        self.name = ""

# Initialize the form
simple_form = SimpleForm()

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html', form=simple_form)

# Route to handle form submissions
@app.route('/process_form', methods=['POST'])
def process_form():
    # Get the form data from the request
    simple_form.name = request.form['name']

    # Redirect to another page to display the form data
    return redirect(url_for('display_data'))

# Route to display the form data
@app.route('/display_data')
def display_data():
    return render_template('display_data.html', form=simple_form)

if __name__ == '__main__':
    app.run(debug=True)
