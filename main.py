from flask import Flask, request, redirect
import os

app = Flask(__name__)

# データの保存先 --- (*1)
DATAFILE = './board-data.txt'


# ルートにアクセスしたとき --- (*2)
@app.route('/')
def index():
    msg = 'まだ書込はありません。'
    # 保存データを読む --- (*3)
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:  # DATAFILEを開く&読み込む
            msg = f.read()
    # メッセージボードと投稿フォーム --- (*4)
    return """
    <html><body>
    <h1>メッセージボード</h1>
    <div style="background-color:yellow;padding:3em;">{0}</div>
    <h3>ボードの内容を更新:</h3>
    <form action="/write" method="POST">
        <textarea name="msg"
         rows="6" cols="60"></textarea><br/>
        <input type="submit" value="書込">
    </form>
    </body></html>
    """.format(msg)


# POSTメソッドで/writeにアクセスしたとき --- (*5)
@app.route('/write', methods=['POST'])
def write():
    # データファイルにメッセージを保存 --- (*6)
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:  # DATAFILEを開く&書き込む
            f.write(msg)
    # ルートページにリダイレクト --- (*7)
    return redirect('/')
    # 再接続。このあとindexメソッドでDATAFILE読み込まれるから
    # 最新の状態のDATAFILEが読み込まれるってことやな


'''
第9回のファイル操作のやつmemo

with open('a.txt', 'rt') as f:    # 読み取り用 a.txt を f として開く
    a_value = f.read()            # 読み取り内容 f を a_value に格納

with open('a.txt', 'wt') as f:    # 書き込み用 a.txt を f として開く
    f.write("new_str")            # "new_str" を f に書き込む

'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
