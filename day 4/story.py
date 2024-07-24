#password verifier
#mr X is trying to create a new password for his instagram acc there are the required conditions creating a new password
#condition 1:
#mim length is 8 max length is 15
#condition 2:
#only @,/ allowed in password
#condition 

#no spaces are allowed 
#condition4:
#only aplha numeric are allowed 
#your supposwed to print weak if len is exact 8 
#len is between 8 to 12
#strong if len 12-15
s=input()
n=len(s)
count=0
str="@/"
for i in s:
    if(i==str[0] or i==str[1] and i!=''):
        count+=1
if(count==0):
    print("please follow the conditions")
elif(n<8):
    print("please follow the conditions")
elif(n==8):
    print("password is weak")
elif(n>8 and n<12):
    print("password is moderate")
elif(n>=12 and n<15):
    print("password is strong")
else:
    print("very strong")    