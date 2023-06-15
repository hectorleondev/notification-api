import json

import pytest

from src.controller.category_controller import CategoryController
from src.handlers import category_handler


class TestCategoryHandler:
    def test_get_category_list_handler(self, mocker):
        expected = {
            "categories": [
                {
                    "category_id": "C001",
                    "name": "One"
                },
                {
                    "category_id": "C002",
                    "name": "Two"
                }
            ]
        }

        mocker.patch.object(CategoryController, 'get_category_list')
        CategoryController.get_category_list.return_value = {
            "categories": [
                {
                    "category_id": "C001",
                    "name": "One"
                },
                {
                    "category_id": "C002",
                    "name": "Two"
                }
            ]
        }

        response = category_handler.get_category_list_handler({}, None)
        assert json.loads(response["body"]) == expected
        assert response["statusCode"] == 200
