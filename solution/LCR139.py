from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        j = 0
        for i in range(len(actions)):
            if actions[i] % 2 == 1:
                actions[i], actions[j] = actions[j], actions[i]
                j += 1
        return actions