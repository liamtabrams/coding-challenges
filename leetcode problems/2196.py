# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Variant 1:
    My first successful attempt at reproducing Approach 1: 'Convert to Graph with 
    Breadth First Search' provided by leetcode. However, I don't think it is an
    optimized implementation of this approach since the official solution provided
    by leet beat about 20% of accepted solutions while mine only beat out 5% :( .
    Still, you have to crawl before you can walk. Also, in terms of space complexity
    this solution beat almost 96% of accepted answers. I am guessing that the run time 
    complexity of this implementation is O(n^2), since 'children' is not sorted 
    (searching through it could take up to n-1 tries, where n is the number of nodes
    or elements in 'descriptions') and we could have close to n parents in our 
    dictionary as well - making the dominant term the block that searches for the root 
    of the tree (aka the parent that is not a child). I'm also guessing that the space 
    complexity is O(n). However, leetcode claims that both the run time and space 
    complexity of this solution is O(n).
    """
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent_info_dict = {}
        children = []
        for d in descriptions:
            parent, child, is_left = d
            children.append(child)
            if parent not in parent_info_dict:
                parent_info_dict[parent] = [[child, is_left]]
            else:
                parent_info_dict[parent].append([child, is_left])
        node_queue = []
        for parent in parent_info_dict:
            if parent not in children:
                root_val = parent
                break
        
        root = TreeNode(root_val)
        node_queue.append(root)

        while node_queue:
            node = node_queue.pop(0)
            if node.val in parent_info_dict:
                for info in parent_info_dict[node.val]:
                    child = TreeNode(info[0])
                    if info[1]:
                        node.left = child
                    else:
                        node.right = child
                    node_queue.append(child)
        
        return root


class Solution:
    """
    Variant 2:
    This is the official solution given by leetcode for Approach 1: 'Convert to Graph
    with Breadth First Search'. It is slightly more efficient in terms of run time, but
    substantially less efficient in terms of memory, than my implementation above of 
    the same approach. Why is it more efficient in terms of run time? I believe the 
    primary reason is that instead of using a list to store children, we use a set,
    which is based on a hash table and thus for each parent we have a lookup time
    complexity of O(1) rather than O(n), in the code block where we remove children
    from the parents set in order to then identify the value of the root node. Why is
    this implementation of this approach less efficient in terms of space than mine? 
    Well, we are using an additional set that we don't need in order to store the
    parent values, rather than looking them up in the parentToChildren dictionary.
    Overall though, leetcode claims that the time and space complexity for this 
    implementation is the same as those for mine above - O(n) for both.
    """ 
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Sets to track unique children and parents
        children = set()
        parents = set()
        # Dictionary to store parent to children relationships
        parentToChildren = {}

        # Build graph from parent to child, and add nodes to sets
        for d in descriptions:
            parent, child, isLeft = d
            parents.add(parent)
            parents.add(child)
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = []
            parentToChildren[parent].append((child, isLeft))

        # Find the root node by checking which node is
        # in parents but not in children
        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        root = TreeNode(next(iter(parents)))

        # Starting from root, use BFS to construct binary tree
        queue = deque([root])

        while queue:
            parent = queue.popleft()
            # Iterate over children of current parent
            for childValue, isLeft in parentToChildren.get(parent.val, []):
                child = TreeNode(childValue)
                queue.append(child)
                # Attach child node to its parent based on isLeft flag
                if isLeft == 1:
                    parent.left = child
                else:
                    parent.right = child

        return root


class Solution:
    """
    Variant 3:
    My own successful implementation of Approach 2: 'Convert to Graph with Depth First 
    Search' given by leetcode. It is a better solution in terms of run time complexity
    but weaker in terms of memory efficiency, compared to Variant 2. It does not use a
    queue or parent set but the additional overhead from the recursive function calls 
    may add memory complexity compared to the iterative approach used in the BFS-based
    solution. I'm guessing that the recursive calls are more conducive to a slightly
    faster runtime compared to the queue-based iterative approach. Still, the overall
    run time and space complexity are the same as Approach 1 - both O(n).  
    """
    def create_child_node(self, parent_node, val, is_left, parentToChildren):
        if val:
            child_node = TreeNode(val)
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            for childValue, isLeft in parentToChildren.get(val, []): 
                self.create_child_node(child_node, childValue, isLeft, parentToChildren)
        else:
            return
    
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Sets to track unique children and parents
        children = set()
        # Dictionary to store parent to children relationships
        parentToChildren = {}

        # Build graph from parent to child, and add nodes to sets
        for d in descriptions:
            parent, child, isLeft = d
            children.add(child)
            if parent not in parentToChildren:
                parentToChildren[parent] = []
            parentToChildren[parent].append((child, isLeft))

        # Find the root node by checking which node is
        # in parents but not in children
        for parent in parentToChildren:
            if parent not in children:
                root_val = parent
                break

        root = TreeNode(root_val)
        for childValue, isLeft in parentToChildren.get(root_val, []):
            self.create_child_node(root, childValue, isLeft, parentToChildren)

        return root


class Solution:
    """
    Variant 4:
    This is the official implementation of Approach 2: 'Convert to Graph with Depth 
    First Search' given by leetcode. It turns out that my above implementation of
    this approach is superior in both run time and spatial complexity. First off, I
    do not build an all_nodes set. Also, (I believe) the way I find the root_val is 
    technically more efficient in terms of run time, since it won't always be necessary 
    to iterate over the whole parent set to find which parent is not a child. These 
    considerations I think explain why Variant 3 is more efficient in terms of both run
    time and memory required. Still, the overall run time and space complexity are the 
    same as Variant 3 - both O(n). This looks like the least efficient way to solve the
    problem at hand given the performance report indicates that it only beats about 5%
    of accepted answers in both time and memory efficiency.  
    """
   def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Step 1: Organize data
        parent_to_children = {}
        all_nodes = set()
        children = set()

        for parent, child, is_left in descriptions:
            # Store child information under parent node
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)

        # Step 2: Find the root
        root_val = (all_nodes - children).pop()

        # Step 3 & 4: Build the tree using DFS
        def _dfs(val):
            # Create new TreeNode for current value
            node = TreeNode(val)

            # If current node has children, recursively build them
            if val in parent_to_children:
                for child, is_left in parent_to_children[val]:
                    # Attach child node based on is_left flag
                    if is_left:
                        node.left = _dfs(child)
                    else:
                        node.right = _dfs(child)
            return node

        return _dfs(root_val)


class Solution:
    """
    Variant 5:
    The following is my successful attempt at reproducing Approach 3: 'Constructing 
    Tree From Direct Map and TreeNode Object' provided by leetcode. This solution is
    vastly superior to Variants 1-4 in terms of time efficiency and is superior in
    terms of memory efficiency to Variants 2-4 but not 1, via comparing the performance
    reports from the different variants. This approach is much more efficient time-wise
    because we do not need to perform either BFS or DFS which requires either for loop
    or recursive function calls. Instead, we create the tree directly from the nodeMap
    that we create from just iterating over the input list, and all we have to do then
    is just return the root of the tree. So we still use 1 dictionary and 1 set data
    structure in this solution, however we are able to generate the tree structure in
    the same for loop with which we traverse 'descriptions', rather than doing that in a
    separate code block. Leetcode analyzes this implementation to still have O(n)
    complexity in both time and space, however it is still the best choice of 
    implementation we have seen so far.  
    """
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodeMap = {}
        children = set()
        for d in descriptions:
            parent, child, is_left = d
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            if is_left:
                nodeMap[parent].left = nodeMap[child]
            else:
                nodeMap[parent].right = nodeMap[child]
            children.add(child)

        for node in nodeMap:
            if node not in children:
                root = nodeMap[node]
                break

        return root


class Solution:
    """
    Variant 6:
    The official solution for Approach 3: 'Constructing Tree From Direct Map and 
    TreeNode Object' given by leetcode. This implementation is very close to Variant 5-
    and displays very close performance to it in terms of both run time and memory 
    efficiency. More rigorous testing would be needed to make a determination about
    which is actually better. This version actually iterates over the nodeMap values,
    and then checks if an element of nodeMap.values has .val attribute that is in the
    children set. I think this might add SLIGHTLY more run time to this implementation
    as compared to Variant 5, but I'm not certain. As expected, Leetcode analyzes this 
    implementation to have O(n) complexity in both time and space.
    """
    def createBinaryTree(
        self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        # Maps values to TreeNode pointers
        node_map = {}

        # Stores values which are children in the descriptions
        children = set()

        # Iterate through description to create nodes and set up tree structure
        for description in descriptions:
            # Extract parent value, child value, and whether
            # it is a left child (1) or right child (0)
            parent_value = description[0]
            child_value = description[1]
            is_left = bool(description[2])

            # Create parent and child nodes if not already created
            if parent_value not in node_map:
                node_map[parent_value] = TreeNode(parent_value)
            if child_value not in node_map:
                node_map[child_value] = TreeNode(child_value)

            # Attach child node to parent's left or right branch
            if is_left:
                node_map[parent_value].left = node_map[child_value]
            else:
                node_map[parent_value].right = node_map[child_value]

            # Mark child as a child in the set
            children.add(child_value)

        # Find and return the root node
        for node in node_map.values():
            if node.val not in children:
                return node  # Root node found

        return None  # Should not occur according to problem statement





