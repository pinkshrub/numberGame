from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'RobBoss'

@app.route('/')
def index():
	return render_template("index.html")
@app.route('/results', methods=['POST'])
def create():
	namer = request.form['name']
	localer = request.form['locale']
	lingor = request.form['lingo']
	commentr = request.form['comment']

	## validations yay ##
	if len(namer) < 1:
		flash('Yo dawg, gotta have a name! AMIRITE?')
		return redirect('/')
	elif len(commentr) > 120:
		flash('more register less comment young one')
		return redirect('/')
	else:
		flash('thanks for registering broski!')

	return render_template('result.html', named=namer, locale=localer, lingo=lingor, comment=commentr)



app.run(debug=True)