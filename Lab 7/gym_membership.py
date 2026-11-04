def parse_plan(code):
    plan, months = code.split('-')
    return plan.upper(), int(months)

def calculate_bmi(data):
    weight, height = data.split(',')
    return round(float(weight) / (float(height) ** 2), 1)

def average_workout(minutes):
    values = [int(m) for m in minutes.split()]
    return sum(values) // len(values)

def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result)

if __name__ == "__main__":
    main()
