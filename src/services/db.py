from src.data.model.category import CategoryModel


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
