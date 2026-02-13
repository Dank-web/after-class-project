base = int(input("Enter the base number: "))
power = int(input("Enter the power (n): "))

result = 1

for i in range(power):
    result = result * base

print("Result:", result)