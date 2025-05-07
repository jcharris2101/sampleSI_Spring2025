fPrncInv = float(input("What's the principal investment? "))
fIntRate = float(input("What's the interest rate? ")) / 100.0
iCompound = int(input("How many times per year is the interest compounded? "))
fNumPeriods = float(input("How many years will it earn interest? "))

fResult = fPrncInv * (1.0 + fIntRate / iCompound) ** (iCompound * fNumPeriods)

print(f"At the end of {fNumPeriods} years you will have ${fResult:,.2f}.")
