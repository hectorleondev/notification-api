from src.data.model.category import CategoryModel
from src.data.model.user import UserModel


def get_categories():
    """
    Get all categories
    :return:
    """
    try:
        _categories = list(CategoryModel.scan())
    except CategoryModel.DoesNotExist:
        _categories = []
    _categories = [_key.to_dict() for _key in _categories]
    return _categories


def get_all_user_by_category_id(category_id: str):
    """
    Get all user by category id
    :param category_id:
    :return:
    """
    return list(UserModel.scan(filter_condition=UserModel.categories.contains(category_id)))
