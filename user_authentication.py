from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'random_secret_key'
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='your_client_id',
    consumer_secret='your_client_secret',
    request_token_url=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/login/authorized')
def authorized():
    response = google.authorized_response()
    session['google_token'] = response['access_token']
    user_info = google.get('userinfo')
    return f'Logged in as: {user_info.data["email"]}'

if __name__ == '__main__':
    app.run(debug=True)
