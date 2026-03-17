from flask import Flask, render_template, request

app = Flask(__name__)

def get_outfit(gender, occasion, color):
    if gender == "Male":
        if occasion == "Casual":
            return f"{color} T-shirt with jeans"
        elif occasion == "Formal":
            return f"{color} shirt with black trousers"
        else:
            return f"{color} blazer with stylish pants"
    else:
        if occasion == "Casual":
            return f"{color} top with jeans"
        elif occasion == "Formal":
            return f"{color} saree or formal dress"
        else:
            return f"{color} party gown"

@app.route("/", methods=["GET", "POST"])
def index():
    outfit = ""
    if request.method == "POST":
        gender = request.form["gender"]
        occasion = request.form["occasion"]
        color = request.form["color"]
        outfit = get_outfit(gender, occasion, color)
    return render_template("index.html", outfit=outfit)

if __name__ == "__main__":
    app.run(debug=True)