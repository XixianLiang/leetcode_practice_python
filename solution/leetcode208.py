from typing import Dict


class TrieNode:
    def __init__(self, is_root=False):
        self.end = False
        self._next_dict:Dict[str, TrieNode] = dict()
        
    def insert(self, string):
        if len(string) == 0:
            self.end = True
            return
        
        prefix = string[0]
        next_string = string[1:]
        self._next_dict[prefix] = self._next_dict.get(prefix, TrieNode())
        self._next_dict[prefix].insert(next_string)
    
    def search(self, string, prefix_search=False):
        if len(string) == 0:
            return self.end if not prefix_search else True
        prefix = string[0]
        next_string = string[1:]
        if prefix not in self._next_dict.keys():
            return False
        return self._next_dict[prefix].search(next_string, prefix_search=prefix_search)
    

class Trie:

    def __init__(self):
        self._trie = TrieNode() 

    def insert(self, word: str) -> None:
        self._trie.insert(word)

    def search(self, word: str) -> bool:
        return self._trie.search(word, prefix_search=False)

    def startsWith(self, prefix: str) -> bool:
        return self._trie.search(prefix, prefix_search=True)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("a")
param_2 = obj.search("a")
param_3 = obj.startsWith("a")
print(param_2, param_3)