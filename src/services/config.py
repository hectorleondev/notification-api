import os

import boto3


class ConfigService:
    def __init__(self):
        self.LOGGER_SERVICE_NAME: str = os.getenv("LOGGER_SERVICE_NAME")
        self.REGION: str = os.getenv("REGION", "us-east-1")
