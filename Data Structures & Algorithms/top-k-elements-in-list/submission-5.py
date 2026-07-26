class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=list(set(nums)) 
        d=[] 
        for i in l:
            b=nums.count(i) 
            d.append(b)
        s=[] 
        for i in range(k):
            f=max(d) 
            g=d.index(f) 
            s.append(l[g]) 
            d.remove(f) 
            l.remove(l[g])

        return s


            




            
            
            
        