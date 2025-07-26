from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        reached = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        next_case = ["right", "down", "left", "up"]
        case = "right"
        i, j = 0, 0
        width = len(matrix[0])
        height = len(matrix)
        ans = []
        # q = 0
        while True:
            # q += 1
            if all([all(reached[_]) for _ in range(height)]):
                return ans
            # print(ans)
            # if q > 9:
            #     break
            if case == "right":
                # print(f"hi:{i},{j}:{reached}")
                while j < width and not ((reached[i][j + 1] if j < width - 1 else False) and reached[i][j]):
                    if not reached[i][j]:
                        ans.append(matrix[i][j])
                    reached[i][j] = True
                    if j < width - 1 and not reached[i][j + 1]:
                        j += 1
                        continue
                    break
                case = "down"
                continue
            elif case == "down":
                # print(f"j:{j}")
                while i < height and not ((reached[i + 1][j] if i < height - 1 else False) and reached[i][j]):
                    if not reached[i][j]:
                        ans.append(matrix[i][j])
                    reached[i][j] = True
                    if i < height - 1 and not reached[i + 1][j]:
                        i += 1
                        continue
                    break
                case = "left"
                continue
            elif case == "left":
                while j >= 0 and not ((reached[i][j - 1] if j > 0 else False) and reached[i][j]):
                    if not reached[i][j]:
                        ans.append(matrix[i][j])
                    reached[i][j] = True
                    if j > 0 and not reached[i][j - 1]:
                        j -= 1
                        continue
                    break
                case = "up"
                continue
            elif case == "up":
                while i >= 0 and not ((reached[i - 1][j] if i > 0 else False) and reached[i][j]):
                    if not reached[i][j]:
                        ans.append(matrix[i][j])
                    reached[i][j] = True
                    if i > 0 and not reached[i - 1][j]:
                        i -= 1
                        continue
                    break
                case = "right"
                continue




print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[3], [2]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6]]))
