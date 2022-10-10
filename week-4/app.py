from flask import Flask, redirect, url_for,render_template, request, session
app = Flask(
    __name__,
    static_folder = "static",
    static_url_path = "/"
)
app.secret_key = "secretKey"
@app.route("/", methods=['POST', 'GET'])
def homepage():
    if request.method =="POST":
        if request.form["account"] == "test" and request.form["password"] == "test":
            return redirect(url_for("login"))
        elif request.form["account"] == "" or request.form["password"] == "":
            return redirect(url_for("error", message="請輸入帳號、密碼"))
        else:
            return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))
    else:
        return render_template("homepage.html")

@app.route("/login", methods=['GET'])
def login():
    session["state"] = "已登入"
    return redirect(url_for("member"))

@app.route("/signout")
def signout():
    session["state"] = "未登入"
    return redirect(url_for("homepage"))

@app.route("/member")
def member():
    if session["state"] != "已登入":
        return redirect(url_for("homepage"))
    else:
        return render_template("member.html")
    
@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", alert=message) # 將message代入alert並傳至前端網頁內容

@app.route("/square/<number>", methods=['POST', 'GET'])
def square(number):
    return render_template("calculate.html", result = int(number) ** 2)

if __name__ == "__main__":
    app.run(port="3000", debug=True)
