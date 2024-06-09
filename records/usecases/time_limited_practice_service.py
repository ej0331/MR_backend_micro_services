from repositories.time_limited_practice_repo import TimeLimitedPracticeRepository
from dtos.record_dto import RecordDto
from dtos.time_limited_practice_dto import TimeLimitedPracticeDto


class TimeLimitedPracticeService():
    def __init__(self) -> None:
        self.time_limited_practice_repo = TimeLimitedPracticeRepository()

    def get_all_time_limited_practices(self):
        time_limited_practices, total = self.time_limited_practice_repo.get_all_time_limited_practices()
        result = [TimeLimitedPracticeDto(
            model).serialize() for model in time_limited_practices]

        return result, total

    def get_time_limited_practices(self, name=None, class_id_list=None, type_id_list=None, finished_start=None, finished_end=None, page=1, per_page=10):
        time_limited_practices, max_page, total, from_index, to_index = self.time_limited_practice_repo.get_time_limited_practices(
            name, class_id_list, type_id_list, finished_start, finished_end, page, per_page)
        result = [TimeLimitedPracticeDto(
            model).serialize() for model in time_limited_practices]

        return result, max_page, total, from_index, to_index

    def get_time_limited_practice_chart_data(self, user_id, finished_start=None, finished_end=None):
        level1_correct_quantities = []
        level1_time_limits = []
        level1_total_quantities = []
        level1_time = []
        level1_finished_at_list = []

        level2_correct_quantities = []
        level2_time_limits = []
        level2_total_quantities = []
        level2_time = []
        level2_finished_at_list = []

        level3_correct_quantities = []
        level3_time_limits = []
        level3_total_quantities = []
        level3_time = []
        level3_finished_at_list = []

        quantity_limited_tests = self.time_limited_practice_repo.get_time_limited_practices_chart_data(
            user_id, finished_start, finished_end)

        for model in quantity_limited_tests:
            level1_correct_quantities.append(model.level1_correct_quantity)
            level1_time_limits.append(
                model.level1_total_quantity - model.level1_correct_quantity)
            level1_total_quantities.append(model.level1_total_quantity)
            level1_time.append(model.level1_time)
            level1_finished_at_list.append(model.finished_at)

            level2_correct_quantities.append(model.level2_correct_quantity)
            level2_time_limits.append(
                model.level2_total_quantity - model.level2_correct_quantity)
            level2_total_quantities.append(model.level2_total_quantity)
            level2_time.append(model.level2_time)
            level2_finished_at_list.append(model.finished_at)

            level3_correct_quantities.append(model.level3_correct_quantity)
            level3_time_limits.append(
                model.level3_total_quantity - model.level3_correct_quantity)
            level3_total_quantities.append(model.level3_total_quantity)
            level3_time.append(model.level3_time)
            level3_finished_at_list.append(model.finished_at)

        result = {
            "level1_correct_quantities": level1_correct_quantities,
            "level1_total_quantities": level1_total_quantities,
            "level1_time_limits": level1_time_limits,
            "level1_times": level1_time,
            "level1_finished_at_list": level1_finished_at_list,

            "level2_correct_quantities": level2_correct_quantities,
            "level2_total_quantities": level2_total_quantities,
            "level2_time_limits": level2_time_limits,
            "level2_times": level2_time,
            "level2_finished_at_list": level2_finished_at_list,

            "level3_correct_quantities": level3_correct_quantities,
            "level3_total_quantities": level3_total_quantities,
            "level3_time_limits": level3_time_limits,
            "level3_times": level3_time,
            "level3_finished_at_list": level3_finished_at_list,
        }

        return result

    def insert_time_limited_practice(self, user_id, type_id, total_quantity, correct_quantity, time, time_limit):
        result = self.time_limited_practice_repo.insert_time_limited_practice(
            user_id=user_id,
            type_id=type_id,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            time=time,
            time_limit=time_limit,
        )

        return RecordDto(result).serialize()

    def update_time_limited_practice(self, id, level, total_quantity, correct_quantity, time, time_limit):
        result = self.time_limited_practice_repo.update_time_limited_practice(
            id=id,
            level=level,
            total_quantity=total_quantity,
            correct_quantity=correct_quantity,
            time=time,
            time_limit=time_limit,
        )

        return RecordDto(result).serialize()
