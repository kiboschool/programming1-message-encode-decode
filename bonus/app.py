from flask import Flask, render_template, request, url_for, flash, redirect
import os

# small hack to import from parent; not needed if app.py is in the same folder
# as main.py
import sys
sys.path.append('..')
from main import encode_base64, decode_base64, encode_morse, decode_morse, encrypt, decrypt

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    message = request.form.get('message')
    operation = request.form.get('operation')
    mode = request.form.get('mode')
    output=""

    if not message:
        flash('Message is required!')
    if not operation:
        flash('Operation is required!')
    if not mode:
        flash('Mode is required!')
    else:
        if operation == "encode":
            if mode == "base64":
                output = encode_base64(message)
            elif mode == "morse":
                output = encode_morse(message)
            elif mode == "encrypt":
                output = encrypt(message)
            else:
                flash("Unsupported encoding mode!")
        elif operation == "decode":
            if mode == "base64":
                output = decode_base64(message)
            elif mode == "morse":
                output = decode_morse(message)
            elif mode == "encrypt":
                output = decrypt(message)
            else:
                flash("Unsupported decoding mode!")
        else:
            flash('Operation not supported!')

    return render_template('index.html', message=message,
                           output=output, mode=mode)

