monthly_investment = float(input("Enter monthly invested value :"))
rate = float(input("Enter expected rate of interest :"))
period = float(input("Enter no of months of investment :"))


principle = monthly_investment * period
time = period/12.0

interest = (principle * rate * time)/100
amount = principle + interest

print("your total investment: "+str(principle))
print("your total return : "+str(amount))