import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@$%^&*()_ [];:<>?"

def get_pw(n):
    res = ""
    for i in range(0, n):
        res = res + random.choice(char)
    return res

while True:
    print("\nNOTE - Disallowed Characters include: #£\\")
    try:
        pw_len = int(input("\nHow long of a password would you like?\n\t>> "))
        print(f"Your Password is: '{get_pw(pw_len)}'")
        break
    except:
        print("Please enter an valid integer.")
        continue

