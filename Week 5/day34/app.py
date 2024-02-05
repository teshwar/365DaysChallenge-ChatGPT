from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Define a simple data model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Use app.app_context() to create an application context
with app.app_context():
    # Create the database tables
    db.create_all()

# Route to display items
@app.route('/')
def display_items():
    items = Item.query.all()

    # Print all items (for demonstration purposes)
    for item in items:
        print(f"Item ID: {item.id}, Name: {item.name}")
              
    return render_template('index.html', items=items)

# Route to add new item
@app.route('/add_item', methods=['POST'])
def add_item():
    print(request.form)
    new_item_name = request.form['item_name']
    new_item = Item(name=new_item_name)
    db.session.add(new_item)
    db.session.commit()
    return 'Item added successfully!'


if __name__ == '__main__':
    app.run(debug=True)
