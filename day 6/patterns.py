#lower triangle pattern
for i in range(5):
    for j in range(5):
         if(i==j or i<j):
           print("*",end="")
    print()

    #upper trinagle patterns
    for i in range(5):
        for j in range(5):
            if(i==j or i>j):
              print("*",end="")
    print()
    