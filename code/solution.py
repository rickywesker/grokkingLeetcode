class Soluton:
    def __init__(self):
        self.table = [0,1]
    def fib(self,n):
        if (n == 0 or n == 1):
            return self.table[n]
        self.make_table(n)
        return self.table[-1]
    
    def make_table(self,n):
        for i in range(2,n+1):
            self.table.append(self.table[0]+self.table[1])
            self.table.pop(0)


