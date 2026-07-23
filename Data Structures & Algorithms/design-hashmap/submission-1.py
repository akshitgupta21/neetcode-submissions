class MyHashMap:

    def __init__(self):
        self.a=[]       

    def put(self, key: int, value: int) -> None:
        a=0
        for i in range(len(self.a)):
            if self.a[i][0] == key:
                self.a[i][1]=value
                a=1
        if a==0:
            self.a.append([key,value])
           
    def get(self, key: int) -> int:
        n=-1
        for i in range(len(self.a)):
            if self.a[i][0]==key:
                l=self.a[i][1]
                n=l
                break
        return n
                                       

    def remove(self, key: int) -> None:
        for i in range(len(self.a)):
            if self.a[i][0]==key:
                del self.a[i]
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)