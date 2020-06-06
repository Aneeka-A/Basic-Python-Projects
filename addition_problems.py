"""
File: addition_problems.py
-------------------------
This piece of code will create addition problems (with 2 digit numbers).
New problems will continue to be displayed until the user gets 3 correct answes in a row.
"""

import random
# Declaring the minimum and the maximum numbers that can appear in the question.
MIN_NUM = 10
MAX_NUM = 99
# Declaring the number of times one has to give correct answers in a row to master the addition program.
MASTER_ADD = 3

def main():
    """
    This program will produce random addition problems
    consisting of only two digit numbers that the user
    will have to answer.
    The program will have to keep producing problems until the
    user masters the addition problems, i.e., until the user
    answers 3 problems correctly in a row.
    """
    correct_in_a_row = 0
    while correct_in_a_row < 3:

        num_1 = random.randint(MIN_NUM, MAX_NUM)
        num_2 = random.randint(MIN_NUM, MAX_NUM)
        print("What is " + str(num_1) + " + " + str(num_2) + " ?")

        expected_ans = int(num_1) + int(num_2)
        expected_ans = int(expected_ans)

        inp_ans = input("Your answer: ")
        inp_ans = int(inp_ans)

        if inp_ans == expected_ans:
            correct_in_a_row += 1
            print("Correct1 You've gotten {} correct in a row.".format(correct_in_a_row))

        else:
            correct_in_a_row = 0
            print("Incorrect. The expected answer is " + str(expected_ans))

    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
