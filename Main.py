from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def Homepage():
    return render_template("index.html")




@app.route("/mycalc", methods=["POST","GET"])
def cal():
    a = int(request.form.get("num1"))
    b = int(request.form.get("num2"))
    c = request.form.get("op")

    if c=="+":
        d = a+b
    elif c=="-":
        d = a-b
    elif c == "*":
        d = a*b
    elif c == "/":
        d = a/b
    else:
        d="Invalid Operator"
    

    return render_template("index.html",value1 = d)



if __name__ ==  "__main__":
    app.run(debug=True)

