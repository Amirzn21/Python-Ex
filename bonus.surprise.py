def surprise(func):
    def wrapper(*args, **kwargs):
        return "Surprise!"
    return wrapper

if __name__ == '__main__':
    @surprise
    def hello():
        return "Hello, world!"

    print(hello())
