'''
This BMI calculator does the BMI formula utilizing metric standards.
FORMULAS:
- BMI =  BMI = kg/m**2
- LBS_to_KG = lbs * 0.45359237
- in_to_cm = inches * 2.54
- cm_to_meters = cm * 0.01

BMI ZONES:
    below 18.5 : you're in the underweight range
    between 18.5 and 24.9 : you're in the healthy weight range
    between 25 and 29.9 : you're in the overweight range
    between 30 and 39.9 : you're in the obese range
'''

def find_standard():
    while True:
        try:
            response = input("\nWhich standard are you using?\n\t1. Imperial\n\t2. Metric\n Please make your selection >> ")
            if int(response) == 1:
                print("\nYou have chosen imperial.\n")
                return True
            else:
                print("\nYou have chosen metric.\n")
                return False
        except ValueError:
            print("Please enter a 1 or a 2.")
            continue

def bmi_zone(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def bmi():
    calc = find_standard()
    if calc:
        height_type = 'inches'
        weight_type = 'pounds'
    else:
        height_type = 'meters'
        weight_type = 'kilograms'
    while True:
        try:
            if calc:
                print("Please input your data for the following:\n")
                height = float(input(f"\tWhat is your height in {height_type}? \n\t  >> "))
                weight = float(input(f"\tWhat is your weight in {weight_type}? \n\t  >> "))
                break
            else:
                print("Please input your data for the following:\n")
                height = float(input(f"\tWhat is your hieght in {height_type}? \n\t  >> "))
                weight = float(input(f"\tWhat is your weight in {weight_type}? \n\t  >> "))
                break
        except ValueError:
            print("Please use whole numbers for the height and weight.")
            continue
    
    if calc:
        height = (height * 2.54) * 0.01
        weight = weight * 0.45359237
        print(height, weight)
    
    bmi = weight / height**2
    zone = bmi_zone(bmi)

    print(f"\n\tYour BMI is {bmi}%, and your zone is: {zone}\n")



bmi()