from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '13579jacky',
    database = 'website',
    charset = 'utf8'
) # 與mysql資料庫連接並設定參數

cursor = db.cursor() # 設立鼠標

app = Flask(
    __name__,
    static_folder = "static", #設定靜態檔案資料夾
    static_url_path = "/" #設定靜態檔案路徑
)
app.secret_key = "secretKey"

@app.route("/", methods=['POST', 'GET'])
def homepage():
    return render_template("homepage.html")

@app.route("/signup", methods=['POST','GET'])
def signup():
    account = request.form["account"]
    sql = "SELECT * FROM member WHERE username = %s"
    val = account
    cursor.execute(sql,val)
    user = cursor.fetchone()
    db.commit
    if user == None:
        name = request.form["name"]
        account = request.form["account"]
        password = request.form["password"]
        sql = "INSERT INTO member (name, username, password) VALUES (%s,%s,%s)"
        val = (name, account, password)
        cursor.execute(sql, val)
        db.commit()
        return redirect(url_for("homepage"))
    else:
        return redirect(url_for("error", message = "帳號已經被註冊"))


@app.route("/signin",methods=['GET','POST'])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    sql = "SELECT * FROM member WHERE username = %s and password = %s"
    val = (account,password)
    cursor.execute(sql,val)
    user = cursor.fetchone()
    db.commit
    if user == None: # 確認該帳戶是否存在
        return redirect(url_for("error", message="帳號或密碼輸入錯誤"))
    else:
        session["id"] = user[0]
        session['name'] = user[1]# 由MySQL fetch出來的user資料為tuple型別，需取其列表的第一項，暫時放入session內做提取
        session["state"] = "已登入"
        return redirect(url_for("member"))
        # return redirect(url_for("signin",method = 'POST'))  

@app.route("/member", methods=['GET', 'POST'])
def member():
    if session["state"] != "已登入":
        return redirect(url_for("homepage"))
    else:
        cursor.execute("SELECT member.name, message.content, message.time FROM message INNER JOIN member ON member.id = message.member_id ORDER BY time")
        info = cursor.fetchall()
        return render_template("member.html",name=session['name'],content = info)

@app.route("/message",methods = ['POST'])
def message():
    content = request.form["content"]
    sql = "INSERT INTO message (member_id, content) VALUES (%s,%s)"
    val = (session['id'],content)
    cursor.execute(sql, val)
    db.commit()
    return redirect(url_for("member"))

@app.route("/error")
def error():
    message = request.args.get("message","") # 擷取query string
    return render_template("error.html", alert=message) # 動態反饋到error.html

@app.route("/signout")
def signout():
    session.clear() # 清空 session 資料
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(port="3000", debug=True)
