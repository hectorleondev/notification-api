import json
from typing import Any

from aws_lambda_powertools import Logger

from src.data.data_type import NotificationInputData
from src.services.config import ConfigService
from src.services.db import get_all_user_by_category_id, save_log
from src.data.enum import SchemaNames, NotificationTypes
from src.services.util import get_random_id
from src.services.validation import validate_event


class NotificationController:
    def __init__(self, _conf_svc: ConfigService, _event: Any, _logger: Logger):
        self.conf_svc = _conf_svc
        self.logger = _logger
        self.event = _event

    def create_notification(self):
        self.logger.info({"message": "Event information", "event_info": self.event})

        body = json.loads(self.event.get("body", {}))

        validate_event(body, SchemaNames.CREATE_NOTIFICATION.value)

        fields = NotificationInputData.from_dict(body)

        users = get_all_user_by_category_id(fields.category_id)

        for user in users:
            notification_types = user.notification_types
            for item in notification_types:
                self.process_notification(item)

                save_log(log_id=get_random_id(),
                                  user_id=user.user_id,
                                  category_id=fields.category_id,
                                  notification_type=item,
                                  message=fields.message)

        return {"message": "The notification was sent successfully"}

    def process_notification(self, notification_type: str):
        if notification_type == NotificationTypes.sms:
            self.logger.info("add logic to send sms")
        if notification_type == NotificationTypes.email:
            self.logger.info("add logic to send email")
        if notification_type == NotificationTypes.push_notification:
            self.logger.info("add logic to push notification")
