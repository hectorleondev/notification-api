import json
from src.controller.notification_controller import NotificationController
from src.handlers import notification_handler


class TestNotificationHandler:

    def test_create_notification_handler(self, mocker):
        expected = {
            "message": "OK"
        }

        mocker.patch.object(NotificationController, 'create_notification')
        NotificationController.create_notification.return_value = {
            "message": "OK"
        }

        response = notification_handler.create_notification_handler({}, None)
        assert json.loads(response["body"]) == expected
        assert response["statusCode"] == 201

    def test_validation_error_handler(self, mocker):

        response = notification_handler.create_notification_handler({
            "body": json.dumps({
                "category_id": ""
            })
        }, None)
        assert response["statusCode"] == 400
