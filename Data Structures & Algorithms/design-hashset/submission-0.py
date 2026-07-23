class MyHashSet:
    def __init__(self):  
        self.a=[]        
    def add(self, key: int) -> None:
        if key in self.a:
            pass
        else:
            self.a.append(key)          

    def remove(self, key: int) -> None:
        d=None
        for i in range(len(self.a)):
            if self.a[i]==key:
                d=i
        if d==None:
            pass        
        else:
            del self.a[d]        
            
    def contains(self, key: int) -> bool:
        if key in self.a:
            return True
        else:
            return False
        


