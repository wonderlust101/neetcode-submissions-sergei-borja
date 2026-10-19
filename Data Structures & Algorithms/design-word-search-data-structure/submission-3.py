class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            # If reached the end of the word
            if i == len(word):
                return node.is_end
            
            char = word[i]

            # If the char indicates to try all branches
            if char == ".":
                for child in node.children.values():
                    # Check if atleast one branch works
                    if dfs(child, i + 1):
                        return True
                return False
            
            # If the branch does not have letter
            if char not in node.children:
                return False
            
            return dfs(node.children[char], i + 1)
        
        return dfs(self.root,0)
            