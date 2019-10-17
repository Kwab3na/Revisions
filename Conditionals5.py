weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))

bmi = weight / (height * height)

if bmi < 19:
    print("Underweight")
elif 19 >= bmi or bmi <= 25:
    print("Normal")
elif 26 >= bmi or bmi <= 30:
    print("Overweight")
else:
    print("Obese")

print("Your bmi is " + str(round(bmi)))