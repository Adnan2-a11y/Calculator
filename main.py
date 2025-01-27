from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = num1 / num2
            elif operation == "power":
                result = num1**num2
            elif operation == "sqrt":
                if num1 < 0:
                  error = "Cannot calculate square root of a negative number!"
                else:
                    result = math.sqrt(num1)
            elif operation == "modulo":
              if num2 == 0:
                error = "Cannot modulo by zero!"
              else:
                result = num1 % num2
        except ValueError:
            error = "Invalid input! Please enter numbers."
        except Exception as e:
            error = f"An unexpected error occured:{e}"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)