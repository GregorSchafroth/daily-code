from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

api_key = os.getenv('API_KEY')
project_id = os.getenv('PROJECT_ID')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager = LoginManager()
login_manager.init_app(app)

env_username = os.getenv('USERNAME')
env_password = os.getenv('PASSWORD')

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.username = username
        
@login_manager.user_loader
def load_user(user_id):
    if user_id == env_username:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == env_username and password == env_password:
            user = User(username)
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
    all_transcripts = get_all_transcripts()
    grouped_transcripts = parse_transcripts(all_transcripts)
    return render_template('dashboard.html', transcripts=grouped_transcripts)

def get_all_transcripts():
    url = f"https://api.voiceflow.com/v2/transcripts/{project_id}"
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching transcripts:", response.text)
        return []

def get_transcript_details(transcript_id):
    url = f"https://api.voiceflow.com/v2/transcripts/{project_id}/{transcript_id}"
    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching transcript details for {transcript_id}: {response.text}")
        return []
  
def parse_transcripts(all_transcripts):
    grouped_transcripts = {}
    for transcript_metadata in all_transcripts:
        transcript_id = transcript_metadata['_id']
        transcript_details = get_transcript_details(transcript_id)
        
        grouped_transcripts[transcript_id] = {
            'session_id': transcript_metadata.get('sessionID', 'Unknown Session'),
            'created_at': transcript_metadata.get('createdAt', 'Unknown Date'),
            'messages': []
        }
        
        for turn in transcript_details:
            if turn['type'] == 'text':
                message = turn.get('payload', {}).get('payload', {}).get('message', 'No message found')
                grouped_transcripts[transcript_id]['messages'].append({
                    'turn_id': turn.get('turnID'),
                    'message': f"AI: {message}",
                    'start_time': turn.get('startTime')
                })
            elif turn['type'] == 'request' and turn.get('payload', {}).get('type') == 'intent':
                query = turn.get('payload', {}).get('payload', {}).get('query', 'No query found')
                grouped_transcripts[transcript_id]['messages'].append({
                    'turn_id': turn.get('turnID'),
                    'message': f"Human: {query}",
                    'start_time': turn.get('startTime')
                })
    
    return grouped_transcripts

if __name__ == '__main__':
    app.run()