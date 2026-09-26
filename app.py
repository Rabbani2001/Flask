from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def multiplication_table():

    if request.method == "POST":
        number = int(request.form["number"])

        result = f"<h2>Table of {number}</h2>"

        for i in range(1, 11):
            result += f"{number} x {i} = {number * i}<br>"

        return result

    return """
        <h2>Multiplication Table</h2>

        <form method="POST">
            <input 
                type="number" 
                name="number" 
                placeholder="Enter a number"
                required
            >

            <button type="submit">
                Generate Table
            </button>
        </form>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)