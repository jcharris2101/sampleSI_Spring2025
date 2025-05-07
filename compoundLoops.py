sLINE_BREAK = "-----------------------------------------------"
sDEC_FORMAT = ",.2f"

while True:
    try:
        fDeposit = float(input("Please enter the initial deposit: "))

        if fDeposit <= 0.0:
            print("Please enter in an amount greater than 0!")
            continue

        break

    except ValueError:
        print("Please enter in a numeric value!")

while True:
    try:
        fRate = float(input("Please enter the interest rate as a percentage: ")) / 100.0 / 12.0

        if fRate <= 0.0:
            print("Please enter in an amount greater than 0!")
            continue

        break

    except ValueError:
        print("Please enter in a numeric value!")

while True:
    try:
        iMonths = int(input("Please enter the number of months: "))

        if iMonths <= 0:
            print("Please enter in an amount greater than 0!")
            continue

        break

    except ValueError:
        print("Please enter in a numeric value!")

while True:
    try:
        fGoal = float(input("Please enter the goal (can be 0): "))

        if fGoal < 0.0:
            print("Please enter in an amount greater than or equal to 0!")
            continue

        break

    except ValueError:
        print("Please enter in a numeric value!")

print(sLINE_BREAK)

fNewAmnt = fDeposit
for iMonth in range(1, iMonths + 1):
    print(f"Month  {iMonth:02}  :  Account Balance is: ${(fNewAmnt := fNewAmnt + fNewAmnt * fRate):12{sDEC_FORMAT}}")

if fGoal > 0.0:
    print(sLINE_BREAK)

    if fDeposit <= fGoal:

        fNewAmnt = fDeposit
        iMonth = 0
        while fNewAmnt <= fGoal:
           fNewAmnt += fNewAmnt * fRate
           iMonth += 1

        print(f"It will take {iMonth} months to reach the goal of $ {fGoal:{sDEC_FORMAT}}")

    else:
        print(f"You've already reached your goal of ${fGoal:{sDEC_FORMAT}}!")