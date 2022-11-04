
def verify_number(e):
    while True:
        var1 = input(f"""
            Please input the {e} number.
                        >> """)
        try:
            if float(var1):
                var1 = float(var1)
                return var1
        except ValueError:
            print("Please enter in only numbers")

def operator_type():
    while True:
        types = ['x', '+', '-', '/', '**', '*']
        item = input('''
            Please enter in an operator type. 
                x  = multiplication
                /  = division
                +  = addition
                -  = subtraction
                ** = exponents
                        >> ''')
        if item in types:
            return item

def do_math(n1, n2, operator):
    match operator:
        case "x":
            return n1 * n2
        case "*":
            return n1 * n2
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "/":
            return n1 / n2
        case "**":
            return n1 ** n2    

def restart():
    res = input(""" 
            Would you like to use the calculator again?
                1. Yes
                2. No
                    >> """)
    if res != '1':
        print("\n\n\tThank you for using the Python Calculator\n\n")
        exit()
    print("\n\n")

def graphic():
    print('''
  _________________________
 |  _____________________  |
 | |   Welcome to the    | |
 | |  Python Calculator  | |
 | |_____________________| |
 |  ___   ___   ___   ___  |
 | | 7 | | 8 | | 9 | | + | |
 | |___| |___| |___| |___| |
 | | 4 | | 5 | | 6 | | - | |
 | |___| |___| |___| |___| |
 | | 1 | | 2 | | 3 | | x | |
 | |___| |___| |___| |___| |
 | | . | | 0 | | = | | / | |
 | |___| |___| |___| |___| |
 |_________________________|
''')

graphic()

while True:
    number1 = verify_number("first")
    operator = operator_type()
    number2 = verify_number("second")
    res = do_math(number1, number2, operator)
    print(f"""
                The result is:  {res}""")
    restart()
    