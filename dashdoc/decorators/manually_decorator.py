def decorator_func(func):
    def wrapped(word="projects"):
        print("Before func")
        func(word)
        print("After func")
        return func
    return wrapped


if __name__ == "__main__":
    print(decorator_func(print)) #("Hello, world")
    decorator_func(print) # Out: None
    decorator_func(print)()
