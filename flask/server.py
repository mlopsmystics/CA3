from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'CA':'3', 'Member 1':'Muhammad Shehzad (20I-1756)','Member 3':'Ali  (20I-0512)'})


@app.route('/cal/add/<num1>/<num2>')
def add(num1, num2):
    try:
        result = int(num1) + int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."})

@app.route('/cal/sub/<num1>/<num2>')
def sub(num1, num2):
    try:
        result = int(num1) - int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid numbers."})
    
if __name__ == '__main__':
    app.run(port=5000,debug=True)