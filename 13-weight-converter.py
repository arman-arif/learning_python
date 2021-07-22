# weight converter

weight = input("\n Your Weight: ")
unit = input(" (L)bs or (K)g ? ")

if unit.upper() == "L":
    converted = int(weight) * 0.45
    print(f" You are {converted} kgs.")
elif unit.upper() == "K":
    converted = int(weight) / 0.45
    print(f" You are {converted} lbs.")

