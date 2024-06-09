from repositories.student_repo import StudentRepository
from dtos.user_detail_dto import UserDetailDto

class StudentService():
    def __init__(self) -> None:
        self.student_repo = StudentRepository()

    def get_users(self, name=None, account=None, class_id_list=None):
        users, total = self.student_repo.get_users(name, account, class_id_list)
        result = [UserDetailDto(user).serialize() for user in users]
        return result, total

    def get_user(self, id):
        result = self.student_repo.get_user(id)
        return UserDetailDto(result).serialize()

    def insert_user(self, class_id, name, account):
        result = self.student_repo.insert_user(class_id, name, account)
        return UserDetailDto(result).serialize()

    def update_user(self, id, class_id, account, name):
        result = self.student_repo.update_user(
            id=id,
            class_id=class_id,
            account=account,
            name=name,
        )
        return UserDetailDto(result).serialize()

    def delete_user(self, id):
        return self.student_repo.delete_user(id)
