from repositories.time_limited_test_repo import TimeLimitedTestRepository
from dtos.record_dto import RecordDto
from dtos.time_limited_test_dto import TimeLimitedTestDto


class TimeLimitedTestService():
    def __init__(self) -> None:
        self.time_limited_test_repo = TimeLimitedTestRepository()

    def get_all_time_limited_tests(self):
        time_limited_tests, total = self.time_limited_test_repo.get_all_time_limited_tests()
        result = [TimeLimitedTestDto(
            model).serialize() for model in time_limited_tests]

        return result, total

    def get_time_limited_tests(self, name=None, class_id_list=None, type_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        time_limited_tests, max_page, total, from_index, to_index = self.time_limited_test_repo.get_time_limited_tests(
            name, class_id_list, type_id_list, finished_start, finished_end, page, per_page)
        result = [TimeLimitedTestDto(
            model).serialize() for model in time_limited_tests]

        return result, max_page, total, from_index, to_index

    def get_time_limited_test_chart_data(self, user_id, finished_start=None, finished_end=None):
        level1_correct_quantity_list = []
        level1_incorrect_quantity_list = []
        level1_total_quantity_list = []
        level1_times = []
        level1_time_limit_list = []
        level1_finished_at_list = []

        level2_correct_quantity_list = []
        level2_incorrect_quantity_list = []
        level2_total_quantity_list = []
        level2_times = []
        level2_time_limit_list = []
        level2_finished_at_list = []

        level3_correct_quantity_list = []
        level3_incorrect_quantity_list = []
        level3_total_quantity_list = []
        level3_times = []
        level3_time_limit_list = []
        level3_finished_at_list = []

        time_limited_tests = self.time_limited_test_repo.get_time_limited_tests_chart_data(
            user_id, finished_start, finished_end)

        for model in time_limited_tests:
            level1_correct_quantity_list.append(model.level1_correct_quantity)
            level1_incorrect_quantity_list.append(
                model.level1_incorrect_quantity)
            level1_total_quantity_list.append(model.level1_total_quantity)
            level1_times.append(model.level1_time)
            level1_time_limit_list.append(model.level1_time_limit)
            level1_finished_at_list.append(model.finished_at)

            level2_correct_quantity_list.append(model.level2_correct_quantity)
            level2_incorrect_quantity_list.append(
                model.level2_incorrect_quantity)
            level2_total_quantity_list.append(model.level2_total_quantity)
            level2_times.append(model.level2_time)
            level2_time_limit_list.append(model.level2_time_limit)
            level2_finished_at_list.append(model.finished_at)

            level3_correct_quantity_list.append(model.level3_correct_quantity)
            level3_incorrect_quantity_list.append(
                model.level3_incorrect_quantity)
            level3_total_quantity_list.append(model.level3_total_quantity)
            level3_times.append(model.level3_time)
            level3_time_limit_list.append(model.level3_time_limit)
            level3_finished_at_list.append(model.finished_at)

        result = {
            "level1_correct_quantity_list": level1_correct_quantity_list,
            "level1_incorrect_quantity_list": level1_incorrect_quantity_list,
            "level1_total_quantity_list": level1_total_quantity_list,
            "level1_time_list": level1_times,
            "level1_time_limit_list": level1_time_limit_list,
            "level1_finished_at_list": level1_finished_at_list,

            "level2_correct_quantity_list": level2_correct_quantity_list,
            "level2_incorrect_quantity_list": level2_incorrect_quantity_list,
            "level2_total_quantity_list": level2_total_quantity_list,
            "level2_time_list": level2_times,
            "level2_time_limit_list": level2_time_limit_list,
            "level2_finished_at_list": level2_finished_at_list,

            "level3_correct_quantity_list": level3_correct_quantity_list,
            "level3_incorrect_quantity_list": level3_incorrect_quantity_list,
            "level3_total_quantity_list": level3_total_quantity_list,
            "level3_time_list": level3_times,
            "level3_time_limit_list": level3_time_limit_list,
            "level3_finished_at_list": level3_finished_at_list,
        }

        return result

    def insert_time_limited_test(self, user_id, type_id, total_quantity, correct_quantity, incorrect_quantity, time, time_limit):
        result = self.time_limited_test_repo.insert_time_limited_test(
            user_id=user_id,
            type_id=type_id,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            incorrect_quantity=incorrect_quantity,
            time=time,
            time_limit=time_limit,
        )

        return RecordDto(result).serialize()

    def update_time_limited_test(self, id, level, total_quantity, correct_quantity, incorrect_quantity, time, time_limit):
        result = self.time_limited_test_repo.update_time_limited_test(
            id=id,
            level=level,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            incorrect_quantity=incorrect_quantity,
            time=time,
            time_limit=time_limit,
        )

        return RecordDto(result).serialize()
