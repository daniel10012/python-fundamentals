
investment = float(input("investment amount"))
ir = float(input("interest rate in percentage")) / 100
years = float(input("number of years to invest"))

future_value = round(investment * (1+ir)* years, 2)

print("the future value is : " + str(future_value))


'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''