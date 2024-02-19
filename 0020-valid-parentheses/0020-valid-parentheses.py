class Solution:
    def isValid(self, s: str) -> bool:
        sym = {'(':')','{':'}','[':']'}
        op = {'(':0,'{':0,'[':0}
        stack = []
        if s[0] not in sym:
            return False
        stack.append(s[0])
        for x in s[1:]:
            if not stack:
                stack.append(x)
                continue
            y = stack.pop()
            if y in op and sym[y]==x:
                continue
            else:
                stack.append(y)
                stack.append(x)
        if not stack:
            return True
        else:
            return False