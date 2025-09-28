from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or stack[-1] < 0 or stack[-1] * asteroid > 0:
                stack.append(asteroid)
                continue
            if stack[-1] > 0 and stack[-1] == abs(asteroid):
                stack.pop()
                continue
            elif stack[-1] > abs(asteroid):
                continue
            while stack and stack[-1] * asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    break
            else:
                if not stack or stack[-1] * asteroid > 0:
                    stack.append(asteroid)
                continue
            stack.pop()
        return stack
                
    

Solution().asteroidCollision([1,2,1,-2])
# Solution().asteroidCollision([-2,-2,1,-2])