import json

import pytest

from src.controller import notification_controller
from src.data.exceptions import BadRequestException


class TestCategoryModel:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


class TestUserModel:
    def __init__(self, user_id, name, email, notification_types):
        self.user_id = user_id
        self.name = name
        self.email = email,
        self.notification_types = notification_types


class TestNotificationController:

    def test_get_log_list(self, mocker):
        expected = {
            "message": "The notification was sent successfully"
        }

        mocker.patch.object(notification_controller, 'get_category')
        notification_controller.get_category.return_value = TestCategoryModel("c001", "category one")

        mocker.patch.object(notification_controller, 'get_all_user_by_category_id')
        notification_controller.get_all_user_by_category_id.return_value = [TestUserModel("u001", "one", "u001@test.co",
                                                                                          ["one", "two"])]

        mocker.patch.object(notification_controller, 'get_random_id')
        mocker.patch.object(notification_controller, 'save_log')

        notification = notification_controller.NotificationController({
            "body": json.dumps({
                "category_id": "C003",
                "message": "Hello World!"
            })
        }, None)

        response = notification.create_notification()
        assert response == expected
