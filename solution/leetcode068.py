from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        def buildString(words, last=False):
            sep = len(words) - 1
            if sep == 0 or last:
                prefix = " ".join(words)
                return prefix + " " * (maxWidth - len(prefix))
            space = maxWidth - sum(len(w) for w in words)
            blanks = space // sep
            addition = space % sep
            ret = ""
            add = False
            for i in range(len(words) - 1):
                if addition > 0:
                    add = True
                    addition -= 1
                ret += (words[i] + " "*blanks + (" " if add else ""))
                add = False
            ret += words[-1]
            return ret

        i = 0
        candidate_words = []
        while i < len(words):
            candidate_words.append(words[i])
            require = len(words[i])
            i += 1
            while require <= maxWidth:
                if i == len(words) or len(words[i]) + 1 + require > maxWidth:
                    ans.append(buildString(candidate_words, i == len(words)))
                    candidate_words.clear()
                    break
                require += (1 + len(words[i]))
                candidate_words.append(words[i])
                i += 1
        
        return ans
        

Solution().fullJustify(
    ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
    20
)