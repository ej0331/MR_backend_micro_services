from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from .base_model import BaseModel
from .user_model import UserModel
from .type_model import TypeModel


class QuantityLimitedPracticeModel(BaseModel):
    __tablename__ = 'quantity_limited_practices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)
    level1_total_quantity = Column(Integer, nullable=False)
    level1_time = Column(Integer, nullable=False)
    level2_total_quantity = Column(Integer, nullable=True)
    level2_time = Column(Integer, nullable=True)
    level3_total_quantity = Column(Integer, nullable=True)
    level3_time = Column(Integer, nullable=True)
    finished_at = Column(TIMESTAMP, nullable=False)

    type = relationship(TypeModel, backref='quantity_limited_practices')

    def __init__(self, user_id, type_id, level1_total_quantity, level1_time, finished_at, level2_total_quantity=None, level2_time=None, level3_total_quantity=None, level3_time=None):
        self.user_id = user_id
        self.type_id = type_id
        self.level1_total_quantity = level1_total_quantity
        self.level1_time = level1_time
        self.level2_total_quantity = level2_total_quantity
        self.level2_time = level2_time
        self.level3_total_quantity = level3_total_quantity
        self.level3_time = level3_time
        self.finished_at = finished_at
