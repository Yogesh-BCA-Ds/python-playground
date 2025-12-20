import math
class operations:
    def not_prime(self):
        non_prime = []
        n = int(input("enter a number: "))
        for i in range(2,n+1):
            for j in range(2,i):
                if i%j == 0:
                    non_prime.append(i)
                    break
        return non_prime
        
    def div_by_SumDigit(self):
        var = self.not_prime()
        l1 = []
        l2 = []
        for i in var: 
            j1 = i
            x = 0
            while j1>0:                                  
                l = j1%10
                x+=l
                j1 = j1//10
            l1.append(x)         
        for m in range(0,len(var)):
            if l1[m] == 0:
                continue
            else: 
                if var[m] % l1[m] == 0:
                    l2.append(var[m])
        return l2
	        
    def not_perfect_square(self):
        var2 = self.div_by_SumDigit()
        l4 = []
        o = []
        s = []
        for i in var2:
            l4.append(int(math.sqrt(i)))
        for j in l4:
            q = j*j
            o.append(q)
        for b in var2:
            if b not in o:
                s.append(b)                
        v = len(s)
        print('valid numbers are:',s)
        print('count:',len(s))                 

op = operations()
op.not_perfect_square()
            
