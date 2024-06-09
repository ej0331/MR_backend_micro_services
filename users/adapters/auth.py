from dotenv import load_dotenv
from flask import Blueprint, request, current_app
from marshmallow import ValidationError
from validations.student_login_schema import StudentLoginSchema
from validations.teacher_login_schema import TeacherLoginSchema
from utilities.api_response_helper import make_success_response, make_error_response
from usecases.auth_service import AuthService

auth_blueprint = Blueprint('auth_blueprint', __name__)
auth_service = AuthService()
load_dotenv()


@auth_blueprint.route('/teacher/login', methods=['POST'])
def teacher_login():
    data = request.json
    messages = []

    try:
        validated_data = TeacherLoginSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)
    
    try:
        account = validated_data.get('account')
        password = validated_data.get('password')
        
        data, messages = auth_service.teacher_login(account, password, messages)
        return make_success_response(data, 200)
    except Exception as e:
        messages.append(e)
        return make_error_response(messages, 500)

@auth_blueprint.route('/student/login', methods=['POST'])
def student_login():
    data = request.json
    messages = []

    try:
        validated_data = StudentLoginSchema().load(data)
    except ValidationError as err:
        for message in err.messages:
            messages.append({
                message: err.messages[message][0]
            })
        return make_error_response(messages, 400)
    try:
        account = validated_data.get('account')
        data, messages = auth_service.student_login(account, messages)

        return make_success_response(data, 200)
    except Exception as e:
        messages.append(e)
        return make_error_response(messages, 500)
