from flask import Flask

app = Flask('MCAD.App1')

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/aboutus')
def about_us():
    return "Welcome to the About Us Page!"

if __name__ == '__main__':
    app.run() # Run the Flask application on the default port (5000)
# This code is for a simple Flask application that serves a welcome message and an about us page