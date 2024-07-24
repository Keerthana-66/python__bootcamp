#peek elements ***
'''my_list=list(map(int,input().split()))
#count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
       print(my_list[i],end=" ") '''

#swap
'''n=int(input())
sum=n*(n+1)//2
print(sum)'''
 
#peak element if it comes last 
'''my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
       count=i
       #print(my_list[i],end=" ")
if(my_list[-1]>my_list[-2] and my_list[-1]>count):
    count=len(my_list)-1
print(my_list[count])'''

#GCD of 2 numbers 
#euclidean algorithm
'''a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:" ))
while b!=0:
     a,b=b,a%b
     print("GDC of 2 numbers is: ",a)'''

#lcm
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:" ))
c,d=a,b
while b!=0:
     a,b=b,a%b
     print((c*d)//a)









