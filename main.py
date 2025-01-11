from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///main.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
class todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    date_created=db.Column(db.Date,default=datetime.datetime.now)
    
@app.route('/')
#.\env\Scripts\activate.ps1
def hello_world():
    return render_template("index.html")
if __name__ == '__main__':
    app.run(debug=True)
