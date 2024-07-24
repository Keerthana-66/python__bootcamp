'''print(ord('a'))
print(ord('<'))'''

#ascii to char
'''print(ord("<"))
print(chr(60))'''

#chech how many vowels are there in string
'''check=(aeiou)
count=0
inp="hello world"
for i in inp:
      if(i in check):
            count+=1
print(count)'''

54#consonant
'''vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower() 
for i in inp:
      if(i in consonent):
            count+=1
print(count)'''
#print all the vowles followed by consonent
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=" "
i="hello world"
inp=i.lower() 
for i in inp:
      if(i in consonent):
            ans+=i
print(ans)
for i in inp:
      if(i in vowel):
            ans+=i
print(ans)