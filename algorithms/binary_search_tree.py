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
    def keys(self):
        keyList = []
        return get_keys(self.root, keyList)

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

    if root.get_key() is None:
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
    parent = root

    while node:
        node_key = node.get_key()
        if node_key == key:
            if node.get_left() is None and node.get_right() is None:
                removed_node = node
                if parent == root and node == root:
                    root = None
                else:
                    if parent.get_left() is not None and parent.get_left().get_key() == node_key:
                       parent.set_left(None)
                    if parent.get_right() is not None and parent.get_right().get_key() == node_key:
                       parent.set_right(None)
                node = None
                return removed_node
            else:
                raise LookupError()

        if node_key > key:
            if node.get_left() is not None:
                left_node = node.get_left()
                parent = node
                node = left_node
                continue
            else:
                raise LookupError()

        if node_key < key:
            if node.get_right() is not None:
                right_node = node.get_right()
                parent = node
                node = right_node
                continue
            else:
                raise LookupError()
    return None

def remove_node_with_one_child(root,key):
    if root is None:
        return None
    node = root
    parent = root

    while node:
        left_node = node.get_left()
        right_node = node.get_right()
        node_key = node.get_key()

        if node_key == key:
            if left_node is None and right_node is None:
                raise LookupError()
            if left_node is not None and right_node is not None:
                raise LookupError()
            if left_node is None or right_node is None:
                child_node = left_node if left_node is not None else right_node
                removed_node = node
                if parent == root and node == root:
                    root = child_node
                else:
                    if parent.get_left() is not None and parent.get_left().get_key() == node_key:
                        parent.set_left(child_node)
                        #print(child_node)
                    if parent.get_right() is not None and parent.get_right().get_key() == node_key:
                        parent.set_right(child_node)
                        #print(child_node)
                node = None
                return removed_node
            else:
                raise LookupError()

        if node_key > key:
            if node.get_left() is not None:
                left_node = node.get_left()
                parent = node
                node = left_node
                continue
            else:
                raise LookupError()

        if node_key < key:
            if node.get_right() is not None:
                right_node = node.get_right()
                parent = node
                node = right_node
                continue
            else:
                raise LookupError()
    return None

def remove_node_with_two_children(root,key):
    if root is None:
        return None
    node = root
    parent = root

    while node:
        left_node = node.get_left()
        right_node = node.get_right()
        node_key = node.get_key()

        if node_key == key:
            if left_node is None or right_node is None:
                raise LookupError()
            if left_node is not None and right_node is not None:
                child_node = get_minimal_left_node(node.get_right())
                copy_of_child_node = TreeNode(child_node.get_left(), child_node.get_key(), child_node.get_value(), child_node.get_right())
                #Delete the child node first
                removed_child_node = remove_node(node, child_node.get_key())
                removed_node = node
                node_to_place = TreeNode(node.get_left(), copy_of_child_node.get_key(), copy_of_child_node.get_value(), node.get_right())
                if parent == root and node == root:
                    root = node_to_place
                else:
                    if parent.get_left() is not None and parent.get_left().get_key() == node_key:
                        parent.set_left(node_to_place)
                        #print(child_node)
                    if parent.get_right() is not None and parent.get_right().get_key() == node_key:
                        parent.set_right(node_to_place)
                        #print(child_node)
                node = None
                return removed_node
            else:
                raise LookupError()

        if node_key > key:
            if node.get_left() is not None:
                left_node = node.get_left()
                parent = node
                node = left_node
                continue
            else:
                raise LookupError()

        if node_key < key:
            if node.get_right() is not None:
                right_node = node.get_right()
                parent = node
                node = right_node
                continue
            else:
                raise LookupError()
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


def get_minimal_left_node(root):
    min_node = root
    while min_node.get_left():
        min_node = min_node.get_left()
    return min_node


def get_minimal_right_node(root):
    min_node = root
    while min_node.get_right():
        min_node = min_node.get_right()
    return min_node


def replace_node(current_node, child_node):
    if current_node is None:
        return None

    old_node = TreeNode(current_node.get_left(), current_node.get_key(), current_node.get_value(), current_node.get_right())

    left_child = None
    right_child = None
    child_key = None
    child_value = None
    if child_node is not None:
        left_child = child_node.get_left()
        right_child = child_node.get_right()
        child_key = child_node.get_key()
        child_value = child_node.get_value()

    current_node.set_left(left_child)
    current_node.set_right(right_child)
    current_node.set_key(child_key)
    current_node.set_value(child_value)
    return old_node

def replace_key_value(current_node, child_node):
    if current_node is None:
        return None

    old_node = TreeNode(current_node.get_left(), current_node.get_key(), current_node.get_value(), current_node.get_right())
    child_key = None
    child_value = None
    if child_node is not None:
        child_key = child_node.get_key()
        child_value = child_node.get_value()
    current_node.set_key(child_key)
    current_node.set_value(child_value)
    return old_node

def remove_node_minimal(node, key):
    if not node:
        return None

    if node and node.get_key():
        if node.get_key() < key:
            return remove_node_minimal(node.get_right(), key)
        if node.get_key() > key:
            return remove_node_minimal(node.get_left(), key)
        if node.get_key() == key:
            if node.get_left() is not None and node.get_right() is not None:
                min_left_node = get_minimal_left_node(node.get_right())
                removed_min_left_node = remove_node_minimal(min_left_node, min_left_node.get_key())
                current_node = replace_key_value(node, min_left_node)
                return current_node
            if node.get_left() is not None:
                current_node = replace_node(node, node.get_left())
                return current_node
            if node.get_right() is not None:
                current_node = replace_node(node, node.get_right())
                return current_node
            if node.get_left() is None and node.get_right() is None:
                current_node = replace_node(node, None)
                return current_node
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


def get_keys(root, keys):
    if root is None:
        return keys
    get_keys(root.get_left(), keys)
    keys.append(root.get_value())
    get_keys(root.get_right(),keys)
    return keys

def basic_test():
    bst = BinarySearchTree()
    bst.add(40)
    bst.add(35)
    bst.add(50)
    bst.add(38)
    bst.add(31)
    bst.add(32)
    bst.add(29)
    bst.add(39)
    bst.add(27)
    bst.add(51)
    bst.add(52)
    bst.add(53)

    print(bst)
    print("In order Walk")
    in_order_walk(bst.root)

    print("remove key 29")
    removed_node = bst.remove_key(29)
    print(removed_node)
    print(bst)

    print("remove key 51")
    removed_node = bst.remove_key(51)
    print(removed_node)
    print(bst)

    print("remove key 39")
    removed_node = bst.remove_key(39)
    print(removed_node)
    print(bst)

    print("remove key 27")
    removed_node = bst.remove_key(27)
    print(removed_node)
    print(bst)

    print("remove key 38")
    removed_node = bst.remove_key(38)
    print(removed_node)
    print(bst)

    print("remove key 40")
    removed_node = bst.remove_key(40)
    print(removed_node)
    print(bst)

    #print("remove key 52")
    #removed_node = bst.remove_key(52)
    #print(removed_node)
    #print(bst)

    #print("In order Walk")
    #in_order_walk(bst.root)

'''
    print("In order Walk")
    in_order_walk(bst.root)

    print("has key 40")
    print(bst.has_key(40))
    print(bst.get_value(40))

    print("has key 41")
    print(bst.has_key(41))
    print(bst.get_value(41))





    print("remove key 50")
    removed_node = bst.remove_key(50)
    print(removed_node)
    print(bst)
'''
    #print("remove key 35")
    #removed_node = bst.remove_key(35)
    #print(removed_node)
    #print(bst)

    #removed_node = bst.remove_key(35)
    #print(removed_node)

    #print(bst)

def random_add():
    bst = BinarySearchTree()
    for i in range(1,100,1):
        rand = random.randrange(0, 1000)
        bst.add(rand)
    print(bst)
    print(bst.keys())
    print("Start removal")
    for i in range(1,100,1):
        rand = random.randrange(0, 1000)
        #print("Remove ", rand)
        removed_node = bst.remove_key(rand)
        if removed_node:
            print(removed_node)
            print(bst)
    print("After removal")
    print(bst.keys())

def main():
    random_add()

if __name__ == "__main__":
    main()