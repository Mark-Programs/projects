import random

def comp_select():
    ''' Generate random number for computer's play '''
    # randomly choose a item out of the list
    x = random.choice(plays)
    return plays.index(x)

def keep_playing():
    ''' Menu called to determine to keep playing the game '''
    while True:
        usr = input("\n\tWould you like to play again?\n\t1. Yes\n\t2. No\n\t >> ")
        res = 0
        try:
            if usr == '1': res = 1
            break
        except:
            print("For 'Yes', please press '1' and hit enter\nFor 'No', please press 2 and hit enter.")
    return True if res == 1 else False


def who_won(usr, comp) -> int:
    ''' Take usr and comp ints to determine winner '''
    # 0 = rock, 1 = paper, 2 = scissors
    # returns usr_wins: True/False
    if usr == 0:
        return True if comp == 2 else False
    if usr == 1:
        return True if comp == 0 else False
    if usr == 2:
        return True if comp == 1 else False
    if usr == 3:
        return True
    


plays = ["Rock", "Paper", "Scissors"]

print("\n\tWelcome to Rock, Paper, Scissors.")

comp_score = 0
user_score = 0

while True:
    while True:
        try:
            user = int(input("\n\tPlease make your selection:" + 
                            "\n\t\t1. Rock" + 
                            "\n\t\t2. Paper" + 
                            "\n\t\t3. Scissors" + 
                            "\n\t\t\t>> ")) - 1
            if user >= 0 and user < 3:
                print(f"\t\t>>> You have selected {plays[user]}")
                break
            if user == 3:
                print("\t\t>>> You have selected to play the JOKER.")
                break
        except:
            print("Not a valid selection, please enter 1, 2 or 3.")


    computer = comp_select()
    if user != 3:
        result = who_won(user, computer)
    if user == computer:
        print(f"\n  \tIt is a draw! you both selected {plays[user]}")
    elif user == 3:
        print(f"\n  \t  The JOKER beats {plays[computer]}")
        user_score += 1
    elif result == True:
        print(f"\n  \t  {plays[user]} beats {plays[computer]}")
        user_score += 1
    else:
        print(f"\n  \t  {plays[user]} loses to {plays[computer]}")
        comp_score += 1

    replay = keep_playing()
    if replay == True:
        print("_" * 80)
        print(f"\n>> You have chosen to keep playing. >> Current Score is = Player: {user_score}, Computer: {comp_score}")
        print("_" * 80)
        continue
    else:
        print("- " * 40)
        print("\n")
        if user_score > comp_score:
            print("\tYou won overall")
        elif user_score < comp_score:
            print("\tYou lost overall")
        else:
            print("\tYou tied overall.")
        print(f"\n\n\tThe final score is:\n\t\tPlayer:   {user_score}\n\t\tComputer: {comp_score}")
        print("\n\t < < < Thank you for playing!  Please come back again soon! > > >\n\n")
        break

