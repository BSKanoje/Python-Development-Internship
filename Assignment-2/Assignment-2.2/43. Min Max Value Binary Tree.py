from collections import deque
 
def largest_node_binary_tree(root):
    queue=deque([root])
    max_node=0

    while queue:
        curr_node=queue.popleft()
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)    

        if curr_node.val >max_node:
            max_node=curr_node.val
    return max_node            