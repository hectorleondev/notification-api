from typing import Any

from aws_lambda_powertools import Logger

from src.services.db import get_logs, get_user, get_category


class LogController:
    def __init__(self,  _event: Any, _logger: Logger):
        self.logger = _logger
        self.event = _event

    def get_log_list(self):
        response = []
        logs = get_logs()
        users = {}
        categories = {}

        for item in logs:
            if item.user_id not in users:
                users[item.user_id] = get_user(item.user_id)

            if item.category_id not in categories:
                categories[item.category_id] = get_category(item.category_id)

            response.append({
                "log_id": item.log_id,
                "user_id": item.user_id,
                "user_name": users[item.user_id].name,
                "email": users[item.user_id].email,
                "phone_number": users[item.user_id].phone_number,
                "category": categories[item.category_id].name,
                "channel": item.notification_type,
                "message": item.message,
                "create_at": item.createdAt.strftime('%m/%d/%Y %H:%M')
            })

        return {"logs": response}
