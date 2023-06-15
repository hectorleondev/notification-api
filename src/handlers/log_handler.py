from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.controller.log_controller import LogController
from src.controller.notification_controller import NotificationController
from src.services.config import ConfigService
from src.services.response import ResponseService


@ResponseService.pretty_response
def get_log_list_handler(event, context, logger: Logger):
    log = LogController(_event=event, _logger=logger)
    response = log.get_log_list()
    return HTTPStatus.OK, response
