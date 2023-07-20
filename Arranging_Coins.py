def Arranging_Coins(n):
    row=0
    for i in range(1,n+1):
        if n>=i:
            n-=i
            row+=1
    return row

n=int(input())
print(Arranging_Coins(n))