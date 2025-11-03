from functools import wraps

def extract(*param_names):
    def decorator(func):
        @wraps(func)
        def wrapper(data):
            params = {name: data.get(name) for name in param_names}
            return func(**params)
        return wrapper
    return decorator