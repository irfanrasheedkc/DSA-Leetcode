class Solution:
    def pivotInteger(self, n: int) -> int:
        x = sqrt(n*(n+1)/2)
        if x.is_integer():
            return int(x)
        else:
            return -1