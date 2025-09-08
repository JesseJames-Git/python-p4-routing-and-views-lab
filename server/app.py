#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:name>")
def print_string(name):
    print(name)
    return name

@app.route("/count/<int:number>")
def count(number):
    each_number = "\n".join(str(num) for num in range(number)) + "\n"
    return f"{each_number}"

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num1 == 0 or num2 == 0:
            return "Cannot divide by zero"
        else:
            result = num1 / num2
    
    elif operation == "%":
        result = num1 % num2
    else:
        return "Ensure you input +,-,*,'%' or div as a valid operation sign"
    return str(result)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
