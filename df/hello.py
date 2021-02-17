import os


def hello():
    return f"Hello world, {os.environ['SECRET']}"


if __name__ == '__main__':
    print(hello())
