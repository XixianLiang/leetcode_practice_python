from typing import List, Dict

class Trie:
    
    def __init__(self):
        self.root:Dict[str, Trie] = dict()
        self.end = False
        self.cur_word = None
    
    def add(self, word, depth=0):
        if len(word) == depth:
            self.end = True
            self.cur_word = word
            return
        ch = word[depth]
        self.root[ch] = self.root.get(ch, Trie())
        self.root[ch].add(word, depth+1)
    
    def search(self, word):
        if len(word) == 0:
            return self.end
        ch = word[0]
        word = word[1:]
        if ch not in self.root:
            return False
        return self.root[ch].search(word)


# trie = Trie()
# trie.add("add")
# trie.add("wtf")
# print(trie.search("add"))


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        global_ans = set()
        
        def bfs(i, j, node: Trie, visited):
            nonlocal board
            ch = board[i][j]
            if ch not in node.root:
                return
            visited[i][j] = True
            next_trie: Trie = node.root[ch]
            if next_trie.end:
                global_ans.add(next_trie.cur_word)
            if not next_trie.root:
                visited[i][j] = False
                return
            if i > 0 and not visited[i-1][j]:
                bfs(i-1, j, next_trie, visited)
            if j > 0 and not visited[i][j-1]:
                bfs(i, j-1, next_trie, visited)
            if i < len(board) - 1 and not visited[i+1][j]:
                bfs(i + 1, j, next_trie, visited)
            if j < len(board[0]) - 1 and not visited[i][j+1]:
                bfs(i, j + 1, next_trie, visited)
            visited[i][j] = False
        
        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                bfs(i, j, trie, visited)

        return list(global_ans)

Solution().findWords(
    [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
    ["oath","pea","eat","rain","hklf", "hf"]
)
# Solution().findWords(
#     [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
#     ["oath","pea","eat","rain"]
# )