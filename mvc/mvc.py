from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# モデル: データを管理する
class UserModel:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users

# ビュー: ユーザーインターフェースを表示
@app.route('/')
def index():
    users = user_model.get_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    user_name = request.form['name']
    user_model.add_user(user_name)
    return redirect(url_for('index'))

# コントローラー
user_model = UserModel()

if __name__ == '__main__':
    app.run(debug=True)
