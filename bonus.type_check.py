from functools import wraps

class TypeErrorException(Exception):
    pass

def type_check(expected_type):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                raise TypeErrorException(f"Expected {expected_type}, got {type(arg)}")
            return func(arg)
        return wrapper
    return decorator

if __name__ == '__main__':
    @type_check(int)
    def add_one(n):
        return n + 1

    print(add_one(5))
