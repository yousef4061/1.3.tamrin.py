weight = float(input("enter weight (kg): "))
height_cm = float(input("enter height (cm): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 24.9:
    category = "normal weight"
elif bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"bmi: {bmi:.1f} - {category}")

#محاسبات وضعیت بدنی