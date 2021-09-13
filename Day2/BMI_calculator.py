
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

 

bmi = int
bmi = int(weight) / float(height)**2
bmi_whole=int(bmi)
bmi_print=str(bmi_whole)
 
#print(bmi)
#bmi_whole = str(bmi)
 
print("Your BMI is " + bmi_print)
#This worked, notice height is a float above...need to allow for decimals with that variable.
#Note, didn't need to do the extra step of adding the "Your BMI is" part but it was nice to learn how to do it by changing bmi_whole to a string with bmi_print. can't concatenate a string and integer so they had to both be strings.
