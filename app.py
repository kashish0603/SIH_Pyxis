from flask import Flask,render_template,request,redirect,session,url_for,send_from_directory,abort,make_response
import re
from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'VIT_Vellore21'
app.config['MYSQL_DB'] = 'Pyxis_team'
  
  
mysql = MySQL(app)
  
  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index1.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email'] 
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM User WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO User VALUES (NULL, % s, % s, % s)', (username, password, email ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route("/index1")
def index1():
    if 'loggedin' in session:
        return render_template('index1.html')
    return redirect(url_for('login'))

# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(render_template("404.html"), 404)

@app.route('/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))

@app.route("/aadhar")
def aadhar():
    if 'loggedin' in session:
        return render_template('aadhar.html')
    
@app.route("/signin")
def signin():
    if 'loggedin' in session:
        return render_template('index1.html')

@app.route("/popup")
def popup():
    if 'loggedin' in session:
        return render_template('popup.html')


# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
# app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png','.jpeg', '.tif']
# app.config['UPLOAD_PATH'] = 'uploads'

# @app.route('/biometric')
# def biometric():
#     files = os.listdir(app.config['UPLOAD_PATH'])
#     return render_template('biometric.html')

# @app.route('/biometricsubmit', methods=['POST'])
# def upload_files():
#     uploaded_file = request.files['file']
#     filename = secure_filename(uploaded_file.filename)
#     if filename != '':
#         file_ext = os.path.splitext(filename)[1]
#         if file_ext not in app.config['UPLOAD_EXTENSIONS']:
#             abort(400)
#         uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#     return redirect(url_for('biometric'))
    
# @app.route('/uploads/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)

@app.route("/biometric")
def biometric():
    if 'loggedin' in session:
        return render_template('biometric.html')

@app.route("/cctv")
def cctv():
    if 'loggedin' in session:
        return render_template('cctv.html')

if __name__ == '__main__':
    app.run(debug=True, host ="localhost", port = int("5000"))    