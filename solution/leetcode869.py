class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def is_power_of_2(n):
            if n == 0:
                return False
            return n & (n-1) == 0

        s = str(n)
        visited = [False for _ in range(len(s))]

        def traceback(cur, start=False):
            nonlocal visited
            if len(cur) == len(s):
                return is_power_of_2(int("".join(cur)))
            for i in range(len(s)):
                if visited[i]:
                    continue
                if start and s[i] == "0":
                    continue
                visited[i] = True
                cur.append(s[i])
                if traceback(cur):
                    return True
                cur.pop()
                visited[i] = False
            return False
        
        return traceback([], True)

Solution().reorderedPowerOf2(1)