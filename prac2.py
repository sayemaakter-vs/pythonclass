Marks=[50,-100,-90,200,70,99,89,80]
for n in Marks:
    if (n>0 and n<100):
        print("Valid")
        if (97<=n):
            print("A+")
        elif (93<=n):
            print("A")
        elif (90<=n):
            print("A-")
        elif (86<=n):
            print("B+")
        elif (83<=n):
            print("B")
        elif (83<=n):
            print("B-")
        elif (80<=n):
            print("c+")
        elif (75<=n):
            print("C") 
        elif (70<=n):
            print("D")
        elif (1<=n):
            print("F") 
    else:
        print("invalid")      