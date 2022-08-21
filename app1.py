from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask import session as login_session
from flask import make_response
import os
from face_verification.new import facerecog

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('select'))
    return render_template('login.html')


@app.route('/select', methods=['GET', 'POST'])
def select():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('index1.html')

@app.route('/biometric', methods=['GET', 'POST'])
def biometric():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('biometric.html')

@app.route('/cctv', methods=['GET', 'POST'])
def cctv():
    if request.method == 'POST':
        img = request.files['image']
        img.save(os.path.join('static', img.filename))

        # If img.jpg already exists, delete it
        if os.path.exists('static/img.jpg'):
            os.remove('static/img.jpg')
        # Rename the image to image.jpg
        os.rename(os.path.join('static', img.filename), os.path.join('static', 'img.jpg'))
        
        return redirect(url_for('searching'))






        return redirect(url_for('index'))
    return render_template('cctv.html')

@app.route('/searching', methods=['GET', 'POST'])
def searching():
    if request.method == 'POST':
        if request.form['realtime']:
            facerecog()
    return render_template('searching.html')

@app.route('/aadhar', methods=['GET', 'POST'])
def aadhar():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('aadhar.html')



if __name__ == '__main__':
    app.run(debug=True)

