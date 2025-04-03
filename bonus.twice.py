from decorator import decorator

@decorator
def twice(func, *args, **kwargs):
    func(*args, **kwargs)
    return func(*args, **kwargs)

if __name__ == '__main__':
    @twice
    def say_hello():
        print("Hello!")

    say_hello()
