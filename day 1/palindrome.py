num=int(input())
rem=0
res=0
temp=num
while(num>0):
    rem=num%10
    res=(res*10)+rem
    if res==temp:
         print("palindrome")
else:
    print("not a palindrome")