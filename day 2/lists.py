#my_list=[1,2,-13,14,-99,499]
#psort:
#my_list.sort()
#print(*my_list)

my_list=list(map(int,input().split(" ")))
choice=int(input())
if(choice==1):
    my_list.append(9)
    print(*my_list)
elif(choice==2):
     my_list.pop(2)
     print(*my_list)
elif(choice==3):
     print("hello")
else:
    print("teju")

