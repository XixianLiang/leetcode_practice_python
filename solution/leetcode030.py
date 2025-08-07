from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        word_len = len(words[0])
        substring_len = word_len * len(words)

        target = dict()
        for word in words:
            target[word] = target.get(word, 0) + 1

        ans = []

        def find_substring(start):
            i = 0
            sub_words = [
                s[start+j*word_len:start+(j+1)*word_len] for j in range(len(words))
            ]
            cur = dict()
            for word in sub_words:
                cur[word] = cur.get(word, 0) + 1
            for i in range((len(s)-start-substring_len) // word_len + 1):
                cur_index = start + i * word_len
                if cur == target:
                    ans.append(cur_index)
                remove_word = s[cur_index:cur_index + word_len]
                add_word = s[cur_index + substring_len: cur_index + substring_len + word_len]
                cur[remove_word] = cur.get(remove_word, 0) - 1
                if cur[remove_word] == 0:
                    del cur[remove_word]
                cur[add_word] = cur.get(add_word, 0) + 1


        for i in range(word_len):
            find_substring(i)
            
        return ans

# print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))