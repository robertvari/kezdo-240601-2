def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper