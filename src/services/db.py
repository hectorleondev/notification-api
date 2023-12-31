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
    try:
        return UserModel.get(user_id)
    except UserModel.DoesNotExist:
        return None


def get_category(category_id: str):

    try:
        return CategoryModel.get(category_id)
    except CategoryModel.DoesNotExist:
        return None


def save_log(log_id: str, user: UserModel, category: CategoryModel, notification_type: str, message):
    log = LogModel()
    log.log_id = log_id
    log.user_id = user.user_id
    log.user_name = user.name
    log.email = user.email
    log.phone_number = user.phone_number
    log.category_id = category.category_id
    log.category_name = category.name
    log.notification_type = notification_type
    log.message = message
    log.save()


def get_logs():
    return list(LogModel.scan())
