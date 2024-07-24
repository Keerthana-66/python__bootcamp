money=int(input())
a=int(input())
b=int(input())
o=int(input())
aprice=(a*15)
bprice=(b*4)
oprice=(o*5)
sum=aprice+bprice+oprice
if(sum>=money):
    print("not cheated")
else:
    print("cheated")

