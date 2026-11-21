#star 
for i in range(1,6):#for printing 5 space
    for j in range(5-i):#for printing * excluding the space
        print(" ",end=" ")#printing space
    for k in range(2*i-1):
        print("*",end=" ")
    print()