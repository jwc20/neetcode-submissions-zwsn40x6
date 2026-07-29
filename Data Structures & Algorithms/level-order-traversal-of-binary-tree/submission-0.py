from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        q = deque()
        q.append(root)

        while q:
            level_size = len(q)
            curr_level = []
            
            for _ in range(level_size):
                curr_node = q.popleft()
                curr_level.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left)

                if curr_node.right:
                    q.append(curr_node.right)
            result.append(curr_level)
        return result