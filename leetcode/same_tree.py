"""Given two binary trees, write a function to check 
if they are the same or not.
Two binary trees are considered the same if 
they are structurally identical
 and the nodes have the same value."""

#O(N) time complexity because it has to traverse both trees, every data point in order
# to verify that the trees are the same (or not)

class Node(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None
class Solution():

    def same_tree(self,a:Node,z:Node):
        if a is None and z is None:
            return True
        if a is not None and z is not None:
            if a.data == z.data:
                return self.same_tree(a.left,z.left) and self.same_tree(a.right,z.right)
        return False
solution = Solution()
a = Node(1)
z = Node(1)
a.left = Node(2)
z.left = Node(2)
a.right = Node(3)
z.right = Node(4)

print(solution.same_tree(a,z))

    



    

