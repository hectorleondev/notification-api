from src.controller import category_controller


class TestCategoryController:
    def test_get_category_list(self, mocker):
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

        mocker.patch.object(category_controller, 'get_categories')
        category_controller.get_categories.return_value = [
            {
                "category_id": "C001",
                "name": "One"
            },
            {
                "category_id": "C002",
                "name": "Two"
            }
        ]

        category = category_controller.CategoryController({}, None)
        response = category.get_category_list()
        assert response == expected

    def test_get_category_empty_list(self, mocker):
        expected = {
            "categories": []
        }

        mocker.patch.object(category_controller, 'get_categories')
        category_controller.get_categories.return_value = []

        category = category_controller.CategoryController({}, None)
        response = category.get_category_list()
        assert response == expected


