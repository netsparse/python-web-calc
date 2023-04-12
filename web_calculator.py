from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    operation = request.form["operation"]
    x = float(request.form["x"])
    y = float(request.form["y"])
    result = None

    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        if y != 0:
            result = x / y
        else:
            result = "Error: Division by zero"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

