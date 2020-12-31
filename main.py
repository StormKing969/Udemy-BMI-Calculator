print("Welcome to the BMI Calculator")
unit = input("The default settings for the calculator is the Imperial System\n"
             "Do you wish to change to the American System? ").lower()
weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

en_bmi = weight / (height ** 2)
us_bmi = (weight * 0.45359237) / ((height * 3.2808) ** 2)

if unit == "yes":
    print("Your BMI is : " + str(int(us_bmi)))
else:
    print("Your BMI is : " + str(int(en_bmi)))