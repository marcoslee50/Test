import random
import time

# introduction and welcome screen
name = ""
question_correct = 0  # print(money[question_correct]) to count how many correct answers
money = [0, 50, 100, 200, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
lives = 0


def intro_main():
    print("\n\n\n\n")
    print("WW      WW  EEEEEEEE  LL       CCCCCCC   OOOOOO   MM  MM  MM  EEEEEEEE      TTTTTTTT   OOOOOO ")
    print("WW  WW  WW  EE        LL      CC        OO    OO  MMM MM MMM  EE               TT     OO    OO")
    print("WW WWWW WW  EEEEEE    LL      CC        OO    OO  MM MMMM MM  EEEEEE           TT     OO    OO")
    print("WWW WW WWW  EE        LL      CC        OO    OO  MM  MM  MM  EE               TT     OO    OO")
    print("WW  WW  WW  EEEEEEEE  LLLLLL   CCCCCCC   OOOOOO   MM      MM  EEEEEEEE         TT      OOOOOO ")
    # print("\n")
    # time.sleep(1)
    print("\n                                 WHO WANTS TO BE A\n")
    print("   MM  MM  MM  II  LL      LL      II   OOOOOO   NN    NN   AAAAAA   II  RRRRRRR   EEEEEEEE")
    print("   MMM MM MMM  II  LL      LL      II  OO    OO  NNN   NN  AA    AA  II  RR    RR  EE      ")
    print("   MM MMMM MM  II  LL      LL      II  OO    OO  NN NN NN  AAAAAAAA  II  RRRRRRR   EEEEEE  ")
    print("   MM  MM  MM  II  LL      LL      II  OO    OO  NN   NNN  AA    AA  II  RR   RR   EE      ")
    print("   MM      MM  II  LLLLLL  LLLLLL  II   OOOOOO   NN    NN  AA    AA  II  RR    RR  EEEEEEEE")
    # time.sleep(1)
    print("\n                                Do you want to play?")
    print("\n                        1 for Yes (Play)      2 for No (Exit)\n")

    intro_option()


def intro_option():
    intro_answer = input()
    if intro_answer == "1":
        global name, lives, money, question_correct  # global variables for function
        name = input("Enter name: ").capitalize()  # --------------
        lives = 3
        question_answer = 0
        print(
            f"\nWelcome {name}\n\nYou start with {lives} lives and your current total is £ {money[question_correct]}\n")

        question1()

    elif intro_answer == "2":
        print("\ngame exit function")  # game end function goes here

    else:
        print("\nPlease select...\n1 for Yes (Play Game)\n2 for No (Exit Game)\n")
        intro_option()


def game_over():
    print("Game over you lost! Maybe next time!")


def answer_correct():  # message to display if answer is correct
    global name, money, lives, question_correct
    question_correct += 1
    print("Well done, you were correct!", "\nAudience applauds!")
    print(f"You now have... £ {money[question_correct]} and {lives} live(s) remaining\n\n")


tension = ["Computer please generate the correct answer", "Lets see if your correct..", "Lets hope your right!",
           "I hope you have made the right decision!"]


# 10 easy questions
def question1():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 1:")
        print("\nIs the Thames the longest river in the world?, '1' for yes, '2' for no")
        answer = input("Please enter your answer.. ")
        print(random.choice(tension))
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question2()  # change this to next question number
        elif answer == "1":
            looser()
            question2()  # change this to next question
        else:
            print("Please pick '1' for yes, '2' for no")
            question1()
    else:
        game_over()


def question2():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 2:")
        print("\nMargaret Thatcher is the UK's PM right now, '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question3()  # change this to next question number
        elif answer == "1":
            looser()
            question3()  # change this to next question number
        else:
            print("Please pick '2' for yes, '1' for no")
            question2()
    else:
        game_over()


def question3():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 3:")
        print("\nAre tomatoes fruits?, '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "1":
            answer_correct()
            question4()  # change this to next question number
        elif answer == "2":
            looser()
            question4()  # change this to next question number
        else:
            print("Please pick '2' for yes, '1' for no")
            question3()
    else:
        game_over()


def question4():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 4:")
        print("\nUSD is one the official currencies in the European Union?, '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question5()  # change this to next question number
        elif answer == "1":
            looser()
            question5()  # change this to next question number
        else:
            print("Please pick '2' for yes, '1' for no")
            question4()


def question5():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 5:")
        print("\nButterflies and moths can live up to 7 years., '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question6()  # change this to next question number
        elif answer == "1":
            looser()
            question6()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question5()
    else:
        game_over()


def question6():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 6:")
        print("\nSteam locomotive was invented in 1855 by Russian contructor A. Konovalov. '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question7()  # change this to next question number
        elif answer == "1":
            looser()
            question7()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question6()
    else:
        game_over()


def question7():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 7:")
        print("\nFirst case of covid was registered in China back in 1961. '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question8()  # change this to next question number
        elif answer == "1":
            looser()
            question8()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question7()
    else:
        game_over()


def question8():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 8:")
        print(
            "\nMount Everest is the only mountain in the world that is higher than 8000 metres, '1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question9()  # change this to next question number
        elif answer == "1":
            looser()
            question9()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question8()
    else:
        game_over()


def question9():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 9:")
        print("\nWulstan the Great was the first king of England.'1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question10()  # change this to next question number
        elif answer == "1":
            looser()
            question10()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question9()
    else:
        game_over()


def question10():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 10:")
        print("\nPython is the name of a big cat.'1' for yes, '2' for no")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "2":
            answer_correct()
            question11()  # change this to next question number
        elif answer == "1":
            looser()
            question11()  # change this to next question number
        else:
            print("Please pick '1' for yes, '2' for no")
            question10()
    else:
        game_over()


# 5 difficult questions
def question11():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 11:")
        print("\nHow many planets are there on the solar system?. 'a. eight', 'b. ten', 'c. six', 'd. five'")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "a":
            answer_correct()
            question12()  # change this to next question number
        elif answer != "b":
            print(" I'm afraid the correct answer was in fact a.")
            looser()
        else:
            print("Please pick 'a','b','c','d'")
            question11()
    else:
        game_over()


def question12():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 12:")
        print("\nWW2 began in year:'a. 1914', 'b. 1919', 'c. 1939', 'd. 1949'")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "c":
            answer_correct()
            question13()  # change this to next question number
        elif answer != "c":
            looser()
        else:
            print("Please pick 'a','b','c','d'")
            question12
    else:
        game_over()


def question13():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 13:")
        print("\nAfrica is:'a. a continent', 'b. a state', 'c. a island', 'd. a state of mind'")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "a":
            answer_correct()
            question14()  # change this to next question number
        elif answer != "a":
            looser()
            question14()  # change this to next question number
        else:
            print("Please pick 'a','b','c','d'")
            question13()
    else:
        game_over()


def question14():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 14:")
        print(
            "\nCoffee beans were first exported to Yemen by Somali merchants out of:'a. Ceylon', 'b. Poland', 'c. Nigeria', 'd. Ethiopia'")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "d":
            answer_correct()
            question15()  # change this to next question number
        elif answer != "d":
            looser()
            question15()  # change this to next question number
        else:
            print("Please pick 'a','b','c','d'")
            question14()
    else:
        game_over()  # sdfdfgdfgd


def question15():  # copy this and change question and answers
    global name, money, lives, question_correct
    if lives != 0:
        print("Question 15:")
        print("\nWinstone Churchill former British PM during WW2 was born:'a. 1874','b. 1888','c. 1901','d. 1921'")
        answer = input("Please enter your answer..")
        time.sleep(2)
        if answer == "a":
            answer_correct()
        else:
            print("Please pick 'a','b','c','d'")
    else:
        game_over()
        #code changes for change request


def winner():
    print(f"{name} Congratulations amazing you are the winner of todays game and have become a millionaire!!! ")


def looser():
    global name, money, lives, question_correct
    lives -= 1
    print(
        f"Oh no! {name}, I'm afraid that is the wrong answer...\nYou now have {lives} live(s) and still have £ {money[question_correct]} in the bank")


def game_over():
    print(f"{name} Oh no I'm afraid that's the end of the road for you today, you are a LOOSER :0(")


intro_main()