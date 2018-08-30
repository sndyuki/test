#認証処理で必要なモジュール
from __future__ import print_function
from flask_script import Manager

#flaskrを起動
from flaskr import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
