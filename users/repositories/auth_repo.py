from flask import current_app
from flask_login import login_user
from flask_principal import Identity, identity_changed

from app.bcrypt import bcrypt
from models.user_model import UserModel


class AuthRepository():
    def teacher_login(self, account, password, messages):
        result = None
        user = UserModel.query.filter(UserModel.account == account).first()
        if (account == user.account and bcrypt.check_password_hash(user.password, password)):
            user = UserModel.query.filter(UserModel.id == user.id).first()

            login_user(user)
            identity_changed.send(current_app._get_current_object(),
                                identity=Identity(user.id))
            result = user.serialize()
        else:
            messages.append({
                "account": 'Invalid account or password'
            })

        return result, messages
    
    def student_login(self, account, messages):
        result = None
        try:
            user = UserModel.query.filter(UserModel.account == account).first()
            login_user(user)
            identity_changed.send(current_app._get_current_object(),
                                identity=Identity(user.id))
            result = user.serialize()
        except Exception as err:
            messages.append({
                "account": 'Invalid account or password'
            })

        return result, messages
