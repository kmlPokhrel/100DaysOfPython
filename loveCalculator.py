

print("Welcome to love calculator")
name1 = input("Enter first name")
name2 = input("Enter second name")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = str(true) + str(love)
ttl = int (love_score)
if ttl > 90 or ttl < 10:
    print(f"Your score is {ttl} , you go together like coke and mentos")
elif ttl > 40 and ttl < 50:
    print(f"yout score is {ttl}, you are alright together")
else:
    print(f"your score is {ttl}.")