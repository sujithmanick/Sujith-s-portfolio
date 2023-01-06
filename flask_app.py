from flask import Flask,render_template,request,session
import smtplib
import json
from email.mime.text import MIMEText
from datetime import date
import pickle
app = Flask(__name__)
app.secret_key = "@78#45SjApp"
def send_email(name,email,message,phone):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        sender_address = 'server.mailbridge@gmail.com'
        sender_pass = ''
        sender = 'contactquickes@gmail.com'
        targets = 'sujithmanick@gmail.com'
        msg = MIMEText('Name : {}\nMailid : {}\nMessage : {}\nPhone : {}'.format(name,email,message,phone))
        msg['Subject'] = 'User Message'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(sender_address,sender_pass )
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

def send_email_user(email):
    try:
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        sender_address = 'server.mailbridge@gmail.com'
        sender_pass = ''
        sender = 'contactquickes@gmail.com'
        targets = email
        msg = MIMEText('Thank you for contacting i will get back to you soon 😊!')
        msg['Subject'] = 'Contact you soon'
        msg['From'] = sender
        msg['To'] = targets

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(sender_address,sender_pass )
        server.sendmail(sender,targets,msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

@app.route("/",methods=['GET','POST'] )
def home():
    if request.method == 'GET':
        return render_template("index.html",next_link="#Contact")
    elif request.method == 'POST':
        session['Name'] = request.form['name']
        session['Email'] = request.form['mail']
        session['phone'] = request.form['phone']
        session['message'] = request.form['message']
        send_email(session['Name'],session['Email'],session['message'],session['phone'])
        send_email_user(session['Email'])
        return render_template("profile.html")








if __name__ == '__main__':
    app.run()
