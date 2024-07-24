#write a captial letters in a given string
''''for i in range(65,91):
    print(chr(i),end=" ")'''

    #remove all the brAckets from given algebric expression
inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125):
        pass
    else:
      print(i,end=" ")


#print next coming four letters with the addition of 4 example ABC  GIVES DEF 0
s=input()
n=int(input())
for i in s:
    e=ord(i)+n
    print(chr(e),end="")