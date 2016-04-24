from flask import Flask, render_template
import jinja2

app = Flask(__name__)
app.jinja_loader = jinja2.FileSystemLoader('./template')


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

@app.route('/showGallery')
def showGallery():
    return render_template('gallery.html')

@app.route('/showCourse')
def showCourse():
    return render_template('courses.html')


if __name__=="__main__":
    app.run()
