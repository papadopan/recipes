from app import ma
from models.user import UserModel

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("id","_password", "validated")