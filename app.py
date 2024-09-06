from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(20))

@app.route("/",methods=['GET','POST'])

def index():
    username=None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        new_user = User(username = username, password=password)
        db.session.add(new_user)
        db.session.commit()
    return render_template("index.html",username=username)


if __name__ =="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
