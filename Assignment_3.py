# Problem: A company wants a program that will calculate the weekly paycheck for an employee based on how many hours they worked. For this company, an employee earns $20 an hour for the first 40 hours that they work. The employee earns overtime, $30 an hour, for each hour they work above 40 hours.
# Assignment: Write a program that will calculate the weekly paycheck for an employee based on how many hours they worked. The program should ask the user to enter the number of hours worked and then display the paycheck amount.

# Pseudocode:

    # Input: Number of hours worked
        # Process: Calculate paycheck amount
        # Conditional: If hours worked is greater than or equal to 40, then calculate overtime pay
            # If condition true: Calculate overtime pay and add regular pay
            # If condition false: Calculate regular pay
    # Output: Paycheck amount

# Working Code:

def output_paycheck_amount(hours_worked):
    hours_worked = int(input("Enter the number of hours worked: "))
    overtime_pay = 30
    regular_pay = 20
    if hours_worked >= 40:
        overtime_hours = hours_worked - 40
        regular_hours = hours_worked - overtime_hours
        overtime_pay = overtime_hours * overtime_pay
        regular_pay = regular_hours * regular_pay
        total_pay = overtime_pay + regular_pay
        print("Your total pay is $", total_pay)
    else:
        total_pay = hours_worked * regular_pay
        print("Your total pay is $", total_pay)

output_paycheck_amount(50)