class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        from collections import Counter

        s = "{:b}".format(x ^ y)

        return Counter(s).get("1", 0)


Solution().hammingDistance(4, 1)
