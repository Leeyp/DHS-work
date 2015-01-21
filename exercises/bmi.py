weight = input("Give me your weight in kg")
height = input("Give me your height in m")

BMI = round(float(weight)/(float(height)*float(height)),2)

if BMI >= 27.5:
	print("You are at high risk!")
elif BMI >= 23.0 and BMI < 27.4:
	print("You are at medium risk!")
elif BMI >= 18.5 and BMI < 22.9:
	print("You are healthy")
else: 
	print("You are underweight!")
