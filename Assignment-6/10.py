# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    bonus = salary * 0.05
    print(f"Your bonus is {bonus}")
else:
    print("You are not eligible for bonus")
