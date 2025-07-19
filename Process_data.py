from flask import Flask, jsonify, request

App = Flask("MCAD.ProcessData")

@App.route('/processData', methods=['POST'])
def process_data():
    data = request.get_json()
    # Placeholder for data processing logic
    # In a real application, this could involve validation, transformation, or storage
    return "HELLO! \n\n WELCOME   " + data["username"], 200

App.run(port=5000, debug=True)  # Run the Flask application on port 5000 with debug mode enabled
# This code is for a simple Flask application that processes data and returns the username from the request