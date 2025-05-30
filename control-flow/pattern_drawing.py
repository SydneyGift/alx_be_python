#Draw a square pattern dependent on the number the user inputs

size = int(input("Enter the size of the pattern:"))

while size > 0:
    for rows in range(1,size + 1):
            print("*", end ="")
            for columns in range(1,size):
                print("*", end ="")
            print()  
    size -= size 