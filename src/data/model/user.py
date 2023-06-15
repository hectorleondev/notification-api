import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, JSONAttribute


class UserModel(Model):
    """
    A model with an index
    """

    class Meta:
        table_name = os.getenv("USER_TABLE")
        region = os.getenv("REGION", "us-east-1")

    user_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    phone_number = UnicodeAttribute()
    categories = JSONAttribute(default=[])
    notification_types = JSONAttribute(default=[])

    def to_dict(self):
        """
        Retrieves the model as a dictionary
        :return:
        """
        _dict_data = {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "categories": self.categories,
            "notification_types": self.notification_types
        }
        return _dict_data
