def NumberChooser(number):
    if number == 0:
        return "Zero"
    elif len(str(number)) == 1:
        return Unit(number) 
    elif len(str(number)) == 2:
        return Dozens(number)
    elif len(str(number)) == 3:
        return Hundreds(number)
    elif len(str(number)) == 4:
        return Thousands(number)
    elif len(str(number)) == 5:
        return TenOfThousands(number)
    elif len(str(number)) == 6:
        return HundredThousands(number)
    elif len(str(number)) == 7:
        return Million(number)
    elif len(str(number)) == 8:
        return TensOfMillions(number)
    elif len(str(number)) == 9:
        return HundredMillions(number)
    elif len(str(number)) == 10:
        return Billions(number)
    elif len(str(number)) == 11:
        return TensOfBillions(number)
    elif len(str(number)) == 12:
        return HundredBillions(number)
def Unit(number):
    if number == 0:
        return ""
    elif number == 1:
        return "Ichi"
    elif number == 2:
        return "Ni"
    elif number == 3:
        return "San"
    elif number == 4:
        return "Yon"
    elif number == 5:
        return "Go"
    elif number == 6:
        return "Roku"
    elif number == 7:
        return "Nana"
    elif number == 8:
        return "Hachi"
    elif number == 9:
        return "Kyuu"

def Dozens(number):
    if number < 10:
        return Unit(number)
    BackDigit = number % 10
    FrontDigit = number//10
    if FrontDigit == 1:
        return "Jyuu " + Unit(BackDigit)
    else:
        return Unit(FrontDigit) + " Jyuu " + Unit(BackDigit)

def Hundreds(number):
    if number < 100:
        return Dozens(number)
    BackDigit = number % 100
    FrontDigit = number//100
    if FrontDigit == 1:
        return "Hyaku " + Dozens(BackDigit)
    elif FrontDigit == 3:
        return  "San Byaku " + Dozens(BackDigit)
    elif FrontDigit == 6:
        return  "Rop Pyaku " + Dozens(BackDigit)
    elif FrontDigit == 8:   
        return "Hap Pyaku " + Dozens(BackDigit)
    else:
        return Unit(FrontDigit) + " Hyaku " + Dozens(BackDigit)

def Thousands(number):
    if number < 1000:
        return Hundreds(number)
    BackDigit = number % 1000
    FrontDigit = number//1000
    if FrontDigit == 1:
        return "Sen " + Hundreds(BackDigit)
    elif FrontDigit == 3:
        return "San Zen " + Hundreds(BackDigit)
    elif FrontDigit == 8:
        return "Has Sen " + Hundreds(BackDigit)
    else:
        return Unit(FrontDigit) + " Sen " + Hundreds(BackDigit)

def TenOfThousands(number):
    if number < 10000:
        return Thousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Unit(FrontDigit) + " Man " + Thousands(BackDigit)

def HundredThousands(number):
    if number < 100000:
        return TenOfThousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Dozens(FrontDigit) + " Man " + Thousands(BackDigit)
#
def Million(number):
    if number < 1000000:
        return HundredThousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Hundreds(FrontDigit) + " Man " + Thousands(BackDigit)

def TensOfMillions(number):
    if number < 10000000:
        return Million(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Thousands(FrontDigit) + " Man " + Thousands(BackDigit)

def HundredMillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Unit(FrontDigit) + " Oku " + TensOfMillions(BackDigit)

def Billions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Dozens(FrontDigit) + " Oku " + TensOfMillions(BackDigit)

def TensOfBillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Hundreds(FrontDigit) + " Oku " + TensOfMillions(BackDigit)

def HundredBillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Thousands(FrontDigit) + " Oku " + TensOfMillions(BackDigit)

print("Enter number to convert: ")
integer = int(input())

print(NumberChooser(integer))

# for i in range(100000,1000000):
#     print(i, NumberChooser(i))