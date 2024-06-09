from faker import Faker
from sqlalchemy.sql import func
from app.database import db
from app.models.system_parameter_model import SystemParameterModel


class BaseSeeder():
    def __init__(self):
        self.db = db
        self.faker = Faker('zh_TW')

    def get_model_random_id(self, model):
        model_instance = model.query.order_by(func.random()).first()
        return model_instance.id

    def get_system_parameter(self, key):
        return SystemParameterModel.query.filter_by(key=key).first()
