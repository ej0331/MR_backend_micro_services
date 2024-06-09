from ..daos.quantity_limited_practice_dao import QuantityLimitedPracticeDao
from ..dtos.record_dto import RecordDto
from ..dtos.quantity_limited_practice_dto import QuantityLimitedPracticeDto


class QuantityLimitedPracticeService():
    def __init__(self) -> None:
        self.quantity_limited_practice_dao = QuantityLimitedPracticeDao()

    def get_all_quantity_limited_practices(self):
        quantity_limited_practices, total = self.quantity_limited_practice_dao.get_all_quantity_limited_practices()
        result = [QuantityLimitedPracticeDto(
            model).serialize() for model in quantity_limited_practices]

        return result, total

    def get_quantity_limited_practices(self, name=None, class_id_list=None, type_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        quantity_limited_practices, max_page, total, from_index, to_index = self.quantity_limited_practice_dao.get_quantity_limited_practices(
            name, class_id_list, type_id_list, finished_start, finished_end, page, per_page)
        result = [QuantityLimitedPracticeDto(
            model).serialize() for model in quantity_limited_practices]

        return result, max_page, total, from_index, to_index

    def get_quantity_limited_practices_chart_data(self, user_id, finished_start=None, finished_end=None):
        level1_times = []
        level1_total_quantities = []
        level1_finished_at_list = []

        level2_times = []
        level2_total_quantities = []
        level2_finished_at_list = []

        level3_times = []
        level3_total_quantities = []
        level3_finished_at_list = []

        quantity_limited_practices = self.quantity_limited_practice_dao.get_quantity_limited_practices_chart_data(
            user_id, finished_start, finished_end)

        for model in quantity_limited_practices:
            level1_times.append(model.level1_time)
            level1_total_quantities.append(model.level1_total_quantity)
            level1_finished_at_list.append(model.finished_at)

            level2_times.append(model.level2_time)
            level2_total_quantities.append(model.level2_total_quantity)
            level2_finished_at_list.append(model.finished_at)

            level3_times.append(model.level3_time)
            level3_total_quantities.append(model.level3_total_quantity)
            level3_finished_at_list.append(model.finished_at)

        result = {
            "level1_times": level1_times,
            "level1_total_quantities": level1_total_quantities,
            "level1_finished_at_list": level1_finished_at_list,

            "level2_times": level2_times,
            "level2_total_quantities": level2_total_quantities,
            "level2_finished_at_list": level2_finished_at_list,

            "level3_times": level3_times,
            "level3_total_quantities": level3_total_quantities,
            "level3_finished_at_list": level3_finished_at_list,
        }

        return result

    def insert_quantity_limited_practice(self, user_id, type_id, total_quantity, time):
        result = self.quantity_limited_practice_dao.insert_quantity_limited_practice(
            user_id=user_id,
            type_id=type_id,
            total_quantity=total_quantity,
            time=time,
        )

        return RecordDto(result).serialize()

    def update_quantity_limited_practice(self, id, level, total_quantity, time):
        result = self.quantity_limited_practice_dao.update_quantity_limited_practice(
            id=id,
            level=level,
            total_quantity=total_quantity,
            time=time,
        )

        return RecordDto(result).serialize()
