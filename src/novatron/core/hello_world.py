def hello_world(name="world", extra=None, greetingto=None):
    """
    hip-cargo hello world example
    """
    greeting = f"Hello, {name}! \n {extra}"
    if greetingto is not None:
        with open(greetingto, "w") as f:
            f.write(greeting)
    else:
        print(greeting)
