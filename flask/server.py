from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CA3"

@app.route("/Division")
def division(num1,num2):
    return 

if __name__ == "__main__":
    app.run(port=5000,debug=True)
