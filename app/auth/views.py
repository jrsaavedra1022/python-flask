from flask import render_template, session, flash, redirect, url_for 
from flask_login import login_user, login_required, logout_user
from . import auth
from app.form import LoginForm, RegisterForm
from app.fix import getUser, user_put
from app.models import UserModel, UserData

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user = getUser(username)

        if user is not None:
            if user.check_password(password):
                user_data = UserData(username, user.password)
                user_model = UserModel(user_data)

                login_user(user_model)

                flash('Bienvenido de nuevo')
                redirect(url_for('hello'))
            else:
                flash('Credenciales incorrectas !!')
        else:
            flash('Credenciales incorrectas !!')
        

        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = RegisterForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        # no validamos el email

        user = getUser(username)
        if user is None:
            user_data = UserData(username, password)
            newUser = user_put(user_data)

            user =  UserModel(newUser)

            login_user(user)

            flash('Bienvenido !!')

            return redirect(url_for('hello'))
        
        else:
            flash("El usuario ya existe !!")




    return render_template('signup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))