from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = list()
        x = len(matrix)
        y = len(matrix[0])
        visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        state_trans = {"right": "down", "down": "left", "left": "up", "up": "right"}

        i = j = 0
        count = 0
        state = "right" if len(matrix[0]) > 1 else "down"
        while count < x * y:
            res.append(matrix[i][j])
            visited[i][j] = 1
            count += 1
            if state == "right":
                j += 1
                if j + 1 >= y or visited[i][j + 1]:
                    state = state_trans[state]
            elif state == "down":
                i += 1
                if i + 1 >= x or visited[i + 1][j]:
                    state = state_trans[state]
            elif state == "left":
                j -= 1
                if j - 1 < 0 or visited[i][j - 1]:
                    state = state_trans[state]
            elif state == "up":
                i -= 1
                if i - 1 < 0 or visited[i - 1][j]:
                    state = state_trans[state]

        return res


print(Solution().spiralOrder([[3], [2]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6]]))
