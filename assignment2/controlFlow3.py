# MOSES MUIRURI NJAU
# SCT211-0002/2022
def calculate_bmi(weight_kg):
    return weight_kg

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"

weight = float(input("Enter your weight in kilograms: "))
bmi = calculate_bmi(weight)
category = determine_bmi_category(bmi)
print(f"You are categorized as: {category}")
