
age = input("What is your current age?")

 

total_days = 90*365
total_weeks = 90*52
total_months = 90*12
x = total_days - int(age)*365
y = total_weeks - int(age)*52
z = total_months - int(age)*12
#You have x days, y weeks, and z months left. 
print(f"You have {x} days, {y} weeks, and {z} months left.")
#This worked, but she took a different route which was a little cleaner...see the 6:00 mark for her code
