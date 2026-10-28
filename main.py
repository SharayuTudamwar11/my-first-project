
# BMI Calculator
# My first GitHub project as a Bioengineering student

print("===== BMI CALCULATOR =====")

# Take user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Validate the input
if weight <= 0 or height <= 0:
    print("Error: Weight and height must be positive numbers.")

else:
    # Calculate BMI
    bmi = weight / (height * height)

    print("\nYour BMI is:", round(bmi, 2))

    # Display BMI category for adults
    if bmi < 18.5:
        print("BMI Category: Underweight")
    elif bmi < 25:
        print("BMI Category: Normal range")
    elif bmi < 30:
        print("BMI Category: Overweight")
    else:
        print("BMI Category: Obesity")

print("\nThank you for using the BMI Calculator!")
