"""
1166. Design File System
Solved
Medium

Topics

Companies

Hint
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

2 <= path.length <= 100
1 <= value <= 109
Each path is valid and consists of lowercase English letters and '/'.
At most 104 calls in total will be made to createPath and get.
"""

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)


class FileSystem:
    """
    Variant 1:
    My first successful implementation of the FileSystem class for this problem. On
    average, this solution beats ~ 80% of accepted answers in terms of run time and
    ~20% of accepted answers in terms of space. This FileSystem object should have
    space complexity of O(n) where n is the total number of files and directories
    that were successfully created in this FileSystem object. This is essentially 
    the same as Approach 1: 'Dictionary for storing paths', except my implementation
    uses slightly different logic.
    """

    def __init__(self):
        self.lookup_table = {}

    def createPath(self, path: str, value: int) -> bool:
        """
        This method should have run time complexity of O(1).
        """
        # we need to check if parent path is in self.lookup_table
        parent_dir = "/".join(path.split("/")[:-1])
        if parent_dir in self.lookup_table or parent_dir == "":
            if path in self.lookup_table:
                return False
            else:
                self.lookup_table[path] = value
                return True    

    def get(self, path: str) -> int:
        """
        This method should have run time complexity of O(1).
        """
        if path in self.lookup_table:
            return self.lookup_table[path]
        else:
            return -1


class FileSystem:
    """
    Variant 2:
    This is the official solution for Approach 1: 'Dictionary for storing paths'
    given by leetcode. They call it 'pretty much a simulation-based approach ...
    because it doesn't use any fancy data-structure for storing the paths and pretty 
    much, we do what the problem asks us to do for both the functions. My first 
    successful implementation of the FileSystem class for this problem. On average, 
    this solution beats ~ 90% of accepted answers in terms of run time and ~40% of 
    accepted answers in terms of space. This FileSystem object should have space 
    complexity of O(n) where n is the total number of files and directories that were 
    successfully created in this FileSystem object. So if this uses the same strategy
    as Variant 1, why do the performance statistics suggest it is more efficient? Let's
    think about and list out reasons why this might be a better implementation of 
    Approach 1:
    
    - This implementation uses 'parent = path[:path.rfind('/')]' to determine the parent
    directory path which is likely more efficient than 
    'parent_dir = "/".join(path.split("/")[:-1])' which involves splitting the input path
    string, then slicing the resulting list, and then rejoining it with the same string
    split separator. That would explain the superior run time complexity.
    - 'defaultdict()' might be a more memory efficient way to construct a dictionary
    than the standard dictionary {}. Even though defaultdict() inherits from {} and has
    an additional attribute (thus using a tad more memory) on instantiation, it 
    automatically initializes new keys with a default value, which can be more 
    efficient when dealing with operations like counting or grouping.
    
    However, we are relying on leetcode reports which is not as accurate as measuring
    things ourselves with our own test cases. So if we wanted to be sure that this is a
    superior implementation of Approach 1 we could more thoroughly test that claim. 
    """
    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        
        # Step-1: basic path validations
        if path == "/" or len(path) == 0 or path in self.paths:
            return False
        
        # Step-2: if the parent doesn't exist. Note that "/" is a valid parent.
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False
        
        # Step-3: add this new path and return true.
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


class TrieNode(dict):
    
    def __init__(self, val):
        #self.rel_path = rel_path
        self.value = val


class FileSystem:
    """
    Variant 3: The following is my own first successful implementation of Approach 2:
    'Trie based approach' that leetcode provides. It uses the above custom class 
    TrieNode I defined which essentially is just a dictionary but with a value 
    attribute. I think the logic/implementation for the different methods of this
    FileSystem class could be cleaned up, but I just wanted to get something working
    and passing leetcode's test cases. In terms of run time efficiency, this solution
    beats about 60% of accepted answers and in terms of memory efficiency, only 6%. I
    would say that the run time efficiency for either createPath or get method isn't
    exactly constant time since both contain while loops that run while an accumulator
    variable is less than the depth of the input path, but it also isn't O(n). Though
    this approach is supposed to have better memory efficiency than the implementations
    of Approach 1, that's not what I'm observing. It's possible that the official
    solution provided by leetcode demonstrates superior memory efficiency, but my
    implementation certainly does not.
    """
    def __init__(self):
        self.root = TrieNode(1)

    def createPath(self, path: str, value: int) -> bool:
        path_nodes = path.split("/")
        curr = self.root
        index = 1
        # first check to see if all ancestors exist
        while index < len(path_nodes) - 1:
            if path_nodes[index] in curr:
                curr = curr[path_nodes[index]]
                index += 1
            else:
                return False
        
        if path_nodes[-1] in curr:
            return False
        curr[path_nodes[-1]] = TrieNode(value)
        return True

    def get(self, path: str) -> int:
        path_nodes = path.split("/")
        curr = self.root
        index = 1
        if path == "":
            return curr.value
        elif len(path_nodes) < 3:
            if path_nodes[-1] in curr:
                return curr[path_nodes[-1]].value
            else:
                return -1
        # first check to see if all ancestors exist
        while index < len(path_nodes) - 1:
            if path_nodes[index] in curr:
                curr = curr[path_nodes[index]]
                index += 1
            else:
                return -1
        
        if path_nodes[-1] in curr:
            return curr[path_nodes[-1]].value
        else:
            return -1


# The TrieNode data structure.
class TrieNode(object):
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name = name
        self.value = -1

class FileSystem:
    """
    Variant 4:
    This is the official solution for Approach 2: 'Trie based approach' given by leet.
    This particular implementation beats ~40% of accepted answers in terms of run time
    complexity and ~6% of accepted answers in terms of memory efficiency. So it seems
    as though my implementation of this particular approach (Variant 3) is slightly
    better in terms of run time complexity. But why might that be?

    The main difference between this implementation and mine is that the TrieNode
    class I defined inherits from dictionary and only has one extra attribute whereas
    this implementation treats the dictionary used to store the node relationships as
    an attribute of a more generically defined TrieNode object, which also has a name
    in addition to a value attribute. Thus accessing a given TrieNode object along the
    input path's branch which this FileSystem's 'createPath' and 'get' methods require 
    entails looking up the TrieNode's map attribute and then an additional lookup of
    the next node object from the FileSystem.map dictionary using the relative path of
    that next node. Basically, assigning the next tree node to 'cur' requires two
    lookups, not one. This could possibly explain why this implementation appears to be
    more slow than Variant 3. Leetcode analyzed this approach to have O(n) complexity
    in both time and space. 
    """
    def __init__(self):
        
        # Root node contains the empty string.
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        
        # Obtain all the components
        components = path.split("/")
        
        # Start "curr" from the root node.
        cur = self.root
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            name = components[i]
            
            # For each component, we check if it exists in the current node's dictionary.
            if name not in cur.map:
                
                # If it doesn't and it is the last node, add it to the Trie.
                if i == len(components) - 1:
                    cur.map[name] = TrieNode(name)
                else:
                    return False
            cur = cur.map[name]
        
        # Value not equal to -1 means the path already exists in the trie. 
        if cur.value!=-1:
            return False
        
        cur.value = value
        return True

    def get(self, path: str) -> int:
        
        # Obtain all the components
        cur = self.root
        
        # Start "curr" from the root node.
        components = path.split("/")
        
        # Iterate over all the components.
        for i in range(1, len(components)):
            
            # For each component, we check if it exists in the current node's dictionary.
            name = components[i]
            if name not in cur.map:
                return -1
            cur = cur.map[name]
        return cur.value






