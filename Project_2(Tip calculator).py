# Project 2 - Tip calculator

total_bill = float(input("How much was the total bill ?\n"))
total_people = int(input("How many people would be contributing ?\n"))
tip_percentage = float(input("What percent tip would you like to give ?(Just the number): "))

tip_amount = total_bill * (tip_percentage/100)
total_amount = tip_amount + total_bill
amount_per_person = round(total_amount/total_people, 2)

print("Each person would have to pay:", amount_per_person)