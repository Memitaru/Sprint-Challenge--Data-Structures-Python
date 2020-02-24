class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # is there already a value at self.left
            # if there is no self.left value
            if not self.left:
                # set the new left child to a new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node is the target value, we found the value
        if self.value == target:
            return True
        # target is smaller, go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)