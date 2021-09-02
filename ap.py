# splite3をimportする
import sqlite3
from sqlite3.dbapi2 import TimestampFromTicks
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)
import datetime

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabaco'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login' , methods = ["POST"])
def login_post():
    name = request.form.get("member_name")
    password = request.form.get("member_pass")
    connect = sqlite3.connect('sunabaco.db')
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM user_tbl WHERE user_name= ? AND user_pass = ?",(name,password))
    user_id = cursor.fetchone()
    if user_id is None:
        return render_template('login.html')
    else:
        session["user_id"] = user_id
        return redirect('/contents1')

@app.route('/add1')
def add_get():
    return render_template('htmladd.html')

@app.route('/add1', methods = ["POST"])
def add_post():
    task =request.form.get('cnt_keyword')
    task1 = request.form.get('cnt_text')
    task2 = request.form.get('cnt_url')
    connect = sqlite3.connect('sunabaco.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO cnt_tbl VALUES (null,null,1,77,?,?,?,null)", (task,task1,task2,) )
    print(task1)
    connect.commit()
    connect.close()
    return redirect('/contents1')

@app.route('/contents1')
def contents1():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT id, yogo FROM yogo_tbl ")
        task = cursor.fetchall()
    # taskのままだと使いづらいので
    # リストの中にオブジェクトのある形に挿入
        task_listType = []
        for row in task:
            task_listType.append({"id":row[0],"yogo":row[1]})
        connect.close()
        return render_template('contents1.html', html_task = task_listType, user_name = user_name)
    else:
        return redirect('/login')

@app.route('/html4')
def html():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        task = cursor.fetchall()
        task_listType = []
        for row in task:
            task_listType.append({"id":row[0],"top_crt":row[1]})
        connect.close()
        return render_template('html.html',html_task = task_listType,user_id = user_id,user_name = user_name)

@app.route('/html2/<int:top_crt_id>')
def html2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 1 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('html2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)
    else:
        return redirect('/login')

@app.route('/css')
def css():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('css.html',user_id = user_id)

@app.route('/css2/<int:top_crt_id>')
def css2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 2 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('css2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)
    else:
        return redirect('/login')

@app.route('/js')
def js():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('js.html',user_id = user_id)

@app.route('/js2/<int:top_crt_id>')
def js2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 3 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('js2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)

@app.route('/jquery')
def jquery():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('jquery.html',user_id = user_id)
        

@app.route('/jquery2/<int:top_crt_id>')
def jquery2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 4 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('jquery2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)

@app.route('/github')
def github():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('github.html',user_id = user_id)

@app.route('/github2/<int:top_crt_id>')
def github2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 5 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('github2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)


@app.route('/python')
def python():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('python.html',user_id = user_id)

@app.route('/python2/<int:top_crt_id>')
def python2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 6 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('python2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)

@app.route('/flask')
def flask():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('flask.html',user_id = user_id)

@app.route('/flask2/<int:top_crt_id>')
def flask2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 7 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('flask2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name) 
    

@app.route('/other')
def other():
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        return render_template('other.html',user_id = user_id)

@app.route('/other2/<int:top_crt_id>')
def other2(top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword, cnt_text, cnt_url  FROM cnt_tbl WHERE yogo_id = 8 and top_crt_id = ?" , (top_crt_id,))
        cnt_keyword = cursor.fetchall()
        cnt_keyword_listType = []
        for row in cnt_keyword:
            cnt_keyword_listType.append({"cnt_keyword":row[0],"cnt_text":row[1],"cnt_url":row[2]})
        print(cnt_keyword)
        print(cnt_keyword_listType)
        connect.close()
        return render_template('other2.html',cnt_keyword = cnt_keyword_listType, user_name = user_name)


@app.route('/contents3/<int:top_crt_id>')
def contents3(yogo_id,top_crt_id):
    if "user_id" in session:
        user_id = session["user_id"][0]
        connect = sqlite3.connect('sunabaco.db')
        cursor = connect.cursor()
        cursor.execute("SELECT user_name FROM user_tbl WHERE id = ?", (user_id,) )
        user_name = cursor.fetchone()[0]
        cursor.execute("SELECT cnt_keyword,cnt_text,cnt_url FROM cnt_tbl WHERE yogo_id = ? and top_crt_id = ?", (yogo_id,top_crt_id))
        cnt_keyword = cursor.fetchone()
        print(cnt_keyword)
        connect.close()
        if cnt_keyword is None:
            return "指定したタスクはないよ"
        else:
            cnt_keyword = cnt_keyword[0]
            item = {"yogo_id":yogo_id,"top_crt_id":top_crt_id,"cnt_keyword":cnt_keyword}
            return render_template('contents3.html',html_item = item,user_name = user_name)
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('user_id' , None)
    return redirect('/login')


@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "404だよ！！見つからないよ！！！"



# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)