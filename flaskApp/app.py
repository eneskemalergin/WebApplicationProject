from flask import Flask, render_template, json, request, redirect, session, jsonify, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.wsgi import LimitedStream
import os
import uuid


app = Flask(__name__)
app.secret_key = "secret"


# Main Page:
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignIn')
def showSignIn():
    return render_template('signIn.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signUp.html')
