from src.data.model.category import CategoryModel
from src.data.model.log import LogModel
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


def get_user(user_id: str):
    """
    Get user by ID
    :param user_id:
    :return:
    """
    return UserModel.get(user_id)


def save_log(log_id: str, user_id: str, category_id: str, notification_type: str, message):
    log = LogModel()
    log.log_id = log_id
    log.user_id = user_id
    log.category_id = category_id
    log.notification_type = notification_type
    log.message = message
    log.save()
