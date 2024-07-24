#print the unique char in string
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello world"
inp=i.lower() 
for i in inp:
      if(i not in ans):
            ans+=i
print(ans)
