class Solution:
    f = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1}
    s = {'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1}
    t = {'z': 1, 'x': 1, 'c': 1, 'v': 1, 'b': 1, 'n': 1, 'm': 1}
    output = []
    def check(self,n,orginal):
        if n[0] in self.f:
            for j in n[1:]:
                if j not in self.f:
                    return
            self.output.append(orginal)
        elif n[0] in self.s:
            for j in n[1:]:
                if j not in self.s:
                    return
            self.output.append(orginal)    
        elif n[0] in self.t:
            for j in n[1:]:
                if j not in self.t:
                    return
            self.output.append(orginal) 
            
    def findWords(self, words: List[str]) -> List[str]:
        self.output.clear()
        for i,n in enumerate(words):
            self.check(n.lower(),n)
        return self.output
    
   