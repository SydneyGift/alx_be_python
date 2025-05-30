#Draw a square pattern dependent on the number the user inputs

size = int(input("Enter the size of the pattern"))

while size > 0:
    range_size = size + 1
    for number in range(1,range_size):
        print("*" * size)
    size -= size