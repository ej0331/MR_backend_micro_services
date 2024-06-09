def _drop_all_tables(app, db):
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.session.commit()
        db.session.close()
        print("Database dropped")


def _create_all_tables(app, db):
    with app.app_context():
        import models.system_parameter_model
        import models.user_model
        import models.type_model
        import models.question_model
        db.reflect()
        db.create_all()
        db.session.commit()
        db.session.close()
        print("Database created")


def init_database(app, db):
    with app.app_context():
        if (os.getenv('ENV') == 'develop'):
            _drop_all_tables(app, db)
        _create_all_tables(app, db)


def run_seeder(entry):
    from seeds.system_parameter_seeder import SystemParameterSeeder
    from seeds.type_seeder import TypeSeeder
    from seeds.question_seeder import QuestionSeeder

    with app.app_context():
        SystemParameterSeeder().run()
        TypeSeeder().run()
        QuestionSeeder(entry).run()


if __name__ == '__main__':
    from dotenv import load_dotenv
    import os

    load_dotenv()
    if (os.getenv('ENV') != 'develop'):
        account = input("Who am I: ")
        secret = input("Secret: ")

        if account != "root" or secret != "qtds":
            print("Invalid account or secret. Exiting...")
            exit()

    try:
        import sys
        from flask import Flask

        print("create app")
        app = Flask(__name__)

        from app.database import db_init
        db_init(app)
        from app.database import db

        from app.bcrypt import bcrypt_init
        bcrypt_init(app)

        entry = os.path.dirname(os.path.realpath(__name__))

        init_database(app, db)
        run_seeder(entry)
        print("Database initialized")
    except Exception as e:
        print("An error occurred:", e)

    if (os.getenv('ENV') != 'develop'):
        input("Press Enter to exit...")
        sys.exit(1)
