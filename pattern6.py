#right angled trinagle
for i in range(1,6):#for printing 5 space
    for j in range(5-i):#for printing * excluding the space
        print(" ",end=" ")#printing space
    for k in range(i):#printing the star
        print("*",end=" ")
    print()