"""Enhance your understanding of Flask with this hands-on coding exercise designed to reinforce your skills. 

Problem Statement: Implement a Flask API for fetching random quotes from a text file.
Solution"""

from flask import Flask, jsonify                # purpose of jsonify is to convert Python objects to JSON format
import random                                   # Importing random module to select a random quote

app = Flask("RandomQuoteApp")                   # Create a Flask application instance 

def get_random_quote():
    with open('quotes.txt', 'r') as file:       # Ensure 'quotes.txt' exists in the same directory with lines quotes
        quotes = file.readlines()               # Read all lines from the file into a list
    return random.choice(quotes).strip()        # Randomly select a quote from the file and remove any leading/trailing whitespace

@app.route('/random-quote')                     # Define a route to fetch a random quote by default 50000 port 

def random_quote():
    quote = get_random_quote()
    return jsonify({'Quotes': quote})            # Return the quote in JSON format

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Run the Flask application on port 5000 with debug mode enabled

# This code creates a simple Flask API that serves a random quote from a text file when accessed
# Ensure you have a 'quotes.txt' file in the same directory with quotes on each line
# To run the application, execute this script and access http://127.0.0.1:5000/random-quote
