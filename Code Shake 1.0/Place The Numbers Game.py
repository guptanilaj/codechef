for t in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    even=0
    odd=0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    if n%2==0:
        if odd==even:
            print("YES")
        else:
            print("NO")
    else:
        if odd-even==1:
            print("YES")
        else:
            print("NO")
