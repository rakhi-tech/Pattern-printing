#hollow square
for i in range(1,6):#for printing 5 row
    for j in range(1,6):#for printing 5 column
        if i == 1 or i==5 or j == 1 or j == 5:#condtion for printing the star
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()