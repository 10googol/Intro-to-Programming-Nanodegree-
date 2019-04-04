# IPND Stage 2 Final Project

# Program function flow is as follows in main program:
# Note: All functions are called from the main program
#       unless otherwise noted.
# 1. call main - in the main portion of the program to get things rolling
# 2. call user_menu - gets users difficulty choice and returns
#    initial program variables quiz_list and quiz_level.
# 3. call find_blanks - returns blank_no (blank number) of
#    current answer in quiz the user is trying to answerself.
# 4. call get_answer - returns correct answer, as well program control,
#    and checks number of attempts.
# 5. call check_answer - called by get_answer to verify answer answer
#    and provided boolean returns for program logic control.
# 6. call fill_answer_number - indexes through quiz_list and fills in
#    blanks depending on what was returned by find_blanks.

easy = """A ___1___ is created with the def keyword. You specify the inputs
          a ___1___ takes by adding ___2___ separated by commas between the
          parentheses. ___1___s by default return ___3___ if you don't specify
          the value to return. ___2___ can be standard data types such as
          string, number, dictionary, tuple, and ___4___ or can be more
          complicated such as objects and lambda functions."""

medium = """In python a ___1___ like a list can be ___2___ through one
            character at at time. A major difference between ___1___s and list
            is ___1___s are ___3___. However, you can use the ___4___ operator
            to point a ___1___ variable to a new ___1___. Using a triple quotes
            allows a user to assign a variable to a ___5___ paragraph.
            There are many popular methods available to be used with ___1___s
            two extremely useful ones are the ___6___ and ___7___ methods."""

hard = """Python has two kinds of loops. The first is the ___1___ loop which
          repeats a statement or group of statements while a given condition
          is ___2___. It tests the condition before executing the loop body.
          The second is the ___3___ loop which executes a sequence of
          statements multiple times and abbreviates the code that manages the
          loop variable. These two kinds of loops can also be ___4___ loops.
          Loops also have three control statements. The ___5___ statement that
          terminates the loop statement and transfers execution to the
          statement immediately following the loop. The ___6___ statement
          that causes the loop to skip the remainder of its body and immediately
          retest its condition prior to reiterating. And finally, the ___7___
          statement which is used when a statement is required syntactically
          but you do not want any command or code to execute."""

answersEasy = ["function", "arguments", "none", "list"]
answersMedium = ["string", "iterated", "immutable", "assignment", "multiline",
                 "replace", "split"]
answersHard = ["while", "true", "for", "nested", "break", "continue", "pass"]

blank_test = True   # Boolean variable used for flow control in main program


###########################################################
################Begin Function Definition##################
def user_menu():
    # Function to provide the user with a menu of choices
    # for quiz difficulty and return the initial variables
    # quiz_level and quiz_list for the rest of the program.
    while True:
        print "\nChoose quiz difficulty: 1. Easy / 2. Medium / 3. Hard \n"
        num = raw_input("-> ")
        if num == '1' or num == '2' or num == '3':
            break
        else:
            print "\nPlease enter a number 1 - 3!"

    if num == '1':
        quiz_list = easy.split()
        quiz_level = 'easy'
    elif num == '2':
        quiz_list = medium.split()
        quiz_level = 'medium'
    else:
        quiz_list = hard.split()
        quiz_level = 'hard'

    print "\nYou have chosen the " + quiz_level + " quiz! \n"

    return quiz_level, quiz_list

def fill_answer_number(answer, quiz_list, blank_no):
    # Function to search through the passed in quiz_list
    # and replace the blank_no with the correct answer
    # as determined by get_answer and check_answer
    index = 0   # variable for indexing through quiz_list
    for i in quiz_list:
        if "." in blank_no and i == blank_no:
            quiz_list[index] = i.replace(blank_no, answer) + "."
        else:
            quiz_list[index] = i.replace(blank_no, answer)
        index += 1

def find_blanks(quiz_list):
    # Function is used to find a blank that needs to be
    # answered in the quiz. It returns the blank_no i.e.
    # ___1___ to be used in the fill_answer_number function
    # to search on the blanks that match that number and replace
    # them with the correct answer or it will return 0. It also returns
    # True or False to be to indicate whether or not a blank was found.
    # This function is the crux of the whole program as the main function
    # use it for logic control.
    for i in quiz_list:
        if '_' in i:
            return i, True
    return 0, False

def get_answer(choice, blank_no):
    # Function to get answer from user and check whether the
    # answer is correct or not by calling check_answer. This is
    # where the logic to count number of tries is implemented as well.
    count = 1   # Variable to keep track of answer tries.
    maxAnswertries = 5  # variable used for determining and calculating
                        # user attempts to answer
    while True:
        answer = raw_input("What should be substituted in for " + blank_no + " ? " )
        correct = check_answer(answer, choice, blank_no)
        if count == maxAnswertries:
            print "That's " + maxAnswertries + " attempts please try again!"
            return False
        elif correct == True:
            return answer
        else:
            print "You have " + str(maxAnswertries - count) + " attempts left."
            count += 1

def check_answer(answer, choice, blank_no):
    # Checks answer from get_answer against correct answers
    # in the answersEasy, answersMedium, and answersHard list
    # which is selected depending on the difficulty level (quiz_level)
    # passed into choice.
    # If answer is correct return True
    answer_list = []    # list to hold answers to the quiz from answersEasy, answersMedium, and answersHard
    index = 0   # Index for answer_list based on blank_no

    blank_no_len = len(blank_no)
    if blank_no_len > 1:
        extra_char = blank_no[blank_no_len - 1]
        blank_no = blank_no.strip(extra_char)
        blank_no = blank_no.strip('_')
    else:
        blank_no = blank_no.strip("_")

    index = int(blank_no) - 1

    if choice == 'easy':
        answer_list = answersEasy
    elif choice == 'medium':
        answer_list = answersMedium
    else:
        answer_list = answersHard

    if answer == answer_list[index]:
        return True

def main():
    # Main function to be called in main section of Program.
    # This functions calls user_menu, find_blanks, get_answer,
    # fill_answer_number and controls program flow.
    quiz_level, quiz_list = user_menu()

    print "You will get 5 guesses per blank."

    while True:
        blank_no, blank_test = find_blanks(quiz_list)
        if not blank_test:
            print "\nCONGRAGULATIONS!!! You have solved the quiz!!! \n"
            print ' '.join(quiz_list)
            break
        else:
            print "\nThe current paragraph reads as follows:"
            print ' '.join(quiz_list) + "\n"
            answer = get_answer(quiz_level, blank_no)
            if not answer:
                break
            else:
                fill_answer_number(answer, quiz_list, blank_no)
################End Function Definition##################
#########################################################



##################################################
################Begin MAIN Program################
main()
################End MAIN Program##################
##################################################
