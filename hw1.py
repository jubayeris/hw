
score = float(input("Enter the score between 0 and 100: "))

if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

if 90 <= score <= 100:
        grade = 'A'
elif 80 <= score < 90:
        grade = 'B'
elif 70 <= score < 80:
        grade = 'C'
elif 60 <= score < 70:
        grade = 'D'
else:
        grade = 'F'

print(f"The grade for the score {score} is: {grade}")


