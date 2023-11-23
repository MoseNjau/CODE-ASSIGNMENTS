total_bill = float(input("Enter the total bill amount: $"))

# Input tip percentage (10%, 12%, or 15%)
while True:
    tip_percentage = input("Enter the tip percentage (10, 12, or 15): ")
    if tip_percentage in ["10", "12", "15"]:
        tip_percentage = float(tip_percentage) / 100
        break
    else:
        print("Invalid input. Please enter 10, 12, or 15.")

num_people = int(input("Enter the number of people splitting the bill: "))
tip_amount = total_bill * tip_percentage
total_amount = total_bill + tip_amount
amount_per_person = total_amount / num_people

print(f"Each person should pay: ${amount_per_person:.2f}")
