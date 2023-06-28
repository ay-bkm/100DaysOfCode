height = float(input("enter your height in m: "))
weight = float(input("enter your weight inkg: "))
bmi = round(weight / (height * height))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight!")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You are normal weight!")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight!")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese!")
else:
    print(f"Your bmi is {bmi}, You are clinically obese!")