class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result = 0
        for x in range(len(s)-1):
            if map[s[x]]<map[s[x+1]]:
                result-=map[s[x]]
            else:
                result+=map[s[x]]
        result+=map[s[len(s)-1]]
        return result