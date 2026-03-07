def calc_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    bmi = weight / (height ** 2)

    if bmi <= 18.5:
        category = "Underweight"
    elif bmi <= 25:
        category = "Normal weight"
    elif bmi <= 30:
        category = "Overweight"
    elif bmi > 35:
        category = "Obesity class I"

    print(f"BMI: {bmi:.2f}, Category: {category}")

    return bmi


result = calc_bmi(70, 1.75)
print("Calculated BMI:", result)
