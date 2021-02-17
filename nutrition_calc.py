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

# create a BMI Class that caculates BMI = weight / height^2, rounding to one decimal place
class Bmi:

	def __init__(self):
		self.height_converted = height_in_cm / 100

	def calc_bmi(self):
		bmi =  weight / (self.height_converted ** 2)
		return round(bmi,1)

# create IBW Class
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

# Energy needs based on BMI and %IBW
# if BMI < = 29.9 and IBW <= 130%, use 30-35 kcal/kg

# if BMI 25 - 29.9 and IBW >= 130%, use 25-30 kcal/kg

# if BMI > = 30 and IBW > 130%, use 20-25 kcal/kg


# Protein needs based on BMI and %IBW
# if BMI < = 29.9 and IBW <= 130%, 1.2-1.5 g/kg
# if BMI 25 - 29.9 and IBW >= 130%, 1.1-1.4 g/kg
# if BMI > = 30 and IBW > 130%, 1.5-2 g/kg IBW,

# CHO needs based on energy needs, 45-65% of kcal in g CHO/day

# Fluid needs based on energy needs, 1 mL/kcal

# Calc setup

# print 

