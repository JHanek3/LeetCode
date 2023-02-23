import collections
"""
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""
def preorder(root):
    
    if not root:
        return []

    # Recursive
    # output = []
    # def dfs(node):
    #     if not node:
    #         return
    #     output.append(node.val)

    #     for c in node.children:
    #         dfs(c)
    # dfs(root)
    # return output

    # Iteratively, q/stack
    stack = collections.deque([root])
    output = []

    while stack:
        cand = stack.popleft()
        output.append(cand.val)
        for c in reversed(cand.children):
            stack.appendleft(c)
    
    return output
"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    d = collections.defaultdict(list)

    def dfs(node, level):
        if not node:
            return
        d[level].append(node.val)
        dfs(node.left, level+1)
        dfs(node.right, level+1)
    
    dfs(root,0)
    return d.values()
