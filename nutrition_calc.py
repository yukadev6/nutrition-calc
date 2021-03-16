# Input for getting weight and height info
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

# Calculate Ideal Body Weight(IBW) and %IBW for male vs. female
while True:
	gender = input("Enter male or female: ").lower()
	if gender == 'male':
		ibw_male = round(50 + (0.9 * (height_in_cm - 152)),1)
		print("IBW: {} kg".format(ibw_male))

		percent_ibw_male = round((weight / ibw_male) * 100)
		print("Percent IBW: {}%".format(percent_ibw_male))

	elif gender == 'female':
		ibw_female = round(45.5 + (0.9 * (height_in_cm - 152)),1)
		print("IBW: {} kg".format(ibw_female))

		percent_ibw_female = round((weight / ibw_female) * 100)
		print("Percent IBW: {}%".format(percent_ibw_female))

	else: 
		print('Sorry, invalid entry. Please enter "male" or "female".')
		continue
	break

# Convert height to meter and calculate BMI (weight / height^2), rounding to one decimal place
height_in_m = height_in_cm / 100

bmi =  round(weight / (height_in_m ** 2),1)
print("BMI: {} kg/m^2".format(bmi))

# Energy needs calculated based on BMI and %IBW, separate for male and female.
# Fluid needs calculated based on energy needs, 1 mL/kcal
def energy_fluid_calc():
	kcal15 = round(weight * 15)
	kcal20 = round(weight * 20)
	kcal25 = round(weight * 25)
	kcal30 = round(weight * 30)
	kcal35 = round(weight * 35)
	
	if gender == 'male':
		try:
			if bmi <= 24.9 and percent_ibw_male < 130:
				print("Estimated energy needs: {}-{} kcal/day (30-35 kcal/kg)".format(kcal30,kcal35))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal30,kcal35))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male < 130:
				print("Estimated energy needs: {}-{} kcal/day (25-30 kcal/kg)".format(kcal25,kcal30))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal25,kcal30))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male >= 130:
				print("Estimated energy needs: {}-{} kcal/day (20-25 kcal/kg)".format(kcal20,kcal25))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal20,kcal25))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated energy needs: {}-{} kcal/day (20-25 kcal/kg)".format(kcal20,kcal25))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal20,kcal25))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated energy needs: {}-{} kcal/day (15-20 kcal/kg)".format(kcal15,kcal20))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal15,kcal20))
			else:
				print("BMI>40, unable to provide estimated energy and fluid needs")
		except:
			print("Unable to provide estimated energy and fluid needs")

	elif gender == 'female':
		try:
			if bmi <= 24.9 and percent_ibw_female < 130:
				print("Estimated energy needs: {}-{} kcal/day (30-35 kcal/kg)".format(kcal30,kcal35))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal30,kcal35))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female < 130:
				print("Estimated energy needs: {}-{} kcal/day (25-30 kcal/kg)".format(kcal25,kcal30))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal25,kcal30))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female >= 130:
				print("Estimated energy needs: {}-{} kcal/day (20-25 kcal/kg)".format(kcal20,kcal25))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal20,kcal25))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated energy needs: {}-{} kcal/day (20-25 kcal/kg)".format(kcal20,kcal25))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal20,kcal25))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated energy needs: {}-{} kcal/day (15-20 kcal/kg)".format(kcal15,kcal20))
				print("Estimated fluid needs: {}-{} mL/day (1 mL/kcal)".format(kcal15,kcal20))
			else:
				print("BMI>40, unable to provide estimated energy and fluid needs")
		except:
			print("Unable to provide estimated energy and fluid needs")

energy_fluid_calc()

# Protein needs calculated based on BMI and %IBW, separate for male and female
def protein_calc():
	gram1_1 = round(weight * 1.1)
	gram1_2 = round(weight * 1.2)
	gram1_3 = round(weight * 1.3)
	gram1_4 = round(weight * 1.4)
	gram1_5 = round(weight * 1.5)
	
	if gender == 'male':
		gram1_5ibwmale = round(ibw_male * 1.5)
		gram2_0ibwmale = round(ibw_male * 2)
		try:
			if bmi <= 24.9 and percent_ibw_male < 130:
				print("Estimated protein needs: {}-{} g/day (1.2-1.5 g/kg)".format(gram1_2,gram1_5))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male < 130:
				print("Estimated protein needs: {}-{} g/day (1.2-1.4 g/kg)".format(gram1_2,gram1_4))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male >= 130:
			 	print("Estimated protein needs: {}-{} g/day (1.1-1.3 g/kg)".format(gram1_1,gram1_3))
			elif bmi >=30 and bmi <=39.9: 
				print("Estimated protein needs: {}-{} g/day (1.5-2 g/kg)".format(gram1_5ibwmale,gram2_0ibwmale))
			else:
			 	print("BMI>40, unable to provide estimated protein needs")
		except:
			print("Unable to provide estimated protein needs")

	elif gender == 'female':
		gram1_5ibwfemale = round(ibw_female * 1.5)
		gram2_0ibwfemale = round(ibw_female * 2)
		try:
			if bmi <= 24.9 and percent_ibw_female < 130:
				print("Estimated protein needs: {}-{} g/day (1.2-1.5 g/kg)".format(gram1_2,gram1_5))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female < 130:
				print("Estimated protein needs: {}-{} g/day (1.2-1.4 g/kg)".format(gram1_2,gram1_4))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female >= 130:
				print("Estimated protein needs: {}-{} g/day (1.1-1.3 g/kg)".format(gram1_1,gram1_3))
			elif bmi >=30 and bmi <=39.9: 
				print("Estimated protein needs: {}-{} g/day (1.5-2 g/kg)".format(gram1_5ibwfemale,gram2_0ibwfemale))
			else:
				print("BMI>40, unable to provide estimated protein needs")
		except:
			print("Unable to provide estimated protein needs")

protein_calc()

# Carbohydrate needs calculated based on 45-65% of energy needs and converted to g/day
def carb_calc():
	kcal15_carb45 = round(((weight * 15) * .45)/4)
	kcal15_carb65 = round(((weight * 15) * .65)/4)
	kcal20_carb45 = round(((weight * 20) * .45)/4)
	kcal20_carb65 = round(((weight * 20) * .65)/4)
	kcal25_carb45 = round(((weight * 25) * .45)/4)
	kcal25_carb65 = round(((weight * 25) * .65)/4)
	kcal30_carb45 = round(((weight * 30) * .45)/4)
	kcal30_carb65 = round(((weight * 30) * .65)/4)

	if gender == 'male':
		try:
			if bmi <= 24.9 and percent_ibw_male < 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal30_carb45,kcal30_carb65))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male < 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal25_carb45,kcal25_carb65))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male >= 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal20_carb45,kcal20_carb65))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal20_carb45,kcal20_carb65))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal15_carb45,kcal15_carb65))
			else:
				print("BMI>40, unable to provide estimated carbohydrate needs")
		except:
			print("Unable to provide estimated carbohydrate needs")

	elif gender == 'female':
		try:
			if bmi <= 24.9 and percent_ibw_female < 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal30_carb45,kcal30_carb65))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female < 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal25_carb45,kcal25_carb65))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female >= 130:
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal20_carb45,kcal20_carb65))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal20_carb45,kcal20_carb65))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated carbohydrate needs: {}-{} g/day (45-65% kcal)".format(kcal15_carb45,kcal15_carb65))
			else:
				print("BMI>40, unable to provide estimated carbohydrate needs")
		except:
			print("Unable to provide estimated carbohydrate needs")
	
carb_calc()
