from dotenv import load_dotenv
import os


class EnvironmentValues:
    def __init__(self):
        load_dotenv()
        self.env_values = os.environ

    def get_value(self, key):
        return self.env_values.get(key)
