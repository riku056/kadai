from flask import Flask, render_template,request
import calc

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/circle")
def circle():
    return render_template("circle.html")

@app.route("/calc_circle")
def calc_circle():
    r = int(request.args.get("r"))
    result = calc.calc_circle(r)
    return render_template("result_value.html",result=result)


if __name__ == "__main__":
    app.run(debug=True)