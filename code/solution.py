class Solution:
    def __init__(self):
        self.table = [0,1]
    def fib(self,n):
        self.make_table(n)
        return self.table[n]
    
    def make_table(self,n):
        if (n == 0 or n == 1):
            return True
        for i in range(2,n+1):
            self.table.append(self.table[i-1]+self.table[i-2])
        return True 

