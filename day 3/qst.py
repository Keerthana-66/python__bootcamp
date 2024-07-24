#find the missing num in an arry
'''my_list=list(map(int,input().split()))
n=int(input())
m=len(my_list)
n=n*(n+1)//2
sum=0
for i in range(len(my_list)):
    sum+=my_list[i]
print(n-sum)'''



#find duplicatr vale
'''my_list=list(map(int,input().split()))
li=[]
for i in my_list:
    if(i not in li):
        li.append(i)
print(*li)'''

#sum of digits using while loop
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''


#find the sum of squares of digit of no.s
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)

#sum of even nos
'''n=123
sum=0
while n>0:
     r=n%10
     if(r%2==0):
       sum=sum+r
       n=n//10
print(sum)'''