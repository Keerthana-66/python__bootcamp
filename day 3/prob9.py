#9  find the element that is present in k+n th index k is given by user 
#k=3  k=2
#3 6 8 61 2 op:2
#----------------------
#k=3
#n=4
#80 70 54 36 72 op:error0

#my_list=list(map(int,input().split()))
#k=int(input())
#n=int(input())
#t=k+n
#if(len(my_list)<k+n):
    #print("error")
#else:
    #for i in range(len(my_list)):
        #print((my_list[t]))
       # break
    




#print the element at a particular index 
#find th element present in k index
#k=3
# 3 6 8 4 61 2
#op:4
#--------------------
#k=8
#80 70 54 36 72
#op:36
#my_list=list(map(int,input().split()))
#k=int(input())
#for i in range(len(my_list)):
 #   "print(k%len(my_list))
  #  "break


#find the max len of given list
#testcase:0
#12 23 36 44 45 57
#57

#testcase:1
#56 78 -8 12 34 -99
#my_list=list(map(int,input().split()))
#max=0
#for i in range(len(my_list)):

 #   if(max<my_list[i]):
  #      max=my_list[i]
#print("the max element in the list: ",max)

#my_list=list(map(int,input().split()))
#min=my_list[0]
#for i in range(len(my_list)):

    #if(min>my_list[i]):
     #   min=my_list[i]
 #print("the min element in the list: ",min)




#replace the elements in an array with  average max and min elements

my_list=list(map(int,input().split()))
max=my_list[0]
for i in range(len(my_list)):
       if(my_list[i]>max):
           max=my_list[i]
print(max)
min=my_list[0]
for i in range(len(my_list)):

        if(my_list[i]<min):
           min=my_list[i]
print(min)
avg=(max+min)//2
print(avg)
for i in range(len(my_list)):
      my_list[i]=avg
print(my_list)

