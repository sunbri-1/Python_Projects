# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
import math



def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area / cover)
  print(f"You will need {num_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)
