n, m = [int(_) for _ in input().split()]



from enum import IntEnum


class Method(IntEnum):
    PLACE = 1
    LEAVE = 2


class Solution:
    def __init__(self, n):
        
        self.place = [0 for _ in range(n)]
        self.target = dict()
    
    def place_obj(self, method, no):
        if method == Method.PLACE:
            ans = self.__place(no)
        else:
            ans = self.__leave(no)
        if ans is not None:
            print(ans + 1)
        
    def __place(self, no):
        if self.target.get(no, None) is not None:
            return
        if len(self.target) == 0:
            self.target[no] = 0
            self.place[0] = no
            return 0
        start = self.find_biggest_place()
        self.target[no] = start
        self.place[start] = no
        return start

    def __leave(self, no):
        if self.target.get(no, None) is None:
            return
        
        i = self.target[no]
        self.place[i] = 0
        del self.target[no]
        return i
         
    def find_biggest_place(self, place=None):
        if place is not None:
            self.place = place
        ans = -1
        max_place = 0
        cur_place = 0
        i = 0
        if self.place[0] == 0:
            while i < len(self.place):
                if self.place[i] != 0:
                    max_place = cur_place
                    ans = 0
                    break
                i += 1
                cur_place += 1
        
        while i < len(self.place):
            while i < len(self.place) and self.place[i]:
                i += 1
            cur_place = 0
            start = i
            while i < len(self.place) and self.place[i] == 0:
                i += 1
                cur_place += 1
            if i < len(self.place):
                cur_place = (cur_place + 1) // 2
                start = start + cur_place - 1
            else:
                start = len(self.place) - 1
            if cur_place > max_place:
                ans = start
                max_place = cur_place
                
        return ans

s = Solution(n)
test = [[1,1],[2,2],[1,1],[1,2],[2,2],[2,1],[1,2]]
# for _ in range(m):
#     method, no = [int(_) for _ in input().split()]
#     s.place_obj(method, no)
for j in range(m):
    method, no = test[j]
    s.place_obj(method, no)

# 3 7
# 1 1
# 2 2
# 1 1
# 1 2
# 2 2
# 2 1
# 1 2