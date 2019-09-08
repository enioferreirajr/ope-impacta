from app import app
from flask import render_template, request, redirect, url_for, session


@app.route('/home', methods=['POST', 'GET'])
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        return render_template('home.html',
                               username=session['username'],
                               loggedin=session['loggedin'],
                               breadcrumb='breadcrumb',
                               page_header='page_header')
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
