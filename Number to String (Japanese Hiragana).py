def NumberChooser(number):
    if number == 0:
        return "ゼロ"
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
        return "いち"
    elif number == 2:
        return "に"
    elif number == 3:
        return "さん"
    elif number == 4:
        return "よん"
    elif number == 5:
        return "ご"
    elif number == 6:
        return "ろく"
    elif number == 7:
        return "なな"
    elif number == 8:
        return "はち"
    elif number == 9:
        return "きゅう"

def Dozens(number):
    if number < 10:
        return Unit(number)
    BackDigit = number % 10
    FrontDigit = number//10
    if FrontDigit == 1:
        return "じゅう" + Unit(BackDigit)
    else:
        return Unit(FrontDigit) + "じゅう" + Unit(BackDigit)

def Hundreds(number):
    if number < 100:
        return Dozens(number)
    BackDigit = number % 100
    FrontDigit = number//100
    if FrontDigit == 1:
        return "ひゃく" + Dozens(BackDigit)
    elif FrontDigit == 3:
        return  "さんびゃく" + Dozens(BackDigit)
    elif FrontDigit == 6:
        return  "ろっぴゃく" + Dozens(BackDigit)
    elif FrontDigit == 8:   
        return "はっぴゃく" + Dozens(BackDigit)
    else:
        return Unit(FrontDigit) + "ひゃく" + Dozens(BackDigit)

def Thousands(number):
    if number < 1000:
        return Hundreds(number)
    BackDigit = number % 1000
    FrontDigit = number//1000
    if FrontDigit == 1:
        return "せん" + Hundreds(BackDigit)
    elif FrontDigit == 3:
        return "さんぜん" + Hundreds(BackDigit)
    elif FrontDigit == 8:
        return "はっせん" + Hundreds(BackDigit)
    else:
        return Unit(FrontDigit) + "せん" + Hundreds(BackDigit)

def TenOfThousands(number):
    if number < 10000:
        return Thousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Unit(FrontDigit) + "まん" + Thousands(BackDigit)

def HundredThousands(number):
    if number < 100000:
        return TenOfThousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Dozens(FrontDigit) + "まん" + Thousands(BackDigit)
#
def Million(number):
    if number < 1000000:
        return HundredThousands(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Hundreds(FrontDigit) + "まん" + Thousands(BackDigit)

def TensOfMillions(number):
    if number < 10000000:
        return Million(number)
    BackDigit = number % 10000
    FrontDigit = number//10000
    return Thousands(FrontDigit) + "まん" + Thousands(BackDigit)

def HundredMillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Unit(FrontDigit) + "おく" + TensOfMillions(BackDigit)

def Billions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Dozens(FrontDigit) + "おく" + TensOfMillions(BackDigit)

def TensOfBillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Hundreds(FrontDigit) + "おく" + TensOfMillions(BackDigit)

def HundredBillions(number):
    if number < 100000000:
        return TensOfMillions(number)
    BackDigit = number % 100000000
    FrontDigit = number//100000000
    return Thousands(FrontDigit) + "おく" + TensOfMillions(BackDigit)

print("Enter number to convert: ")
integer = int(input())

print(NumberChooser(integer))

# for i in range(1,1000000):
#     print(i, NumberChooser(i))