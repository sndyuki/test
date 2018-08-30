#ここを基準に、相対パスでimportできるようになる
#また、__init__.pyで生成されたインスタンスも他のpythonスクリプトでimportできる。
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#appインスタンス生成
app = Flask(__name__)

#Flaskのconfigが 設定ファイルを読み込む処理
#from_envvar:環境変数から
#from_object:pythonオブジェクトから
#from_pyfile:pythonファイルから
app.config.from_object('flaskr.config')

#dbインスタンス生成
db = SQLAlchemy(app)

import flaskr.views