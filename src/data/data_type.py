from dataclasses import dataclass
from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class NotificationInputData:
    category_id: str
    message: str
