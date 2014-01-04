#!/usr/bin/env python
#
## Binary Search Trees:
#
# A binary search tree is represented by a linked data structure in
# which each nodes is an object. In addition to a key and satellite
# data, each node contains attribute left, right, and p that point to
# the nodes corresponding to its left child, its right child, and its
# parent, respectively. The keys in a binary search tree are always
# stored in such a way as to satisfy the binary-search-tree property:
#
#   Let x be a node in a binary search tree. If y is a node in the
#   left subtree of x, then y.key <= x.key. If y is a node in the
#   right subtree of x, then y.key >= x.key.
#
# An inorder tree walk allows us to recursively print out all the keys
# in a binary search tree by printing the root of a subtree between
# printing the left and right subtree values. A preorder tree walk
# prints the root before the values in either subtree, and a postorder
# tree walk prints the root after the values in its subtrees.
#
## Operations:
#
# SEARCH, MINIMUM, MAXIMUM, PREDECESSOR, SUCCESSOR, INSERT, DELETE
#
## Performance:
#
# Worst case search performance:       O(n)
# Best case search performance:        O(log n)
# Average case search performance:     O(log n)
#
## Disadvantages:
#
# If constructed from ordered data, it essentially becomes a linked
#  list, with O(n) searching performance.
#
## References:
#
# Introduction to Algorithms, section 12.1, page 287.
# http://stackoverflow.com/a/5444796
#
## Code:
#
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key

    def insert(self, n):
        if n.key < self.key:
            if self.left:
                self.left.insert(n)
            else:
                self.left = n
                n.p = self
        else:
            if self.right:
                self.right.insert(n)
            else:
                self.right = n
                n.p = self

    def search(self, key):
        if self.key == key:
            return self
        if key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        else:
            return Node(None) # Return a null node

    # Follow the left child pointers from the root until we encounter
    # a nil:
    def minimum(self):
        if self.left != None:
            return self.left.minimum()
        else:
            return self

    # Follow the right child pointers from the root until we encounter
    # a nil:
    def maximum(self):
        if self.right != None:
            return self.right.maximum()
        else:
            return self

    def successor(self):
        if self.right:
            return self.right.minimum()

        if self.p and self == self.p.right:
            return self.p.successor()
        else:
            return self.p

    def _transplant(self, n):
        if not self.p:
            self = n
        elif self == self.p.left:
            self.p.left = n
        else:
            self.p.right = n

        if n:
            n.p = self.p

    def delete(self, n):
        if not n.left:
            n._transplant(n.right)
        elif not n.right:
            n._transplant(n.left)
        else:
            y = n.right.minimum()
            if y.p != n:
                y._transplant(y.right)
                y.right = n.right
                y.right.p = y
            n._transplant(y)
            y.left = n.left
            y.left.p = y

    def inorder_tree_walk(self):
        if self.left:
            self.left.inorder_tree_walk()

        print self.key

        if self.right:
            self.right.inorder_tree_walk()

    def preorder_tree_walk(self):
        print self.key

        if self.left:
            print self.left.preorder_tree_walk()

        if self.right:
            print self.right.preorder_tree_walk()

    def postorder_tree_walk(self):
        if self.left:
            print self.left.preorder_tree_walk()

        if self.right:
            print self.right.preorder_tree_walk()

        print self.key

## Iterative implementations of tree functions:

def tree_insert(tree, n):
    y = None
    x = tree
    while x != None:
        y = x
        if n.key < x.key:
            x = x.left
        else:
            x = x.right
    n.p = y
    if not y:
        tree = n
    elif n.key < y.key:
        y.left = n
    else:
        y.right = n

# An iterative tree search, achieved by unrolling the recursion in
# Node.search() into a while loop. Again, if the key is key is not
# found within the tree, a null node is returned.
def tree_search(node, key):
    while key != node.key:
        if key < node.key:
            node = node.left
        else:
            node = node.right

        if node == None:
            return Node(None)
    return node

def tree_minimum(node):
    while node.left != None:
        node = node.left
    return node

def tree_maximum(node):
    while node.right != None:
        node = node.right
    return node

def tree_successor(node):
    if node.right:
        return tree_minimum(node.right)
    parent = node.p
    while parent and node == parent.right:
        node = parent
        parent = parent.p
    return parent

def tree_transplant(tree, u, v):
    if not u.p:
        # If u is the tree root:
        tree = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v

    if v:
        v.p = u.p

def tree_delete(tree, z):
    if not z.left:
        tree_transplant(tree, z, z.right)
    elif not z.right:
        tree_transplant(tree, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            tree_transplant(tree, y, y.right)
            y.right = z.right
            y.ripht.p = y
        tree_transplant(tree, z, y)
        y.left = z.left
        y.left.p = y

if __name__ == "__main__":
    tree = Node(3)
    tree.insert(Node(1))
    tree.insert(Node(2))
    tree.insert(Node(5))
    tree.insert(Node(12))
    tree_insert(tree, Node(9))
    tree_insert(tree, Node(12))
    tree_insert(tree, Node(12))
    tree_insert(tree, Node(6))

    print "Inorder tree walk:"
    print tree.inorder_tree_walk()

    print "\nPreorder tree walk:"
    tree.preorder_tree_walk()

    print "\nPostorder tree walk:"
    tree.postorder_tree_walk()

    print "\nSearch:", tree.search(6).key, tree.search(7).key
    print "Search:", tree_search(tree, 6).key, tree_search(tree, 7).key
    print "Minimum:", tree.minimum().key, tree_minimum(tree).key
    print "Maximum:", tree.maximum().key, tree_maximum(tree).key
    print "Successor:", tree_successor(tree).key, tree.successor().key
    node = tree.search(6)
    print "Successor:", tree_successor(node).key, node.successor().key

    print "\nDelete 2:"
    tree_delete(tree, tree.search(2))
    tree.inorder_tree_walk()

    print "\nDelete 9:"
    tree.delete(tree.search(9))
    tree.inorder_tree_walk()

    print "\nDelete 12:"
    tree.delete(tree.search(12))
    tree.inorder_tree_walk()

    print "\nDelete 1:"
    tree_delete(tree, tree)
    tree.inorder_tree_walk()
