from dtos.base_dto import BaseDto
from models.time_limited_practice_model import TimeLimitedPracticeModel


class TimeLimitedPracticeDto(BaseDto):
    def __init__(self, model: TimeLimitedPracticeModel):
        self.id = model.id
        self.user = {
            "id": model.user.id,
            "name": model.user.name,
        }
        self.class_ = {
            "id": model.user.class_instance.id,
            "name": model.user.class_instance.name,
        }
        self.type = {
            "id": model.type.id,
            "name": model.type.name,
        }

        self.level1_correct_quantity = model.level1_correct_quantity
        self.level1_total_quantity = model.level1_total_quantity
        self.level1_time = model.level1_time
        self.level1_time_limit = model.level1_time_limit
        self.level2_correct_quantity = model.level2_correct_quantity
        self.level2_total_quantity = model.level2_total_quantity
        self.level2_time = model.level2_time
        self.level2_time_limit = model.level2_time_limit
        self.level3_correct_quantity = model.level3_correct_quantity
        self.level3_total_quantity = model.level3_total_quantity
        self.level3_time = model.level3_time
        self.level3_time_limit = model.level3_time_limit
        self.finished_at = model.finished_at
