#acc to the previous history z practicipated in 14 games out of this he is 
#write a program to check whether Z,X,Y travel in same plane or not 

bh=int(input("height of X"))
bw=int(input("weight of X"))
th=int(input("height of Y"))
tw=int(input("weight of Y"))
fact7=(50*14)/100
if(bh==140 and bw%2==0):
    print("mr.X are selected for batminton")
elif(th<140 and th>118 and tw%fact7==0):
    print("mr.Y are selected for table tennis")
else:
    print("mr.Z are selected for swimming")