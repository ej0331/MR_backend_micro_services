import re
from marshmallow import Schema, ValidationError
from models.user_model import UserModel
from models.class_model import ClassModel


class BaseSchema(Schema):
    def user_account_exists(account):
        user = UserModel.query.filter(UserModel.account == account).first()
        if user:
            raise ValidationError('Account already exists')

    def user_account_not_exists(account):
        user = UserModel.query.filter(UserModel.account == account).first()
        if not user:
            raise ValidationError('Account not found')

    def user_name_not_exists(name):
        user = UserModel.query.filter(UserModel.name == name).first()
        if not user:
            raise ValidationError('Name not found')

    def user_id_not_exists(user_id):
        user = UserModel.query.get(user_id)
        if not user:
            raise ValidationError('User not found')

    def class_name_exists(name):
        class_instance = ClassModel.query.filter(
            ClassModel.name == name).first()
        if class_instance:
            raise ValidationError('Name already exists')

    def class_name_not_exists(name):
        class_instance = ClassModel.query.filter(
            ClassModel.name == name).first()
        if not class_instance:
            raise ValidationError('Name not found')

    def class_id_not_exists(class_id):
        class_instance = ClassModel.query.get(class_id)
        if not class_instance:
            raise ValidationError('Class not found')

    def class_id_list_not_exists(class_id_list):
        if not re.match(r'^[\d,]+$', class_id_list):
            raise ValidationError('class_id_list contains invalid characters')

        int_class_id_list = [int(class_id)
                             for class_id in class_id_list.split(',') if class_id]
        for class_id in int_class_id_list:
            class_instance = ClassModel.query.get(class_id)
            if not class_instance:
                raise ValidationError('Class not found')
