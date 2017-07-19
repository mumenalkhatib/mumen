from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def home():
	title = "Home"
	return render_template("home.html" , title=title ,)

@app.route('/home.html')
def home():
	title = "Home"
	return render_template("home.html" , title=title ,)

@app.route('/contact me.html')
def contact_me():
	title = "Contact_me"
	return render_template("contact me.html" , title=title ,)

@app.route('/about me.html')
def about_me():
	title = "About_me"
	return render_template("about me.html" , title=title ,)

@app.route('/hobbies.html')
def hobbies():
	title = "Hobbies"
	return render_template("hobbies.html" , title=title ,)

@app.route('/we code.html')
def we_code():
	title = "We_Code"
	return render_template("we code.html" , title=title ,)

@app.route('/list.html')
def list():
	title = "List"
	List = ["mumen" , "minymoh" , "majd" , "belal" , "amin"]
	display = True 
	return render_template("list.html" , title=title , list=List , display=display)

if __name__ == "__main__":
	app.run()