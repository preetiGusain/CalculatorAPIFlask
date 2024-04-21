from flask import jsonify

def checkForInput(num1, num2):
    errorResponse = {}
    if(num1 == None):
        errorResponse["message"] = "num1 not present in query"
        return jsonify(errorResponse)
    
    if(num2 == None):
        errorResponse["message"] = "num2 not present in query"
        return jsonify(errorResponse)
    
    if(num1.isdigit() != True):
        errorResponse["message"] = "num1 is not a valid input"
        return jsonify(errorResponse)

    if(num2.isdigit() != True):
        errorResponse["message"] = "num2 is not a valid input"
        return jsonify(errorResponse)
    
    return None