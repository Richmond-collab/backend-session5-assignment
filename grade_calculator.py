name = input("Enter your name: ")
score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Error: Score must be between 0 and 100.")
else:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    else:
        grade = "Fail"

    print(f"\nStudent: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")