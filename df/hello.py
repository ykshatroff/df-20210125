import os


def hello():
    return f"Hello world, {os.environ['SECRET']}"


class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Hello:
    def __init__(self):
        self.user = User(os.environ['SECRET'])

    def get_user(self):
        return self.user

    def output(self):
        return f"Hello world, {self.get_user().name}"


if __name__ == '__main__':
    print(hello())
