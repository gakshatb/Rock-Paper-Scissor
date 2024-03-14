import random
import pyttsx3


def text_output(text=None):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def winner(comp=None, user=None):
    if comp == user:
        return
    elif comp == 's' and user == 'p' or comp == 'p' and user == 'r' or comp == 'r' and user == 's':
        return -1
    else:
        return 1


def main():
    possible_choice = ['s', 'p', 'r']
    print("WELCOME GAMER!")
    text_output("WELCOME GAMER!")
    text_output("Rules Are Simple")
    print("S for Scissor")
    print("R for Rock")
    print("P for Paper")
    flag = True
    while flag:
        print("____________________________________________________________________")
        print("Enter Number Of Round You Want To Play: ", end="")
        text_output("Enter Number Of Round You Want To Play")
        no_round = input()
        while True:
            if no_round.isnumeric():
                no_round = int(no_round)
                break
            else:
                print("Please Enter A Valid Number: ", end="")
                text_output("Please Enter A Valid Number")
                no_round = input()
        print("GOOD-LUCK")
        text_output("Good Luck")
        user_score = 0
        comp_score = 0
        no_draw = 0
        print("_________________***BEGIN***_________________")
        text_output("Begin")
        while no_round > 0:
            comp_choice = random.choice(possible_choice)
            print("Enter Your Choice: ", end="")
            text_output("Enter Your Choice")
            user_choice = input().lower()
            if user_choice not in possible_choice:
                print("Please Choose According To Given Instruction")
            while True:
                if user_choice not in possible_choice:
                    print("Please Enter A Valid Choice: ", end="")
                    text_output("Please Enter A Valid Choice")
                    user_choice = input().lower()
                else:
                    break
            deci = winner(comp_choice, user_choice)
            if deci == 1:
                user_score += 1
                print("YOU WON")
                text_output("You Won")
            elif deci == -1:
                comp_score += 1
                print("YOU LOST")
                text_output("You Lost")
            else:
                no_draw += 1
                print("IT'S A DRAW")
                text_output("Its A Draw")
            no_round -= 1
        text_output("SCORES ARE")
        print("_________________SCORE-BOARD_________________")
        print(f"Your Final Score: {user_score}")
        text_output(f"Your Score: {user_score}")
        print(f"COMP Final Score: {comp_score}")
        print(f'Number Of Draw: {no_draw}')
        text_output(f"Total Number Of Draw: {no_draw}")
        if user_score > comp_score:
            print("Congrats You Won The Game")
            text_output("Congrats You Won The Game")
        elif user_score < comp_score:
            print("Better Luck Next Time")
            text_output("Better Luck Next Time")
        else:
            print("It's A Draw Let's Play Again")
            text_output("It's A Draw. Let's Play Again")
        print("_________________***********_________________")
        print("Do You Want To Play Again Y/N: ", end="")
        text_output("Do You Want To Play Again Yes or No: ")
        response = input().lower()
        while True:
            if response == 'y':
                print("Good Choice")
                break
            elif response == 'n':
                flag = False
                print("____________________________________________________________________")
                break
            else:
                print("Please Enter A Valid Response: ", end="")
                text_output("Please Enter A Valid Response")
                response = input().lower()
    print("GAME IS OVER!")
    text_output("GAME IS OVER!")
    print("THANK YOU FOR YOUR TIME")
    print("HAVE A NICE DAY")
    text_output("HAVE A NICE DAY")


if __name__ == '__main__':
    main()
