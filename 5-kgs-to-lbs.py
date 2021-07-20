conversion_ratio = 0.45359237

user_weight = input("Your weight? (In Kgs) ")

in_lbs = float(user_weight) / conversion_ratio

print("Your weight (In Kilograms)\t: " + str(user_weight) + " kgs")
print("Your weight (In Pounds)\t: " + str(round(in_lbs, 2)) + " lbs")
