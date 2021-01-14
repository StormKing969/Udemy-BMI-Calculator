print("Welcome to the BMI Calculator")
unit = input("The default settings for the calculator is the Imperial System\n"
             "Do you wish to change to the American System? ").lower()
weight = int(input("Enter your weight: "))
height = int(input("Enter your height: "))

en_bmi = weight / (height ** 2)
us_bmi = int((weight * 0.45359237) / ((height / 3.2808) ** 2))

if unit == "yes":
    if us_bmi < 18.5:
        print(f"Your BMI is {us_bmi} and you are underweight")
    elif 25 > us_bmi >= 18.5:
        print(f"Your BMI is {us_bmi} and you are normal weight")
    elif 25 <= us_bmi < 30:
        print(f"Your BMI is {us_bmi} and you are overweight")
    elif 30 <= us_bmi < 35:
        print(f"Your BMI is {us_bmi} and you are obese")
    else:
        print(f"Your BMI is {us_bmi} and you are clinically obese")
else:
    if en_bmi < 18.5:
        print("Your BMI is : " + str(int(en_bmi)))
        print("You are underweight")
    elif 25 > en_bmi >= 18.5:
        print("Your BMI is : " + str(int(en_bmi)))
        print("You are normal weight")
    elif 25 <= en_bmi < 30:
        print("Your BMI is : " + str(int(en_bmi)))
        print("You are overweight")
    elif 30 <= en_bmi < 35:
        print("Your BMI is : " + str(int(en_bmi)))
        print("You are obese")
    else:
        print("Your BMI is : " + str(int(en_bmi)))
        print("You are clinically obese")