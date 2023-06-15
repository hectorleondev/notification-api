import json
from src.controller.log_controller import LogController
from src.handlers import log_handler


class TestLogModel:
    def __init__(self, log_id, user_id, category_id, notification_type, message, createdAt):
        self.log_id = log_id
        self.user_id = user_id
        self.category_id = category_id
        self.notification_type = notification_type
        self.message = message
        self.createdAt = createdAt


class TestLogHandler:

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

        mocker.patch.object(LogController, 'get_log_list')
        LogController.get_log_list.return_value = {
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

        response = log_handler.get_log_list_handler({}, None)
        assert json.loads(response["body"]) == expected
        assert response["statusCode"] == 200
