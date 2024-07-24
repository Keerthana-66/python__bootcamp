#print the numeric values in the string and add them 
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
check='0123456789'
ans=0
i="hello 1234world"
inp=i.lower() 
for i in inp:
      if(i in check):
            ans+=int(i)
print(ans)