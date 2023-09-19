age=int(input("Enter your age: "))
total_days = 32850
total_month = 1080
total_week = 4680
# week_of_user = age  * 52
user_total_days = total_days - age * 365
user_total_month = total_month - age * 12
user_total_week = (90 - age) * 52
print(f"You have {user_total_days} days,{user_total_week} weeks and {user_total_month} months left ")
