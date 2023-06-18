import datetime
from src.controller import log_controller


class TestCategoryModel:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


class TestUserModel:
    def __init__(self, user_id, name, email, phone_number):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone_number = phone_number


class TestLogModel:
    def __init__(self, log_id, user_id, user_name, email, phone_number, category_id, category_name, notification_type, message, createdAt):
        self.log_id = log_id
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.category_id = category_id
        self.category_name = category_name
        self.notification_type = notification_type
        self.message = message
        self.createdAt = createdAt


class TestLogController:

    def test_get_log_list(self, mocker):
        expected = {
            "logs": [
                {
                    "log_id": "l001",
                    "user_id": "u001",
                    "user_name": "one",
                    "email": "u001@test.co",
                    "phone_number": "111",
                    "category": "category one",
                    "channel": "movie",
                    "message": "hello",
                    "create_at": "2000-01-01 00:00"
                },
                {
                    "log_id": "l002",
                    "user_id": "u001",
                    "user_name": "one",
                    "email": "u001@test.co",
                    "phone_number": "111",
                    "category": "category one",
                    "channel": "finance",
                    "message": "again",
                    "create_at": "2000-01-01 00:00"
                }
            ]
        }

        logs_data = [
            TestLogModel("l001", "u001", "one", "u001@test.co", "111", "c001", "category one", "movie", "hello", datetime.datetime(2000, 1, 1, 0, 0)),
            TestLogModel("l002", "u001", "one", "u001@test.co", "111", "c001", "category one", "finance", "again", datetime.datetime(2000, 1, 1, 0, 0)),
        ]

        mocker.patch.object(log_controller, 'get_logs')
        log_controller.get_logs.return_value = logs_data

        log = log_controller.LogController({}, None)
        response = log.get_log_list()
        assert response == expected
