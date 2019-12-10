#https://en.wikipedia.org/wiki/Binary_search_tree
#Vijayarajan Govindarajan 2018


class TreeNode:
    def __init__(self, left, key, value, right):
        self.key  = key
        self.value = value
        self.left = left
        self.right = right

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_value(self, value):
        self.value = value

    def set_key(self, key):
        self.key = key

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __repr__(self):
        return str(self.key) + ", v=" + str(self.value) + ", l=[" + str(self.left) + "], r=[" + str(self.right) + "]"

def main():
    root = TreeNode(None, 40, 40, None)
    l1 = TreeNode(None, 35, 35, None)
    l2 = TreeNode(None, 30, 30, None)
    r1 = TreeNode(None, 45, 45, None)
    r2 = TreeNode(None, 51, 51, None)

    print(root)
    print(l1)

if __name__ == "__main__":
    main()