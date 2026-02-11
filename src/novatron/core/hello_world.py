

def hello_world(name="world", greetingto=None):
    """
    hip-cargo hello world example
    """
    greeting = f"Hello, {name}!"
    if greetingto is not None:
        with open(greetingto, "w") as f:
            f.write(greeting)
    else:
        print(greeting)