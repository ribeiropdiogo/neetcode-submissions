class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Iterate word
        for c in word:
            # Calculate index
            index = ord(c) - ord('a')
            # Check if index has Node
            if cur.children[index] is None:
                # Initialize node
                cur.children[index] = TrieNode()
            # Move pointer
            cur = cur.children[index]
        # Mark end of word
        cur.isEndOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        # Iterate word
        for c in word:
            # Calculate index
            index = ord(c) - ord('a')
            # Check if index has Node
            if cur.children[index] is None:
                return False
            # Move pointer
            cur = cur.children[index]
        return cur.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        # Iterate prefix
        for c in prefix:
            # Calculate index
            index = ord(c) - ord('a')
            # Check if index has Node
            if cur.children[index] is None:
                return False
            # Move pointer
            cur = cur.children[index]
        return True

        
        