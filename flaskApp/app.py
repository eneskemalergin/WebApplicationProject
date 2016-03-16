from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import os
import uuid


app = Flask(__name__)

# Main Page:
@app.route('/')
def main():
    return render_template('index.html')

#signIn Page
@app.route('/showSignIn')
def showSignIn():
    return render_template('signIn.html')

#signUp Page
@app.route('/showSignUp')
def showSignUp():
    return render_template('signUp.html')

@app.route('/gallery')
def gallery():
    return render_template('#') # Add when you have it here...

@app.route('/showCourse')
def showCourse():
    return render_template('#') # Add when you have it here...

if __name__=="__main__":
    app.run()
