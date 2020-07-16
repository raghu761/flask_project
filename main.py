from flask import Flask,render_template ,request
from flask_sqlalchemy import SQLAlchemy
#import MYSQL
import json

with open('config.json') as c:
	params=json.load(c)["params"]

local_server=True

app=Flask(__name__)
if local_server:
	app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
	app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db=SQLAlchemy(app)

class Contacts(db.Model):	
	#sno name email phone_num mes date
	sno = db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(120),nullable=False)
	email = db.Column(db.String(120),nullable=False)
	phone_num = db.Column(db.String(50),nullable=False)
	mes= db.Column(db.String(50),nullable=False)
	date = db.Column(db.String(12),nullable=True)


@app.route('/')
def home():		

	return render_template("index.html",params=params)

@app.route('/about')
def about():
	return render_template("about.html",params=params)

@app.route('/contact',methods=['GET','POST'])
def contact():
	if request.method=='POST':
		name=request.form.get('name')
		email=request.form.get('email')
		phone=request.form.get('phone')
		message=request.form.get('message')

		entry=Contacts(name=name,phone_num=phone,email=email,mes=message)
		db.session.add(entry)
		db.session.commit()



	return render_template("contact.html",params=params)


@app.route('/post')
def sample_post():
	return render_template("post.html",params=params)


app.run(debug=True)
