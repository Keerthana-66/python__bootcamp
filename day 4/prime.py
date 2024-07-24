
#prime or not 
'''a=int(input("enter a number:"))
r=a**0.5
count=0
for i in range(2,int(r+1)):
    if a%i==0:
        count=1
        break'''
    
    #FINDA THE PRIME NOS GIVEN RANGE
''''a=int(input("enter a number:"))
b=int(input("enter a number:"))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
           print(i)'''


n=int(input("enter a number :"))
for i in range(2000,2025):
    if n%4==0 and n%100!=0:
      print(i)
else:
    print("not a leap year")