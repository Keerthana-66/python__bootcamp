#7.1your given with a natural no'1 -10 print even no's
"""my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i])"""
    


    #7.1show even numbers 
"""my_list=list(map(int,input().split()))  
for i in range(1,len(my_list),2):
    print(my_list[i])"""

#7.3given with spaces seprated list find numbee even element or oddelement 
my_list=list(map(int,input().split()))
even=0
odd=0
for i in my_list:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)




    


