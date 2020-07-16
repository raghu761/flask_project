from flask import Flask ,render_template ,request
from flask_sqlalchemy import SQLAlchemy
import forms
app=Flask(__name__)
app.config['SECRET_KEY']='hello'
app.config['SQLAlCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/data'
db=SQLAlchemy(app)



class model(db.Model):
	title_name=db.Column(db.String(100),nullable=False)
	





@app.route('/',methods=["GET","POST"])
def home():	
	form=forms.AddTaskForm();
	if form.validate_on_submit:
		print('submit title ',form.title.data)
		title_head=form.title.data

		entry=Model(title_name=title_head)
		db.session.add(entry)
		db.session.commit()

		return render_template("index.html",form=form, value=form.title.data)
	return render_template("index.html",form=form)

app.run(debug=True)

