# letters for referencing in cipher
# char length: 26
letters = 'abcdefghijklmnopqrstuvwxyz'
# char length: 42
special = '`~!@#$%^&*()_+-=[]}{;:",<.> /?\\|' + "'0123456789"

def prog_start():
    while True:
        choice = input('''
            Welcome to the Caesar Cipher Program
                 ___________________________
                |                           |
                |  What do you wish to do?  |
                |- - - - - - - - - - - - - -|
                |   1. Encrypt              |
                |   2. Decrypt              |
                |   3. Exit                 |
                |___________________________|

                    >> ''')
        val = '123'
        if choice not in val:
            print("\nNot a valid selection, please enter a 1, 2, or 3.")
            continue
        else:
            if choice == '3':
                print("\n\t Thank you for using the Caesar Cipher.")
                exit()
            else:
                break
        
    
    text = input("\n\tPlease enter in your message: \n\t\t >> ")
    while True:
        shift_value = input("\n\tHow many characters would you like to shift by? \n\t\t >> ")
        if int(shift_value): break
        else: print("Please enter a valid number.")

    if choice == '1': mode = 'encrypt'
    else: 
        mode = 'decrypt'

    cipher(text, int(shift_value), mode)
    

def cipher(message, shift, mode):
    res = ''
    for letter in message.lower():
        if letter in letters:
            pos = letters.index(letter)
            if shift > len(letters):
                shift = shift % len(letters)
            if mode == 'encrypt':
                new_pos = pos + shift
                if new_pos >= len(letters): new_pos -= 26
            else:
                new_pos = pos - shift
                if new_pos < 0: new_pos += 26
            res += letters[new_pos]
        else:
            pos = special.index(letter)
            if shift > len(special):
                shift = shift % len(special)
            if mode == 'encrypt':
                new_pos = pos + shift
                if new_pos >= len(special): new_pos -= 43
            else:
                new_pos = pos - shift
                if new_pos < 0: new_pos += 43
            res += special[new_pos]

    if mode == 'encrypt':
        print(f'''
                                     ||
            The Encrypted message is : {res}
                                     ||''')
        print("\n\t >> Message encryption completed <<")
    else:
        print(f'''
                                     || 
            The Decrypted message is : {res}
                                     ||''')
        print("\n\t >> Message decryption completed <<")


# use for interface requesting program restart (do another)
def replay():
    while True:
        choice = input('''
                |  What do you wish to do?      |
                |- - - - - - - - - - - - - - - -|
                |   1. Use the program again    |
                |   2. Exit                     |
                                >> ''')
        val = '12'
        if choice not in val:
            print("\nNot a valid selection, please enter a 1, or 2.")
            continue
        else:
            if choice == '1':
                break
            else:
                print("\n\t Thank you for using the Caesar Cipher.\n")
                exit()


while True:
    prog_start()
    res = replay()



