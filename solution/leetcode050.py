class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def quickMul(N):
            if N==0:
                return 1.0
            y = quickMul(N // 2)
            if N % 2 == 0:
                return y * y
            else:
                return y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)