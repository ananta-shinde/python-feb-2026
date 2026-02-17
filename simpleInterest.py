principle = float(input("Enter principle :"))
rate = float(input("Enter expected rate of interest :"))
period = float(input("Enter no of years of investment :"))

interest = (principle * rate * period)/100
amount = principle + interest

print("your total investment: "+str(principle))
print("your total return : "+str(amount))