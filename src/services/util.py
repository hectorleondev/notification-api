import json
import os
from src.data import schema
from src.services.config import ConfigService

conf_service = ConfigService()


def get_content_json(filename: str) -> dict:
    """
    get json content
    :param filename:
    :return:
    """
    with open(f"{os.path.dirname(schema.__file__)}/{filename}.json") as f:
        data = json.load(f)
    return data
