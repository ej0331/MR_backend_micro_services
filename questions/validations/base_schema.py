import re
from marshmallow import Schema, ValidationError
from models.type_model import TypeModel


class BaseSchema(Schema):
    def type_id_not_exists(type_id):
        typeModel = TypeModel.query.get(type_id)
        if not typeModel:
            raise ValidationError('Type not found')

    def type_id_list_not_exists(type_id_list):
        int_type_id_list = [int(type_id)
                            for type_id in type_id_list.split(',') if type_id]
        for type_id in int_type_id_list:
            typeModel = TypeModel.query.get(type_id)
            if not typeModel:
                raise ValidationError('Type not found')

    def validate_level(level):
        if level is not None and level > 3:
            raise ValidationError("Level must be less than or equal to 3.")
        return level

