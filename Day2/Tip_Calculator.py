print("Welcome to the tip calculator.")
total = input("What was the total bill? ")
tip_pct = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
tip = (float(tip_pct) / 100) * float(total)
grand_total = float(total) + float(tip)
per_person = float(grand_total) / int(people)
answer = round(per_person, 2)
print(f"Each person should pay: ${answer}")
#This worked, but if the second decimal ended in a 0 it wouldn't show it...e.g. kept getting $34.5 per person instead of $34.50 but it worked if there was a second decimal there.
#she addressed it in the solution video, there is a format function (which she didn't go over earlier) where you specify the format of decimal places...see stack overflow for how to round 2 decimal places python"
#answer is to add: answer = "{:.2f}".format(per_person)
