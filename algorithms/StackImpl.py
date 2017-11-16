# https://runestone.academy/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html
# Vijayarajan Govindarajan 2017

class StackImpl:
    def __init__(self):
        self.container = []

    def __repr__(self):
        return str(self.container)

    def push(self, value):
        self.container.append(value)

    def pop(self):
        count = len(self.container)
        if count > 0:
            return self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[len(self.container) - 1]

    def size(self):
        return len(self.container)


def main():
    stack = StackImpl()
    stack.push(1)
    stack.push("True")
    stack.push(23.34)
    print(stack)
    while not stack.isEmpty():
        print(str(stack.pop()))


if __name__ == "__main__":
    main()
