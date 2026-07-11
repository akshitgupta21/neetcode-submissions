class Solution:
    def minstrs(self,strs):
        l=[]
        for i in strs:
            l.append(len(i))
        y=min(l)
        return y


    def longestCommonPrefix(self, strs: List[str]) -> str:
        d=[]
        x=0
        a=0
        v=self.minstrs(strs)
        b=""
        while x==0 and a<v:
            s=set()
            for i in range(len(strs)):
                s.add(strs[i][a])
            if len(s)!=1:
                x=1
            else:
                a+=1
                d.extend(s)
        if d==[]:
            z=""
            return z
        else:
            l="".join(d)
            return l                    

                

o=Solution()
o.longestCommonPrefix(["bat","bag","bank","band"])








            
        