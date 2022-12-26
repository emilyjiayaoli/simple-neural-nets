def f_x(n):
    
        if n==0: 
            return 0
        elif n>0:
            x = (4/5)*(n-1)
            return f_x(x)

print(f_x(50))

#iterative approach
def calculate(n):
    def f_x(n):
        if n == 0: return 0
        return (4/5)*(n-1)
    while n>=0:
        n = f_x(n)
    return n
print(calculate(50))


#recursive, given x
def calculate2(x):
    x = 5*x
    def f_x(n):
        if n == 0: return 0
        return (4/5)*f_x((4/5)*(n-1))-1
    f_x(x)
    

def calculate3(x):
    res = 5*x
    for i in range(5):
        res = 5/4 * (res + 1)
    return res

def find():
    count = 1
    for i in range(1500):
        temp = calculate3(i)
        #print(temp)
        if (temp * 10)%10 == 0 and (temp * 100)%100 == 0 and (temp * 1000)%1000 == 0:
            return temp
print(find())
