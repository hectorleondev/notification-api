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

        for item in logs:
            response.append({
                "log_id": item.log_id,
                "user_id": item.user_id,
                "user_name": item.user_name,
                "email": item.email,
                "phone_number": item.phone_number,
                "category": item.category_name,
                "channel": item.notification_type,
                "message": item.message,
                "create_at": item.createdAt.strftime('%Y-%m-%d %H:%M')
            })

        return {"logs": response}
