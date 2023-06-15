import os

from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, UTCDateTimeAttribute)
from datetime import datetime
from pynamodb.indexes import (GlobalSecondaryIndex, AllProjection)


class UserIndex(GlobalSecondaryIndex):
    class Meta:
        projection = AllProjection()

    user_id = UnicodeAttribute(hash_key=True)


class CategoryIndex(GlobalSecondaryIndex):
    class Meta:
        projection = AllProjection()

    category_id = UnicodeAttribute(hash_key=True)


class UserCategoryIndex(GlobalSecondaryIndex):
    class Meta:
        projection = AllProjection()

    category_id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(range_key=True)


class LogModel(Model):
    """
    A model with an index
    """

    class Meta:
        table_name = os.getenv("LOG_TABLE")
        region = os.getenv("REGION", "us-east-1")

    log_id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(null=False)
    category_id = UnicodeAttribute(null=False)
    notification_type = UnicodeAttribute(null=False)
    message = UnicodeAttribute()
    createdAt = UTCDateTimeAttribute(null=False, default=datetime.now())

    user_index = UserIndex()
    category_index = CategoryIndex()
    user_category_index = UserCategoryIndex()

    def to_dict(self):
        """
        Retrieves the model as a dictionary
        :return:
        """
        _dict_data = {
            "log_id": self.log_id,
            "user_id": self.user_id,
            "category_id": self.category_id,
            "notification_type": self.notification_type,
            "createdAt": self.createdAt
        }
        return _dict_data
