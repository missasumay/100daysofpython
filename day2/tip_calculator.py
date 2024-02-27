# inputs
total_bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? Enter number only\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15%?\n"))
how_many_people = int(input("How many people to split the bill?\n"))

# calculate amount per person
amount_per_person = (total_bill / how_many_people) 

#calculate final amount per person with tip
total_amount = amount_per_person + (amount_per_person * (tip / 100))

# print result
print(f"Each person should pay: ${total_amount}")