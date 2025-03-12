class Trie:
    def __init__(self) -> None:
        self.isEndOfWord = False
        self.map = {}

def insert(root, word):
    temp = root 
    for i in range(len(word)): 
        x = word[i] 

        # If there is no path then make a new node 
        if x not in temp.map: 
            temp.map[x] = Trie() 

        temp = temp.map[x] 

    # Mark end of word and store the meaning 
    temp.isEndOfWord = True
        
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = Trie()
        for word in dictionary:
            insert(root, word)

        for i in root.map.items():
            print(i)

        for word in sentence:
            pass
        
        return None
    
dictionary = ["cat", "rat", "bat", "brat"]
sentence = "bla bla bla"
s = Solution()
s.replaceWords(dictionary, sentence)
