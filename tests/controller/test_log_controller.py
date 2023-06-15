import datetime
from src.controller import log_controller


class TestCategoryModel:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


class TestUserModel:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


class TestLogModel:
    def __init__(self, log_id, user_id, category_id, notification_type, message, createdAt):
        self.log_id = log_id
        self.user_id = user_id
        self.category_id = category_id
        self.notification_type = notification_type
        self.message = message
        self.createdAt = createdAt


class TestLogController:

    def test_get_log_list(self, mocker):
        expected = {
            "logs": [
                {
                    "id": "l001",
                    "user_name": "one",
                    "email": "u001@test.co",
                    "category": "category one",
                    "channel": "movie",
                    "message": "hello",
                    "create_at": "01/01/2000"
                },
                {
                    "id": "l002",
                    "user_name": "one",
                    "email": "u001@test.co",
                    "category": "category one",
                    "channel": "finance",
                    "message": "again",
                    "create_at": "01/01/2000"
                }
            ]
        }

        logs_data = [
            TestLogModel("l001", "u001", "c001", "movie", "hello", datetime.datetime(2000, 1, 1, 0, 0)),
            TestLogModel("l002", "u001", "c001", "finance", "again", datetime.datetime(2000, 1, 1, 0, 0)),
        ]

        mocker.patch.object(log_controller, 'get_logs')
        log_controller.get_logs.return_value = logs_data

        mocker.patch.object(log_controller, 'get_category')
        log_controller.get_category.return_value = TestCategoryModel("c001", "category one")

        mocker.patch.object(log_controller, 'get_user')
        log_controller.get_user.return_value = TestUserModel("u001", "one", "u001@test.co")

        log = log_controller.LogController({}, None)
        response = log.get_log_list()
        assert response == expected
