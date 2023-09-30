print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? PLN "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? 12 "))

number_people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_people
result = round(bill_per_person, 2)
result = "{:.2f}".format(bill_per_person)
print(f" Each person should pay: {result} złotych ")