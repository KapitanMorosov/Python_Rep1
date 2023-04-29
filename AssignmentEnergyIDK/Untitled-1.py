AccountNum = input("Account Number: ")
AccountNum = int(AccountNum)
AmountGJ = input("Amount of GJ used: ")
AmountGJ = int(AmountGJ)
AmountKWH = input("Amount of electricty used: ")
AmountKWH = int(AmountKWH)
Month = input("Month: ")
Month = int(Month)

TypeE = input("Electricty plan: ")
TypeG = input("Gas plan: ")
Province = input("Province, enter the abbreviated version ex: (AB for Alberta): ")

monthlyF = 120.62
tax = 0 

if Province == "AB" or "BC" or "MB" or "NT" or "NU" or "QC" or "SK" or "YK":
    tax = 0.05
    print(tax)

if Province == "ON":
    tax = 0.13
    print(tax)

if Province == "NB" or "NL" or "NS" or "PE":
    tax = 0.15
    print(tax)   