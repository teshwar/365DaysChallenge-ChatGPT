from flask import Flask, render_template

app = Flask(__name__)

# Dynamic route that takes a name parameter
@app.route('/greet/<name>')
def greet_user(name):
    # Display a personalized message using the parameter from the URL
    greeting_message = f'Hello, {name}! Welcome to our website.'

    # Render the HTML template and pass the personalized message as a variable
    return render_template('greet.html', message=greeting_message)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
