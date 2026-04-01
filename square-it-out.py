# Take input from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

squares = []
even_squares = []
odd_squares = []

# Generate squares and classify them
for num in range(start, end + 1):
    sq = num ** 2
    squares.append(sq)
    
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)

# Output results
print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)