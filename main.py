import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import create_app
from app.form import LoginForm, TodoForm, DeleteTask, UpdateTask
from app.fix import getUsers, getUser, getTasksByUserId, todo_put, delete_task, update_task

app = create_app()

todos = ['Comprar café', 'Solitud de compra', 'Entregar video a productor']




@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    # response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTask()
    update_form = UpdateTask()

    context = {
        'user_ip': user_ip,
        'todos': getTasksByUserId(username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'udpate_form': update_form,
    }

    if todo_form.validate_on_submit():
        todo_put(username=username, description=todo_form.description.data)

        flash("Tu tarea se creo con exito !!")
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    delete_task(todo_id)

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:is_done>', methods=['POST'])
def update(todo_id, is_done):
    update_task(todo_id, is_done)
    return redirect(url_for('hello'))

@app.route('/users')
def users():
    users = getUsers()
    tasks = getTasksByUserId('jrsaavedra')
    # print(tasks)
    user = getUser('jrsaavedra')
    if user is not None:
        a = user.check_password("12a3Admin")
        print(a)
        print("here .... user ...")
    print(user)

    return jsonify(users)