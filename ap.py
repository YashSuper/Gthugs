from flask import Flask,render_template,request
app = Flask(__name__)
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
status=0
@app.route("/")
def index():
    return render_template ("index.html")
@app.route("/send",methods=['GET','POST'])
def send():
    status=0
    ph="N/a"
    em="N/a"
    Nm=request.form.get('Name')
    ph=request.form.get('phone')
    em=request.form.get('Email')
    ln=request.form.get('Lastname')
    Mess=request.form.get('Message')
    msg = Message("From "+em, sender = '', recipients = ['yashbharadwajsuper@gmail.com'])
    msg.body = f"This Message is sent by {Nm}({ph},{em}),\n \t {Mess}"
    mail.send(msg)
    status=1
    return render_template("index.html",status=status)
