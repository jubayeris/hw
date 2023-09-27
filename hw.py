try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    if hours < 0 or rate < 0:
        raise ValueError("Hours and rate must be positive numbers")

    if hours > 40:
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        regular_hours = 40
        salary = (regular_hours * rate) + (overtime_hours * overtime_rate)
    else:
        salary = hours * rate

    print(f"The total salary is: ${salary:.2f}")

except ValueError as ve:
    print(f"Error: {ve}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
