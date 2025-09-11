from collections import deque


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
        knowq = deque([(0, 1)])
        shareq = deque([])
        will_share = 0
        for i in range(1, n):
            if knowq and i >= knowq[0][0] + delay:
                new_share = knowq.popleft()
                shareq.append(new_share)
                will_share += new_share[1]
            if shareq and i >= shareq[0][0] + forget:
                new_forget = shareq.popleft()
                will_share -= new_forget[1]
            if will_share > 0:
                knowq.append((i, will_share))
        knwon = sum(_[1] for _ in knowq) + will_share
        return knwon
print(Solution().peopleAwareOfSecret(6, 2, 4))
print(Solution().peopleAwareOfSecret(4, 1, 3))