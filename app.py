from flask import Flask, render_template,request
import calc
import kadaiA

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

@app.route("/keisan")
def keisan():
    return render_template("kadai_keisan.html")

@app.route("/keisan_result")
def keisan_result():
    kyuu1 = int(request.args.get("a"))
    kyuu2 = int(request.args.get("b"))
    result = kyuu1 * kyuu2
    #result = kadaiA.keisan_result(kyuu)
    return render_template("keisan_result.html",result=result)


if __name__ == "__main__":
    app.run(debug=True)