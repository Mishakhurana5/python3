clothes = input("Enter the type of season: ")

if clothes == 'Summer' or clothes == 'summer' or clothes == 'SUMMER':
    print("You should wear light clothes")
elif clothes == 'Winter' or clothes == 'winter' or clothes == 'WINTER':
    print("You should wear heavy clothes")
else:
    print("Please enter a valid season")
    