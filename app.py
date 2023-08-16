from flask import Flask, render_template, request, redirect, url_for
from send_email import SendEmail
import os

app = Flask(__name__)
app.secret_key = os.getenv('CSRF-KEY')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sender_name = request.form['name']
        sender_phone = request.form['phone']
        sender_email = request.form['email']
        message = request.form['message']
        send_email = SendEmail(name=sender_name, email=sender_email, phone=sender_phone, message=message)
        return render_template('send_successful.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False)
