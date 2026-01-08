
"""
num_guests = 25
bread_weight = 16.0
serving_size = 2.5

serving_per_loaf = bread_weight / serving_size
loaf_needed = num_guests / serving_per_loaf

print("For", num_guests, "people, you will need", loaf_needed, "loaves of bread" )
print()
print(f"{loaf_needed * 1.5:.10f} teaspoons instant yeast")
print(f"{loaf_needed * 1.5:.10f} teaspoons salt")
print(f"{loaf_needed * 1.5:.10f} teaspoons sugar")
print(f"{loaf_needed * 2.5:.10f} cups all-purpose flour")
print(f"{loaf_needed * 2.0:.10f} cups sourdough starter")
print(f"{loaf_needed * 0.5:.10f} cups lukewarm water")
"""

percentage = float (input("Enter the percentage to tip: "))
people = int(input("Enter number of people: "))
bill_amount = float(input("Enter bill: "))
tip_amount = round((bill_amount * percentage/100), 2)
total_amount = round(bill_amount + tip_amount , 2)
tip_person = round(tip_amount / people)
total_person = round(total_amount / people)
print("Tip amount: $" + str(tip_amount))
print("Total amount: $" + str(total_amount))
print("Tip per person: $" + str(tip_person))
print("Total per person: $" + str(total_person))