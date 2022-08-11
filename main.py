from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '103d485a680c3850328fdcdecc8c32b752357d80b19d303d'

checkboxes = []

@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'GET':
        todo_list = request.args.get('todo-list')
        color = request.args.get('color')

        if not todo_list:
            flash('please fill out the todo list')
        else:
            checkboxes.clear();
            for line in todo_list.splitlines():
                checkboxes.append(line)
            return render_template('generated.html', len = len(checkboxes), checkboxes = checkboxes, color = color)
    
    return render_template('index.html')

@app.route('/generated', methods=('GET', 'POST'))
def main():
    return render_template('generated.html', len = len(checkboxes), checkboxes = checkboxes)
