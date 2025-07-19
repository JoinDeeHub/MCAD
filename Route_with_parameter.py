from flask import Flask

# Create an instance of the Flask class
app = Flask("myapp")

# Define a route for the root URL ("/")
# This route will respond to GET requests
# The function takes a name as a parameter and returns a greeting message
@app.route('/hello/<name>')
def hello_world(name):
    """This function will be executed when the root URL is accessed"""
    return f'Hello, {name}!'

# Start the Flask application
if __name__ == '__main__':
    app.run(port=5001, debug=True) # Run on port 5001 with debug mode enabled
# This code is for a simple Flask application that serves a "Hello, World!" message.

#app.run(host='0.0.0.0', port=5050, debug=True) # host on all interfaces, port 5050, with debug mode enabled

