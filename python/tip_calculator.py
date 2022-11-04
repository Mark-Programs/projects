'''
Python program to process data to determine a tip
1. Inquire about total bill cost
2. Ask if the bill needs to be split between people
3. Ask what percentage tip will be given
4. Display the total cost each person will pay, including tip percentage
'''

while True:
    while True:
        total_bill = input("\n\tWhat is the total for the bill?\n\t\t>> ")
        try:
            if float(total_bill):
                total_bill = float(total_bill)
                break
        except ValueError:
            print("Please enter a valid bill number. (ie: 85.27)")
            continue
        break

    while True:
        bill_split = input("\n\tHow many people will contribute to the bill?\n\t\t>> ")
        try:
            if int(bill_split):
                bill_split = int(bill_split)
                if bill_split == 0:
                    bill_split = 1
                break
        except ValueError:
            print("Please enter a valid integer. (ie: 4)")
            continue
        break

    while True:
        server_tip = input("\n\tPlease type the percentage for the tip\n\t\t>> ")
        try:
            if int(server_tip):
                server_tip = int(server_tip) / 100
                break
        except ValueError:
            print("Please enter a valid integer. (ie: 10)")
            continue
        break
        
    break

try:
    total_bill = total_bill / float(bill_split)
except ZeroDivisionError:
    pass

to_pay = (total_bill * server_tip) + total_bill

print("=" * 60)
print(f"\tEach of the {bill_split} person(s) should pay: ${to_pay:.2f}")
print("=" * 60)
