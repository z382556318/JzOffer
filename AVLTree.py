import binary_sort_tree

class AVLBiTNode():
    def __init__(self, data, lchild = None, rchild = None):
        self.val = data
        self.lchild = lchild
        self.rchild = rchild
        self.bf = 0

class AVLTree(BinarySortTree):
    def insert(self, key):
