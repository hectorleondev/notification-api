import json
from typing import Any

from aws_lambda_powertools import Logger

from src.data.data_type import NotificationInputData
from src.data.exceptions import BadRequestException
from src.data.model.user import UserModel
from src.services.db import get_all_user_by_category_id, save_log, get_category
from src.data.enum import SchemaNames, NotificationTypes, ErrorMessage
from src.services.util import get_random_id
from src.services.validation import validate_event


class NotificationController:
    def __init__(self,  _event: Any, _logger: Logger):
        self.logger = _logger
        self.event = _event

    def create_notification(self):
        self.logger.info({"message": "Event information", "event_info": self.event})

        body = json.loads(self.event.get("body", {}))

        validate_event(body, SchemaNames.CREATE_NOTIFICATION.value)

        fields = NotificationInputData.from_dict(body)

        if get_category(fields.category_id) is None:
            raise BadRequestException(ErrorMessage.NOT_FOUND_CATEGORY.value)

        users = get_all_user_by_category_id(fields.category_id)

        if not users:
            raise BadRequestException(ErrorMessage.SUBSCRIPTION_ERROR.value)

        for user in users:
            notification_types = user.notification_types
            for item in notification_types:
                self.process_notification(item, user)

                save_log(log_id=get_random_id(),
                                  user_id=user.user_id,
                                  category_id=fields.category_id,
                                  notification_type=item,
                                  message=fields.message)

        return {"message": "The notification was sent successfully"}

    def process_notification(self, notification_type: str, user: UserModel):
        if notification_type == NotificationTypes.sms.value:
            self.logger.info(f"add logic to send sms to {user.name}")
        if notification_type == NotificationTypes.email.value:
            self.logger.info(f"add logic to send email to {user.name}")
        if notification_type == NotificationTypes.push_notification.value:
            self.logger.info(f"add logic to push notification {user.name}")
