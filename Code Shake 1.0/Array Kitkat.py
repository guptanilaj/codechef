def isprime(x):
    if x==0 or x==1:
        return "KITKAT"
    for i in range(2,x):
        if x%i==0:
            return "KAT"
    return "KIT"
for i in range(int(input())):
    n=int(input())
    diff=[]
    lst=[int(x) for x in input().split(" ")]
    for j in range(int(n/2)):
        print(abs(lst[j]-lst[n-j-1]))
        diff.append(abs(lst[j]-lst[n-j-1]))
    print(isprime(sum(diff)))
    diff.clear()
