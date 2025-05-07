sName = input("Please enter your name: ")

iGrade1 = int(input(f"Hello {sName}, please enter your first test grade: "))
iGrade2 = int(input(f"Now, enter your second test grade: "))
iGrade3 = int(input(f"Enter your third test grade: "))
iGrade4 = int(input(f"Finally, enter your fourth test grade: "))

if iGrade1 <= 0 or iGrade2 <= 0 or iGrade3 <= 0 or iGrade4 <= 0:
    print("Your grades must be greater than 0.")
    raise SystemExit

sDropLowest = input(f"Now {sName}, would you like to drop your lowest grade? Y/N: ")

if sDropLowest != "Y" and sDropLowest != "y" and sDropLowest != "N" and sDropLowest != "n":
    print("Enter \"Y\" or \"N\" to Drop the Lowest Grade.")
    raise SystemExit

if sDropLowest == "Y" or sDropLowest == "y":
    print("You have chosen to drop your lowest grade.")
    
    if iGrade1 <= iGrade2 and iGrade1 <= iGrade3 and iGrade1 <= iGrade4:
        iLowest = iGrade1
        
    elif iGrade2 <= iGrade3 and iGrade2 <= iGrade4:
        iLowest = iGrade2
        
    elif iGrade3 <= iGrade4:
        iLowest = iGrade3
        
    else:
        iLowest = iGrade4
    
    iDivisor = 3

else:
    print("You have chosen not to drop your lowest grade.")
    
    iLowest = 0
    iDivisor = 4

fAvg = (iGrade1 + iGrade2 + iGrade3 + iGrade4 - iLowest) / iDivisor

# This works, but I have another way to do this further down that I use
"""
if fAvg >= 97.0:
    sLetter = "A+"
elif fAvg >= 94.0:
    sLetter = "A"
elif fAvg >= 90.0:
    sLetter = "A-"
elif fAvg >= 87.0:
    sLetter = "B+"
elif fAvg >= 84.0:
    sLetter = "B"
elif fAvg >= 80.0:
    sLetter = "B-"
elif fAvg >= 77.0:
    sLetter = "C+"
elif fAvg >= 74.0:
    sLetter = "C"
elif fAvg >= 70.0:
    sLetter = "C-"
elif fAvg >= 67.0:
    sLetter = "D+"
elif fAvg >= 64.0:
    sLetter = "D"
elif fAvg >= 60.0:
    sLetter = "D-"
else:
    sLetter = "F"
"""

# Some cool code for determining the grade letter that Brian showed us in fall 2024
if fAvg >= 90.0:
    sLetter = "A"
elif fAvg >= 80.0:
    sLetter = "B"
elif fAvg >= 70.0:
    sLetter = "C"
elif fAvg >= 60.0:
    sLetter = "D"
else:
    sLetter = "F"

if sLetter != "F":
    iAvgMod10 = int(fAvg % 10.0)
    sLetter += "+" if iAvgMod10 >= 7 or fAvg >= 100.0 else "-" if iAvgMod10 <= 3 else ""

print(f"Alright {sName}, you got an average of {fAvg:.1f} and your letter grade is a {sLetter}.")