from .database import *
from .serializer import *

def createDB():
    """ Método de creación de la base de datos. """
    db.drop_all()
    db.create_all()

def insertUsersDB():
    """ Método para crear registros de usuarios. """
    createDB()

    # creación de usuarios
    admin = User(username='jrsaavedra', email='admin@example.com', is_admin=True)
    admin.set_password("123Admin")

    guest = User(username='invitado', email='guest@example.com')
    guest.set_password("123Invitado")

    t1 = Task(task='Hacer oficio')
    t2 = Task(task='Comprar café')
    t3 = Task(task='Solitud de compra')
    t4 = Task(task='Entregar video a productor')
    admin.tasks.append(t1)
    admin.tasks.append(t2)
    admin.tasks.append(t3)
    admin.tasks.append(t4)
    guest.tasks.append(t2)
    guest.tasks.append(t3)
    guest.tasks.append(t4)
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()


def getUsers():
    """ Método de listado de usuarios. """
    insertUsersDB()
    # return User.query.all()
    user_schema = UserSchema()
    data = User.query.all()

    users = [user_schema.dump(u) for u in data]
    return users 

def getTasksByUserId(username):
    """ Método para ob(tener el listado de las tareas. """
    task_schema = TaskSchema()
    user_schema = UserSchema()
    data = Task.query.filter(Task.user.has(username=username))
    
    tasks = []
    for t in data:
        user = user_schema.dump(t.user)
        task = task_schema.dump(t)
        task['user'] = user

        tasks.append(task)

    return tasks

def getUser(username):
    """ Obtener un usuario a partir del nombre de usuario. """
    
    return User.query.filter_by(username=username).first()


def user_put(user_data):
    """ Método para crear un nuevo usuario en la base de datos. """
    user = User(username=user_data.username, email=user_data.username + "@example.com")
    user.set_password(user_data.password)

    db.session.add(user)
    db.session.commit()
    user_data.password = user.password
    return user_data

def todo_put(username, description):
    """ Método para crear una nueva tarea. """
    user = getUser(username)
    task = Task(task=description, user=user)
    db.session.add(task)
    db.session.commit()

def delete_task(task_id):
    """ Método para elminar una tarea. """
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

def update_task(task_id, is_done):
    task_done = not bool(is_done)
    task = Task.query.get(task_id)
    task.is_done = task_done
    
    db.session.commit()
