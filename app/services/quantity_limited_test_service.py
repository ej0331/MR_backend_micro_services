from ..daos.quantity_limited_test_dao import QuantityLimitedTestDao
from ..dtos.record_dto import RecordDto
from ..dtos.quantity_limited_test_dto import QuantityLimitedTestDto


class QuantityLimitedTestService():
    def __init__(self) -> None:
        self.quantity_limited_test_dao = QuantityLimitedTestDao()

    def get_all_quantity_limited_tests(self):
        quantity_limited_tests, total = self.quantity_limited_test_dao.get_all_quantity_limited_tests()
        result = [QuantityLimitedTestDto(
            model).serialize() for model in quantity_limited_tests]

        return result, total

    def get_quantity_limited_tests(self, name=None, class_id_list=None, type_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        quantity_limited_tests, max_page, total, from_index, to_index = self.quantity_limited_test_dao.get_quantity_limited_tests(
            name, class_id_list, type_id_list, finished_start, finished_end, page, per_page)
        result = [QuantityLimitedTestDto(
            model).serialize() for model in quantity_limited_tests]

        return result, max_page, total, from_index, to_index

    def get_quantity_limited_tests_chart_data(self, user_id, finished_start=None, finished_end=None):
        level1_correct_quantity_list = []
        level1_incorrect_quantity_list = []
        level1_time_list = []
        level1_finished_at_list = []

        level2_correct_quantity_list = []
        level2_incorrect_quantity_list = []
        level2_time_list = []
        level2_finished_at_list = []

        level3_correct_quantity_list = []
        level3_incorrect_quantity_list = []
        level3_time_list = []
        level3_finished_at_list = []

        quantity_limited_tests = self.quantity_limited_test_dao.get_quantity_limited_tests_chart_data(
            user_id, finished_start, finished_end)

        for model in quantity_limited_tests:
            level1_correct_quantity_list.append(model.level1_correct_quantity)
            level1_incorrect_quantity_list.append(
                model.level1_total_quantity - model.level1_correct_quantity)
            level1_time_list.append(model.level1_time)
            level1_finished_at_list.append(model.finished_at)

            level2_correct_quantity_list.append(model.level2_correct_quantity)
            level2_incorrect_quantity_list.append(
                model.level2_total_quantity - model.level2_correct_quantity)
            level2_time_list.append(model.level2_time)
            level2_finished_at_list.append(model.finished_at)

            level3_correct_quantity_list.append(model.level3_correct_quantity)
            level3_incorrect_quantity_list.append(
                model.level3_total_quantity - model.level3_correct_quantity)
            level3_time_list.append(model.level3_time)
            level3_finished_at_list.append(model.finished_at)

        result = {
            "level1_correct_quantity_list": level1_correct_quantity_list,
            "level1_incorrect_quantity_list": level1_incorrect_quantity_list,
            "level1_time_list": level1_time_list,
            "level1_finished_at_list": level1_finished_at_list,

            "level2_correct_quantity_list": level2_correct_quantity_list,
            "level2_incorrect_quantity_list": level2_incorrect_quantity_list,
            "level2_time_list": level2_time_list,
            "level2_finished_at_list": level2_finished_at_list,

            "level3_correct_quantity_list": level3_correct_quantity_list,
            "level3_incorrect_quantity_list": level3_incorrect_quantity_list,
            "level3_time_list": level3_time_list,
            "level3_finished_at_list": level3_finished_at_list,
        }

        return result

    def insert_quantity_limited_test(self, user_id, type_id, total_quantity, correct_quantity, time):
        result = self.quantity_limited_test_dao.insert_quantity_limited_test(
            user_id=user_id,
            type_id=type_id,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            time=time,
        )
        return RecordDto(result).serialize()

    def update_quantity_limited_test(self, id, level, total_quantity, correct_quantity, time):
        result = self.quantity_limited_test_dao.update_quantity_limited_test(
            id=id,
            level=level,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            time=time,
        )

        return RecordDto(result).serialize()
