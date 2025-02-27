class multiples:
    def __init__(self,n,k):
        self.n = n
        self.k = k
    def find_numbers(self):
        result = [x for x in range(self.n, self.k) if x%3 == 0 and x%5 == 0]
        return result
n = int(input())
k = int(input())
finder = multiples(n,k)
print(finder.find_numbers())    
