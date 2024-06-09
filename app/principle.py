from flask import Flask
from flask_principal import Principal, Permission, RoleNeed, identity_loaded
from flask_login import current_user

principle = None
teacher_permission = None
student_permission = None


def principle_init(app: Flask) -> None:
    global principle, teacher_permission, student_permission
    principal = Principal(app)
    teacher_role = RoleNeed('teacher')
    student_role = RoleNeed('student')
    teacher_permission = Permission(teacher_role)
    student_permission = Permission(student_role)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        if current_user and hasattr(current_user, 'account'):
            if current_user.account == 'teacher':
                identity.provides.add(teacher_role)
            else:
                identity.provides.add(student_role)
