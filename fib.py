def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fibo(n):
    ls=[0,1,1]
    for i in range(3,n+1):
        ls+=[sum(ls[-2:])]
    return ls[n]
def hanoi (n,a,b,c):
    if n==0:
        return
    hanoi(n-1,b,a,c)
    print(f"{n} : {a}->{C}")
    hanoi(n-1,b,a,c)
def path(p,n,m):
    global count
    if n==0 and m==0:
        count+=1
        print(count,": ",p)
    if n:
        path(p+"^",n-1,m)
    if m:
        path(p+">",n,m-1)

if __name__ == "__main__":
    count=0
    path("",100,7)