class model:
    def __init__(self, val=0):
        self.val = val

    def var1(self,val):
        self.var1 = val
        return self.var1+self.val

    def var2(self, val):
        self.var2 = val
        return self.var2+self.val
    
    def solve(self,val):
        return self.__init__(val)

m = model(2)
x = m.var1(0)
y = m.var2(2)

print(x)
print(y)

m.solve(100)

print(x)
print(y)

