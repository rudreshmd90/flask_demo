from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']="sarojamma"

#create a form class
class NameForm(FlaskForm):
	name = StringField("what is your NameForm",validators=[DataRequired()])
	submit = SubmitField("Submit")


#@app.route('/')

#def index():
#	return  "<h1> HELLO WORLD! </h1>"

@app.route('/')
def index():
	name="RUDRESH  "
	fav_food=['idli vada','dosa',24,55.5]
	return render_template("index.html",user_name=name,fav_food=fav_food)

 

#localhost:5000/user/RUDRESH passing arguments

@app.route('/user/<name>')

def user(name):
	return  "<h1> HELLO {} </h1>".format(name)

@app.errorhandler(404)

def page_not_found(e):
	return render_template("404.html")
@app.errorhandler(500)

def page_not_found(e):
	return render_template("500.html")

#create a namepage

@app.route('/name',methods=['GET','POST'])
def name():
	name = None
	form = NameForm()

	#validate form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template("name.html",name=name,form=form)

