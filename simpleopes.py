import random

def user_input():
    my_input = int(input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n"))
    return my_input

def random_simple():
    num1 = str(random.randint(2, 9))
    num2 = str(random.randint(2, 9))
    ops = ["+", "-", "*"]
    opr = random.choice(ops)
    return num1 + " " + opr + " " + num2

def random_square():
    num_sq = random.randint(11, 29)
    return num_sq

rights = 0
N = 0

while N != 5:
    level = user_input()
    if level == 1:
        while N < 5:
            num_simple = random_simple()
            print(num_simple)
            while True:
                try:
                    ans_simple = int(input())
                    if ans_simple == eval(num_simple):
                        print("Right!")
                        rights += 1
                        N += 1
                        break
                    else:
                        print("Wrong!")
                        N += 1
                        break
                except ValueError:
                    print("Incorrect format.")
                    continue
    elif level == 2:
        while N < 5:
            num_sq = random_square()
            print(num_sq)
            while True:
                try:
                    ans_sq = int(input())
                    if ans_sq == num_sq ** 2:
                        print("Right!")
                        rights += 1
                        N += 1
                        break
                    else:
                        print("Wrong!")
                        N += 1
                        break
                except ValueError:
                    print("Wrong format! Try again.")
                    continue
    else:
        print("Incorrect format.")
        continue


save_or_no = input(f"Your mark is {rights}/5. Would you like to save the result? Enter yes or no.\n")
yes_list = ["yes", "y", "YES", "Yes"]
if save_or_no in yes_list:
    name = input("What is your name?\n")
    my_file = open("results.txt", "a+")
    if level == 1:
        my_file.write(f"{name}: {rights}/5 in level {level} (simple operations with numbers 2-9).\n")
        my_file.close()
    elif level == 2:
        my_file.write(f"{name}: {rights}/5 in level {level} (integral squares of numbers 11-29).\n")
        my_file.close()
    print('The results are saved in "results.txt".')
else:
    exit()
