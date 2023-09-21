print("Welcome to the tip calculator")
total_bill = float(input("What is the total bill $ "))
tip = float(input("What percent of tip you want to give 10 12 15 "))
split = float(input("In how many ppl you wanna split the bill"))
# tip_percent = tip / 100
# total_tip_amt = total_bill * tip_percent
total_tip_amt = (total_bill * tip) / 100
bill = total_bill + total_tip_amt
pay = bill / split
tpay = round(pay,2)
print(f"Each person will pay {tpay}")