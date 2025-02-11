# Tip Calculator

# Get user inputs
bill = float(input("Enter the total bill amount: $"))
tip_percentage = float(input("Enter the tip percentage (e.g., 12 for 12%): "))
people = int(input("Enter the number of people splitting the bill: "))

# Calculate total amount per person
total_per_person = (bill / people) * (1 + tip_percentage / 100)

# Format the result to 2 decimal places
formatted_total = "{:.2f}".format(total_per_person)

# Display the result
print(f"Each person should pay: ${formatted_total}")
