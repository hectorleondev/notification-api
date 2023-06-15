from enum import unique, Enum


@unique
class SchemaNames(Enum):
    CREATE_NOTIFICATION = "create_notification"


@unique
class NotificationTypes(Enum):
    email = "E-Mail"
    sms = "SMS"
    push_notification = "Push Notification"


@unique
class ErrorMessage(Enum):
    SUBSCRIPTION_ERROR = "There are not subscriptions for that category"
    NOT_FOUND_CATEGORY = "Category not found"
