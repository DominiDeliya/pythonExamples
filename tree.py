input_arr = ["4", "1", "5", "2", "#", "#", "#"]
output_arr = []


class Node(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def create(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp

        root.left = create(arr, root.left, 2 * i + 1, n)
        root.right = create(arr, root.right, 2 * i + 2, n)

        return root


def preorder(root):
    if root is None or root.value == "#":
        return

    output_arr.append(root.value)
    preorder(root.left)
    preorder(root.right)


n = len(input_arr)
root = None
root = create(input_arr, root, 0, n)
preorder(root)

print(" ".join(output_arr))

# Algorithm Preorder(tree)
#    1. Visit the root.
#    2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#    3. Traverse the right subtree, i.e., call Preorder(right-subtree)
