import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class CategoryModel(Model):
    """
    A model with an index
    """

    class Meta:
        table_name = os.getenv("CATEGORY_TABLE")
        region = os.getenv("REGION", "us-east-1")

    category_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)

    def to_dict(self):
        """
        Retrieves the model as a dictionary
        :return:
        """
        _dict_data = {
            "category_id": self.category_id,
            "name": self.name
        }
        return _dict_data
