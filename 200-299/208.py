class TrieNode:
    def __init__(self, description=None) -> None:
        self.children: dict[str, TrieNode] = {}
        self.endOfWord: bool = False
        self.description = description


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str, description: str = None) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfWord = True
        current.description = description

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))

# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
