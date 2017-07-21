from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/')
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

@app.route('/form.html')
def form():
	title = "form"
	return render_template("form.html" , title=title ,)

@app.route('/contactme1.html' , methods=["GET","POST"])
def contact_me1():
	title = "Contact_me"
	if request.method == "GET":
		return render_template("contact me.html" , title=title)
	else: 
		name = request.form["name"]
		email = request.form["email"]
		comment = request.form["comment"]
		return render_template("form.html" , name=name , email=email , comment=comment)




if __name__ == "__main__":
	app.run()