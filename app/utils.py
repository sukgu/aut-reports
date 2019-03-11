import json
from app.models import Testcase

def validate_json(filename):
    with open(filename) as file:
        try:
            return json.load(file)
        except Exception as e:
            return repr(e)
        
def get_object_from_json(filename):
    with open(filename) as file:
        json_content = json.load(file)
        items = json_content.items()
        testcase_list = []
        for item in items:
            title = item[0]
            result = item[1]
            testcase = Testcase()
            testcase.result = result
            testcase.title = title
            testcase_list.append(testcase)
        return testcase_list
        