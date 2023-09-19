from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'CA':'3', 'Member 1':'Muhammad Shehzad (20I-1756)', 'Member 2':'Zahid Imran (20I-0469)'})


@app.route('/cal/add/<num1>/<num2>')
def add(num1, num2):
    try:
        result = int(num1) + int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."})


#div function added
@app.route('/cal/div/<num1>/<num2>')
def div(num1, num2):
    try:
        result = int(num1) // int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."})

@app.route('/cal/mul/<num1>/<num2>')
def mul(num1, num2):
    try:
        result = int(num1) * int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."})


if __name__ == '__main__':
    app.run(port=5000,debug=True)