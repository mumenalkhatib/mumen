from flask import Flask, render_template, request
import random
import dataset 

db = dataset.connect("postgres://sqtgiyiuserjtd:a2e990bf3dc72c62c59e389afbbd31ede6690fc0a67ac79ca4de5b605d75a70f@ec2-23-21-96-159.compute-1.amazonaws.com:5432/d3d2m0i1jjdgd")
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

@app.route('/form.html' , methods=["POST"])
def form():
	form =request.form
	name =form["name"]
	email =form["email"]
	comment =form["comment"]

	contactsTable = db["contacs"]
	entry = {"name":name , "email":email , "comment":comment}
	contactsTable.insert(entry)
	print list (contactsTable.all())
	return render_template ("form.html" , name=name , email=email , comment=comment )


@app.route('/showall.html')
def showall():
	contactsTable = db["contacs"]
	allcontacs = list (contactsTable.all())
	return render_template ("showall.html" , contacts = allcontacs)


if __name__ == "__main__":
	app.run()