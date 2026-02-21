#take input
print("Half Pyramid Pattern of Stars (*) : ")
n = int(input("Enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
        print("* ", end="")
    print()

#Mirrored Right-angled Triangle

rows = int(input("enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)