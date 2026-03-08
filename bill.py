#program to calculate customer due amount

#take bill amount from user 
bill_amount = float(input("Enter the total bill amount: "))

#take paid amount from user
paid_amount = float(input("Enter the amount paid by the customer: "))

#calculate due amount
due_amount = bill_amount - paid_amount

#display result
if due_amount > 0:
    print("Customer still needs to pay:", due_amount)
elif due_amount == 0:
    print("The bill is fully paid. No due amount")
else:
    print("Customer paid extra:",abs(due_amount))