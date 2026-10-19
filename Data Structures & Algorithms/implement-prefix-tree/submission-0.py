class TrieNode:
    def __init__(self):
        self.children = {} # {A: TrieNode()}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root # Start at root

        
        for char in word:
            # Builds the branch
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            # Moves down the branch
            curr = curr.children[char]
        
        curr.is_end = True
    
    def _traverse(self, word:str) -> TrieNode:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        
        return curr

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None
        