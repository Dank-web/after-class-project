decimal = int(input("Enter a decimal number: "))

binary = bin(decimal)

print("Binary number:", binary[2:])  # [2:] removes '0b'