# Problem: Binary Tree Inorder Traversal (LeetCode #94)
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        total = []
        
        def inorder(node):
            if node:  
                inorder(node.left)
                total.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return total
        