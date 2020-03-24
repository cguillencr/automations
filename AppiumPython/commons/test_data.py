import json
import os


class TestData:
    @staticmethod
    def read_test_data_file():
        helper_path = os.path.abspath(
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        test_data_file = os.path.join(helper_path, "commons", "test_data.json")

        with open(test_data_file) as file:
            return json.load(file)