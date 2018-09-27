#https://en.wikipedia.org/wiki/Binary_search_tree
#Vijayarajan Govindarajan 2018
import random
from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)

    def is_empty(self):
        return True if self.root is None else False

    def add(self, key):
        self.root = add_node(self.root, key, key)
        return

    def has_key(self, key):
        return has_key(self.root, key)

    def get_value(self, key):
        return get_value(self.root, key)

    def remove_key(self, key):
        if self.has_key(key):
            node = remove_node(self.root, key)
            return node


def add_node(root, key, value):
    if root is None:
        root = TreeNode(None, key, value, None)
        return root

    if root.get_key() == key:
        old_node = root
        new_node = TreeNode(root.get_left(), key, value, root.get_right())
        root = new_node
        return root

    if root.get_key() < key:
        new_node = root.get_right()
        if new_node is None:
            new_node = TreeNode(None, key, value, None)
            root.set_right(new_node)
        else:
            add_node(new_node,key,value)
        return root

    if root.get_key() > key:
        new_node = root.get_left()
        if new_node is None:
            new_node = TreeNode(None, key, value, None)
            root.set_left(new_node)
        else:
            add_node(new_node, key,value)
        return root


def has_key(root, key):
    if root is None:
        return False

    if root.get_key() == key:
        return True

    if root.get_key() < key:
        new_node = root.get_right()
        return has_key(new_node, key)

    if root.get_key() > key:
        new_node = root.get_left()
        return has_key(new_node, key)

    return False


def get_node(root, key):
    if root is None:
        return None

    if root.get_key() == key:
        return root

    if root.get_key() < key:
        new_node = root.get_right()
        return get_node(new_node, key)

    if root.get_key() > key:
        new_node = root.get_left()
        return get_node(new_node, key)

    return None


def get_value(root, key):
    node = get_node(root, key)
    if node is not None:
        return node.get_value()
    return None

def remove_node_with_no_children(root,key):
    if root is None:
        return None
    node = root

    while node:
        node_key = node.get_key()
        if node_key == key:
            if node.get_left() is None and node.get_right() is None:
                removed_node = node
                node = None
                return removed_node
            else:
                raise LookupError()

        if node_key > key:
            if node.get_left() is not None:
                left_node = node.get_left()
                node = left_node
                continue
            else:
                raise LookupError()

        if node_key < key:
            if node.get_right() is not None:
                right_node = node.get_right()
                node = right_node
                continue
            else:
                raise LookupError()
    return None


def remove_node_with_one_child(root,key):
    if root is None:
        return None
    parent = root
    node = root

    while node:
        left_node = None
        right_node = None

        if node.get_left() is not None:
            left_node = node.get_left()
        if node.get_right() is not None:
            right_node = node.get_right()

        if node.get_key() == key:
            if left_node is not None and right_node is not None:
                raise LookupError()
            if left_node is None and right_node is None:
                raise LookupError()
            child_node = left_node if not None else right_node

            #special handling for root node
            if node.get_key() == parent.get_key():
                parent = child_node
                root = child_node
                return node
            else:
                if parent.get_left() is not None and parent.get_left().get_key() == node.get_key():
                    parent.set_left(child_node)
                    return node
                if parent.get_right() is not None and parent.get_right().get_key() == node.get_key():
                    parent.set_right(child_node)
                    return node

        if node.get_key() > key:
            if left_node is None:
                raise LookupError()
            child_node = left_node
            parent = node
            node = child_node
            continue

        if node.get_key() < key:
            if right_node is None:
                raise LookupError()
            child_node = right_node
            parent = node
            node = child_node
            continue
    return None

def remove_node_with_two_children(root,key):
    return None

def remove_node(root, key):
    if not has_key(root,key):
        return None
    node = get_node(root,key)

    if node is None:
        raise LookupError()

    if node.get_left() is None and node.get_right() is None:
        removed_node = remove_node_with_no_children(root,key)
        return removed_node

    if node.get_left() is not None and node.get_right() is not None:
        removed_node = remove_node_with_two_children(root,key)
        return removed_node
    if node.get_left() is not None or node.get_right() is not None:
        removed_node = remove_node_with_one_child(root,key)
        return removed_node

    return None



def pre_order_walk(root):
    if root is None:
        return
    pre_order_walk(root.get_left())
    pre_order_walk(root.get_right())
    print(root.get_value())
    return


def in_order_walk(root):
    if root is None:
        return
    in_order_walk(root.get_left())
    print(root.get_value())
    in_order_walk(root.get_right())
    return


def basic_test():
    bst = BinarySearchTree()
    bst.add(40)
    bst.add(35)
    bst.add(50)
    bst.add(38)
    bst.add(39)

    print(bst)
    print("In order Walk")
    in_order_walk(bst.root)

    print("has key 40")
    print(bst.has_key(40))
    print(bst.get_value(40))

    print("has key 41")
    print(bst.has_key(41))
    print(bst.get_value(41))

    print("remove key 39")
    removed_node = bst.remove_key(39)
    print(removed_node)
    print(bst)

    #removed_node = bst.remove_key(35)
    #print(removed_node)

    #print(bst)

def random_add():
    bst = BinarySearchTree()
    for i in range(1,100,1):
        rand = random.randrange(0, 1000)
        bst.add(rand)
    print(bst)
    in_order_walk(bst.root)

def main():
    basic_test()

if __name__ == "__main__":
    main()