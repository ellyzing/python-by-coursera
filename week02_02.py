import json
import functools


def to_json(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        result=func(*args, **kwargs)
        return json.dumps(result)
    return inner
