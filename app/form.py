from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """ clase de login. """
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class RegisterForm(FlaskForm):
    """ clase de register. """
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    email = StringField("Correo electronico", validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class TodoForm(FlaskForm):
    """ Clase para formas. """
    description = StringField("Descripción", validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteTask(FlaskForm):
    """ Clase Form para eliminar tareas. """
    submit = SubmitField('Eliminar')

class UpdateTask(FlaskForm):
    """ Clase Form para actualizar una tarea. """
    submit = SubmitField('Actualizar')