from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os

dbconfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "13579jacky",
    "database" : "website"
}

connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name = "my_pool",
    pool_size = 5,
    pool_reset_session = True,
    **dbconfig
)

app = Flask(
    __name__,
    static_folder = "static", 
    static_url_path = "/" 
)
app.secret_key = os.urandom(20)

@app.route("/", methods=['POST', 'GET'])
def homepage():
    return render_template("homepage.html")

@app.route("/signup", methods=['POST','GET'])
def signup():
    account = request.form["account"]
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        check_sql = "SELECT * FROM member WHERE username = %s"
        check_val = account
        cursor.execute(check_sql,check_val)
        user = cursor.fetchone()
        connection_object.commit()
        if user == None:
            name = request.form["name"]
            account = request.form["account"]
            password = request.form["password"]
            signup_sql = "INSERT INTO member (name, username, password) VALUES (%s,%s,%s)"
            signup_val = (name, account, password)
            cursor.execute(signup_sql, signup_val)
            connection_object.commit()
            return redirect(url_for("homepage"))
        else:
            return redirect(url_for("error", message = "帳號已經被註冊"))
    except:
        return "Unexpected Error", 500
    finally:
        cursor.close()
        connection_object.close()

@app.route("/signin",methods=['GET','POST'])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        signin_sql = "SELECT * FROM member WHERE username = %s and password = %s"
        signin_val = (account,password)
        cursor.execute(signin_sql,signin_val)
        user = cursor.fetchone()
        connection_object.commit()
        if user != None:
            session["id"] = user[0]
            session["name"] = user[1]
            session["state"] = "已登入"
            return redirect(url_for("member"))
        else:
            return redirect(url_for("error", message="帳號或密碼輸入錯誤"))
    except:
        return "Unexpected Error", 500
    finally:
        cursor.close()
        connection_object.close()
        
        

@app.route("/member", methods=['GET', 'POST'])
def member():
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        session["state"] == "已登入"
        cursor.execute("SELECT member.name, message.content, message.time FROM message INNER JOIN member ON member.id = message.member_id ORDER BY time")
        info = cursor.fetchall()
        return render_template("member.html", name=session["name"],content = info)
    except:
        return redirect(url_for("homepage"))
    finally:
        cursor.close()
        connection_object.close()
        
@app.route("/api/member", methods=['GET'])
def searching_name():
    username = request.args.get("username", "")
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        sql = "SELECT * FROM member WHERE username = %s"
        val = (username, )
        cursor.execute(sql, val)
        user = cursor.fetchone()
        connection_object.commit()
        if user != None:
            return {
                "data":{
                "id":user[0],
                "name":user[1],
                "username":user[2]
                }
            }
        else:
            return {
                "data":None
            }
    except:
        return "Unexpected Error", 500
    finally:
        cursor.close()
        connection_object.close()

@app.route("/api/member", methods = ['PATCH'])
def change_info():
    req = request.get_json()
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        sql  = "UPDATE member SET name = %s WHERE id = %s"
        val = (req["name"], session["id"])
        cursor.execute(sql, val)
        connection_object.commit()
        session["name"]=req["name"]
        return {"ok":True}
    except:
        return {"error":True}
    finally:
        cursor.close()
        connection_object.close()
    

@app.route("/message",methods = ['POST'])
def message():
    content = request.form["content"]
    try:
        connection_object = connection_pool.get_connection()
        cursor =  connection_object.cursor()
        message_sql = "INSERT INTO message (member_id, content) VALUES (%s,%s)"
        message_val = (session['id'],content)
        cursor.execute(message_sql, message_val)
        connection_object.commit()
        return redirect(url_for("member"))
    finally:
        cursor.close()
        connection_object.close()
    

@app.route("/error")
def error():
    message = request.args.get("message","")
    return render_template("error.html", alert=message) 

@app.route("/signout")
def signout():
    session.clear() 
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(port="3000", debug=True)
