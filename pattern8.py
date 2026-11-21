for i in range(5,0,-1):#for printing 4 space
    for j in range(5-i):#for printing * excluding the space
        print(" ",end=" ")#printing space
    for k in range(2*i-1):
        print("*",end=" ")
    print()