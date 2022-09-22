# lets me uses sleep
from time import sleep


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter A, B, C or D").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num +=1

    display_score(correct_guesses, guesses)
def check_answer(answer, guess):

    if answer == guess:
        print("Correct, +1 point")
        return 1
    else:
        print("WRONG +0 point")
        return 0

def display_score(correct_guess, guesses):
    print("---------------")
    print()
    print("RESULTS")
    print()
    print("---------------")
    print()

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")

    score = int((correct_guess/len(questions))*100)
    print("Your score is: "+str(score)+"%" " Out of 100")
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
    statement_generator("You will be asked 10 questions about osu and its other game modes, all questions will be Multi choice", "-")
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
# questions
questions = {
    "Who is the current number one player": "D",
    "Who is the most well known osu player": "B",
    "Who created the WYSI meme": "B",
    "Who has held the number one spot for the most time": "A",
    "Which of these countries has not won the OWC": "C",
    "Who is the number one Taiko player": "D",
    "What is the current osu standard pp record": "C",
    "Who won the first ever OWC": "D",
    "When was osus first version released": "B"
}
options = [["A. RyuK", "B. Utami", "C. WhiteCat", "D. MreKk"],
           ["A. Shigetora", "B. BTMC", "C. WhiteCat", "D. Kariyu"],
           ["A. Aireu", "B. Shigetora", "C. BTMC", "D. Aricin"],
           ["A. MreKk", "B. Cookiezi", "C. WhiteCat", "D. FlyingTuna"],
           ["A. America", "B. China", "C. Canada", "D. United Kingdom"],
           ["A. Ney", "B. Minekuchi", "C. nameless_ll", "D. syaron105"],
           ["A. 1156", "B. 1217", "C, 1241", "D. 1329"],
           ["A. Japan", "B. Australia", "C. Germany", "D. Taiwan"],
           ["A. 1999", "B. 2007", "C. 2013", "D. 2002"]]

new_game()




