from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CA3"

@app.route("/division")
def division(num1,num2):
    if num1==0:
        return "Wrong Input"
    else:
        return num1/num2


if __name__ == "__main__":
    app.run(port=5000,debug=True)
