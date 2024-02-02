"""
Day 32: Dynamic Routing in Flask

    Create a dynamic route in Flask that takes a parameter from the URL.
    Use this parameter to display personalized messages on the webpage.

----------------------------

Dynamic Route Definition:
    Flask allows the creation of dynamic routes by adding variable parts to the URL. These variable parts are specified within < > brackets in the route definition.
    
    In this example, @app.route('/greet/<name>') defines a dynamic route that takes a parameter named name from the URL.
    - python3 app.py
    - go on http://127.0.0.1:5000/greet/{name}
      where whatever after greet will become custom and can be used in function.
"""