#Print an increasing number pattern from a users input

size = int(input("Enter the size of the pattern between 1 and 10: "))

while 1 <= size <= 10:#Make sure the pattern can only be between one and ten
    for rows in range(1, size+1, 1):#This will execute size+1 times thus giving the total number of size rows
        for columns in range(1, rows+1, 1):#This will execute rows' time for every outer loop execution
            print(columns, end="")
        print("")#After printing each row, go to the next line i.e empty line after each row.
    size -= size#So that the while loop only runs once.
