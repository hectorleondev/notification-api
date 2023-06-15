from typing import Any

from aws_lambda_powertools import Logger

from src.services.config import ConfigService
from src.services.db import get_categories


class CategoryController:
    def __init__(self, _conf_svc: ConfigService, _event: Any, _logger: Logger):
        self.conf_svc = _conf_svc
        self.logger = _logger
        self.event = _event

    def get_category_list(self):
        self.logger.info({"message": "Event information", "event_info": self.event})

        categories = get_categories()

        return {"categories": categories}
