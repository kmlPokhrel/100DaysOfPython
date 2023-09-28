print("Welcome to the rollercoster")
height = float(input("Enter your height"))
sum = 0
if height > 120:
    age = float(input("Enter your age"))
    picture = input("do you wanna take pictures: Y/N")
    if picture == 'Y' or 'y':
        sum += 3
    if age < 12:
        sum += 17
    elif age > 18:
        sum += 20
    else:
        sum += 10

else:
    print("you aren't allowed to ride rollercoster")
print(f"pay ${sum}")

