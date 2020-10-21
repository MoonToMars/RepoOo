print("This is snek\n")

def tongue():
    for i in range(7):
        print("    ", end ="")

        if i % 4 == 0:
            print("*")
        elif i % 4 == 1:
            print(" *")
        elif i % 4 == 2:
            print("  *")
        else:
            print(" *")



def face():
    print("     *\n    ***\n\
   *****\n\
  *******")

def body():
    for i in range(17):
        if i % 6 == 0:
            print("  *******")
        elif i % 6 == 1:
            print(" *******")
        elif i % 6 == 2:
            print("*******")
        elif i % 6 == 3:
            print(" *******")
        elif i % 6 == 4:
            print("  *******")
        elif i % 6 == 5:
            print("   *******")

def tail():
    print("   *****\n    ***\n     *")

tongue()
face()
body()
tail()