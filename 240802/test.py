from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

api_key = "VF.DM.66ac8d5992ccb0c68bfaa36b.Kc6TJlWdkkjj855z"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    transcripts = get_transcripts(current_user.id)
    return render_template('dashboard.html', transcripts=transcripts)

def get_transcripts(user_id):
    url = f'https://general-runtime.voiceflow.com/state/user/{user_id}/transcripts'
    headers = {
        'Authorization': api_key,
        'versionID': 'production'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
