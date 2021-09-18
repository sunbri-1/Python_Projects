# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")



import random
total_peeps = len(names)
random_int = random.randint(0, total_peeps-1)
print(f"{names[random_int]} is going to buy the meal today!")
