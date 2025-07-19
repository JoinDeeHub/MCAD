from flask import Flask, request, jsonify

app = Flask("myapp")

@app.route('/genrateTable', methods=['POST'])

def genrate_table():
    number = request.get_json()['table']
    tabledata = []
    for i in range(1, 11):
        tabledata.append(f"{number} * {i} = {number * i}")
    return tabledata

app.run(port=5000, debug=True) # Run the Flask application on the default port (5000)    