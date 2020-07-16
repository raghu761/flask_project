from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hi():
	return render_template("index.html")


@app.route('/about')
def hello():
	name="raghunath"
	return render_template("about.html",getname=name)


app.run()

