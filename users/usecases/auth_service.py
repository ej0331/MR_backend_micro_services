from repositories.auth_repo import AuthRepository

class AuthService():
    def __init__(self) -> None:
        self.auth_repo = AuthRepository()

    def teacher_login(self, account, password, messages):
        result, messages = self.auth_repo.teacher_login(account, password, messages)
        return result, messages
    
    def student_login(self, account, messages):
        result, messages = self.auth_repo.student_login(account, messages)
        return result, messages
