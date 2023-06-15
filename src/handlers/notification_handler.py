from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.controller.notification_controller import NotificationController
from src.services.config import ConfigService
from src.services.response import ResponseService


@ResponseService.pretty_response
def create_notification_handler(event, context, conf_svc: ConfigService, logger: Logger):
    notification = NotificationController(_conf_svc=conf_svc, _event=event, _logger=logger)
    response = notification.create_notification()
    return HTTPStatus.OK, response
