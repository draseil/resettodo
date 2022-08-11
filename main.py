from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '103d485a680c3850328fdcdecc8c32b752357d80b19d303d'

messages = []

@app.route('/', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		todo_list = request.form['todo-list']

		if not todo_list:
			flash('please fill out the todo list')
		else:
			for line in todo_list.splitlines():
				messages.append(line)
			return redirect(url_for('main'))
	
	return render_template('index.html')

@app.route('/generated', methods=('GET', 'POST'))
def main():
	return render_template('generated.html', len = len(messages), messages = messages)
