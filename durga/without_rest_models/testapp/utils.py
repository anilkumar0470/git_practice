import json


def is_valid_json(data):

    try:
        p_data = json.loads(data)
        return True
    except ValueError:
        return False

