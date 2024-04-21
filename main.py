from flask import Flask, request, jsonify

from utils import checkForInput
app = Flask(__name__)
    
@app.route("/calculator/addition")
def addition():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    hasError = checkForInput(num1=num1, num2=num2)
    if(hasError):
        return hasError, 500

    response = {
        "result": int(num1) + int(num2)
    }

    return jsonify(response), 200

@app.route("/calculator/subtraction")
def subtraction():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    hasError = checkForInput(num1=num1, num2=num2)
    if(hasError):
        return hasError, 500

    response = {
        "result": int(num1) - int(num2)
    }

    return jsonify(response), 200

@app.route("/calculator/multiplication")
def multiplication():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    hasError = checkForInput(num1=num1, num2=num2)
    if(hasError):
        return hasError, 500

    response = {
        "result": int(num1) * int(num2)
    }

    return jsonify(response), 200

@app.route("/calculator/division")
def division():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    hasError = checkForInput(num1=num1, num2=num2)
    if(hasError):
        return hasError, 500

    response = {
        "result": int(num1) / int(num2)
    }

    return jsonify(response), 200

@app.route("/calculator/modulus")
def modulus():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    hasError = checkForInput(num1=num1, num2=num2)
    if(hasError):
        return hasError, 500

    response = {
        "result": int(num1) % int(num2)
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)
