# input for weight in kg and height in cm
try:
	weight = float(input("Enter weight in kg: "))
except:
	print("Sorry, invalid entry. Please enter a value for weight")	
	weight = float(input("Try again - Enter weight in kg: "))

try:
	height_in_cm = float(input("Enter height in cm: "))
except:
	print("Sorry, invalid entry. Please enter a value for height")
	height_in_cm = float(input("Try again - Enter height in cm: "))	

# convert height in cm to m
height_in_m = height_in_cm / 100

# calculate BMI (weight / height^2), rounding to one decimal place
bmi =  weight / (height_in_m ** 2)
bmi_rounded = round(bmi,1)

print("BMI: {} kg/m^2".format(bmi_rounded))

# input for gender and calculate IBW and percent IBW for male and female
while True:
	gender = input("Enter male or female: ").lower()
	if gender == 'male':
		ibw_male = 50 + (0.9 * (height_in_cm - 152))
		ibw_male_rounded = round(ibw_male,1)
		print("IBW: {} kg".format(ibw_male_rounded))

		percent_ibw_male = (weight / ibw_male_rounded) * 100
		percent_ibw_male_rounded = round(percent_ibw_male)
		print("Percent IBW: {}%".format(percent_ibw_male_rounded))

	elif gender == 'female':
		ibw_female = 45.5 + (0.9 * (height_in_cm - 152))
		ibw_female_rounded = round(ibw_female,1)
		print("IBW: {} kg".format(ibw_female_rounded))

		percent_ibw_female = (weight / ibw_female_rounded) * 100
		percent_ibw_female_rounded = round(percent_ibw_female)
		print("Percent IBW: {}%".format(percent_ibw_female_rounded))

	else: 
		print('Sorry, invalid entry. Please enter "male" or "female".')
		continue
	break


# if BMI < = 24.9 and IBW <= 130%, use 30-35 kcal/kg, 1.2-1.5 g/kg, 45-65% of kcal in g CHO/day, and 1 mL/kcal


# if BMI 25 - 29.9 and IBW <= 130%, use 30-35 kcal/kg, 1.2-1.5 g/kg, 45-65% of kcal in g CHO/day, and 1 mL/kcal

# if BMI 25 - 29.9 and IBW >= 130%, use 25-30 kcal/kg, 1.1-1.4 g/kg, 45-65% of kcal in g CHO/day, and 1 mL/kcal

# if BMI > = 30 and IBW > 130%, use 20-25 kcal/kg, 1.5-2 g/kg IBW, 45-65% of kcal in g CHO/day, and 1 mL/kcal

