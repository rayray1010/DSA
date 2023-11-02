class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # WRITE KTH_SMALLEST METHOD HERE #
    # def kth_smallest(self, k):
    #     self.kth_smallest_count = 0
    #     return self.kth_smallest_helper(self.root, k)

    # def kth_smallest_helper(self, node, k):
    #     if node is None:
    #         return None

    #     left_result = self.kth_smallest_helper(node.left, k)
    #     if left_result is not None:
    #         return left_result

    #     self.kth_smallest_count += 1
    #     if self.kth_smallest_count == k:
    #         return node.value

    #     right_result = self.kth_smallest_helper(node.right, k)
    #     if right_result is not None:
    #         return right_result

    #     return None
    def kth_smallest(self, k):
        self.smallest_count = 0
        return self.kth_helper(self.root, k)

    def kth_helper(self, node, k):
        if node is None:
            return None
        left_result = self.kth_helper(node.left, k)
        self.smallest_count += 1
        if self.smallest_count == k:
            return node.value
        right_result = self.kth_helper(node.right, k)

        if left_result is not None:
            return left_result
        if right_result is not None:
            return right_result
        return None


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """
