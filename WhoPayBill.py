import random
ppl = input("Enter name of ppl doing party")
Lppl= ppl.split(", ")
t = len(Lppl)
bill = random.randint(0,t-1)
billPay = Lppl[bill]
print(f"{billPay} , will pay the bill ")
