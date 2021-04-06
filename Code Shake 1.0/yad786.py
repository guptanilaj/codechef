for i in range(int(input())):
    s1=input()
    s2=input()
    sum1=0
    sum2=0
    for j in s1:
        sum1+=ord(j)
    for j in s2:
        sum2+=ord(j)
    res=abs(sum1-sum2)
    if sum1==sum2:
        print("No one")
    elif (res>=1 and res<=10):
        print("Rashmi")
    else:
        print("Mohit")