from http import HTTPStatus

from aws_lambda_powertools import Logger

from src.controller.category_controller import CategoryController
from src.services.config import ConfigService
from src.services.response import ResponseService


@ResponseService.pretty_response
def get_category_list_handler(event, context, logger: Logger):
    category = CategoryController(_event=event, _logger=logger)
    response = category.get_category_list()
    return HTTPStatus.OK, response

