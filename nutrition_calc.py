# input for getting weight and height info
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

# convert height to meter and calculate BMI = weight / height^2, rounding to one decimal place
height_in_m = height_in_cm / 100

bmi =  round(weight / (height_in_m ** 2),1)
print("BMI: {} kg/m^2".format(bmi))

# calculate IBW and %IBW for male vs. female
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

# Energy needs based on BMI and %IBW
def energy_calc():
	kcal15 = round(weight * 15)
	kcal20 = round(weight * 20)
	kcal25 = round(weight * 25)
	kcal30 = round(weight * 30)
	kcal35 = round(weight * 35)
	
	if gender == 'male':
		try:
			if bmi <= 24.9 and percent_ibw_male < 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal30,kcal35))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male < 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal25,kcal30))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male >= 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal20,kcal25))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated energy needs: {}-{} kcal/day".format(kcal20,kcal25))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated energy needs: {}-{} kcal/day".format(kcal15,kcal20))
			else:
				print("BMI>40, unable to provide estimated energy needs")
		except:
			print("Unable to provide estimated energy needs")

	elif gender == 'female':
		try:
			if bmi <= 24.9 and percent_ibw_female < 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal30,kcal35))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female <= 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal25,kcal30))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_female >= 130:
				print("Estimated energy needs: {}-{} kcal/day".format(kcal20,kcal25))
			elif bmi >=30 and bmi <=34.9: 
				print("Estimated energy needs: {}-{} kcal/day".format(kcal20,kcal25))
			elif bmi >=35 and bmi <=39.9: 
				print("Estimated energy needs: {}-{} kcal/day".format(kcal15,kcal20))
			else:
				print("BMI>40, unable to provide estimated energy needs")
		except:
			print("Unable to provide estimated energy needs")

energy_calc()

# Protein needs based on BMI and %IBW
def protein_calc():
	gram1_1 = round(weight * 1.1)
	gram1_2 = round(weight * 1.2)
	gram1_3 = round(weight * 1.3)
	gram1_4 = round(weight * 1.4)
	gram1_5 = round(weight * 1.5)
	
if gender == 'male':
		try:
			if bmi <= 24.9 and percent_ibw_male < 130:
				print("Estimated protein needs: {}-{} g/day".format(gram1_2,gram1_5))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male < 130:
				print("Estimated protein needs: {}-{} g/day".format(gram1_2,gram1_4))
			elif bmi >=25 and bmi <=29.9 and percent_ibw_male >= 130:
				print("Estimated protein needs: {}-{} g/day".format(gram1_1,gram1_3))
			# elif bmi >=30 and bmi <=39.9: 
			# 	gram1_5ibwm = round(ibw_male * 1.5)
			# 	gram2_0ibwm = round(ibw_male * 2)
			# 	print("Estimated protein needs: {}-{} g/day".format(gram1_5ibwm,gram2_0ibwm))
			else:
				print("BMI>40, unable to provide estimated protein needs")
		except:
			print("Unable to provide estimated protein needs")

# elif gender == 'female':
# 		try:
# 			if bmi <= 24.9 and percent_ibw_female < 130:
# 				print("Estimated protein needs: {}-{} g/day".format(gram1_2,gram1_5))
# 			elif bmi >=25 and bmi <=29.9 and percent_ibw_female < 130:
# 				print("Estimated protein needs: {}-{} g/day".format(gram1_2,gram1_4))
# 			elif bmi >=25 and bmi <=29.9 and percent_ibw_female >= 130:
# 				print("Estimated protein needs: {}-{} g/day".format(gram1_1,gram1_3))
# 			# elif bmi >=30 and bmi <=39.9: 
# 			# 	gram1_5ibwf = round(ibw_female * 1.5)
# 			# 	gram2_0ibwf = round(ibw_female * 2)
# 			# 	print("Estimated protein needs: {}-{} g/day".format(gram1_5ibwf,gram2_0ibwf))
# 			else:
# 				print("BMI>40, unable to provide estimated protein needs")
# 		except:
# 			print("Unable to provide estimated protein needs")

protein_calc()

# CHO needs based on energy needs, 45-65% of kcal in g CHO/day

# Fluid needs based on energy needs, 1 mL/kcal

 

