# Day 2 Excercise 3    Math Munipulation and f-strings

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆


# Write your code below this line 👇
age_as_int = int(age)
years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12


# minutes added to code
mins_left = years_left * 525600


message = f"You have {days_left}days, {weeks_left}weeks, \
     {months_left}months,and {mins_left}minutes"
print(message)
