# lets me uses sleep
from time import sleep


def new_game():

    guesses = []
    correct_guess = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)

        question_num +=1

# Allows me to make the code look cool

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# this code will display the instructions and what the user should expect

def instructions():
    print()
    statement_generator("Welcome to the quiz quest, Today I will be testing you on your knowledge of osu!", "?")
    sleep(2)
    statement_generator("You will be asked 10 questions about osu and its other game modes, all questions will be true or false", "-")
    sleep(2)
    statement_generator("All questions MUST be answered with either A, B, C or D", "!")
    sleep(2)
    statement_generator("If You ever want to leave this quiz, just type in 'xxx' at any time to leave", "x")
    sleep(2)
    statement_generator("Good luck Have Fun", "*")



instructions()
# asks the user to input their name or nickname
name = input("Please put your name here or a nickname if you want to play anonymously: ")
sleep(2)
print()
sleep(2)
print("Hello {}, Thank you for participating".format(name))

point = 0

rounds_played = 0

print()
play_start = input("Would you like to begin")

if play_start == "yes":
         print("Ok, then here is your first question")

elif play_start == "no":
    print("Ok, Thank you for your time {}".format(name))

else:
    print("Ok, have a nice day {}".format(name))

questions = {
    "Who is the current number one player"
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
    ""
}
options = [["A. RyuK", "B. Utami", "C. WhiteCat", "D. MreKk"],
           []]






