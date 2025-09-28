from typing import Dict, List


class Trie:
    
    def __init__(self):
        self.root: Dict[str, Trie] = dict()
        self.word = None
    
    def add(self, word, i=0):
        if len(word) == i:
            self.word = word
            return
        ch = word[i]
        self.root[ch] = self.root.get(ch, Trie())
        self.root[ch].add(word, i+1)
    
    def search(self, word, i=0, ret:List[str]=[]):
        if len(ret) == 3:
            return ret
        if i < len(word):
            if self.root.get(word[i], None) is not None:
                return self.root[word[i]].search(word, i+1, ret)
            else:
                return ret

        if self.word:
            ret.append(self.word)
        for _, value in sorted(self.root.items(), key=lambda x: x[0]):
            ret = value.search(word, i+1, ret)
            if len(ret) == 3:
                return ret
        return ret


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        t = Trie()
        for product in products:
            t.add(product)
        ans = []
        for i in range(1, len(searchWord)+1):
            cur_word = searchWord[:i]
            ans.append(t.search(cur_word, ret=[])[:])
        return ans

# print(
#     Solution().suggestedProducts(
#         products=["mobile","mouse","moneypot","monitor","mousepad"],
#         searchWord="mouse"
#     )
# )
Solution().suggestedProducts(
    ["code","codephone","coddle","coddles","codes"],
    "coddle",
)