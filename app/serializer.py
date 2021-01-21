from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .database import *

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: User
        fields = ('id', 'username', 'email', 'password', 'is_admin')
        load_instance = True

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model: Task
        fields = ('id', 'task', 'user_id', 'user', 'is_done')
        include_relationships = True
        load_instance = True

