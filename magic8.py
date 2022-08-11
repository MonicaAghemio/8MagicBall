import sys
import random

ans = True

while ans:
    question = input("Ask a question: ")

    answers = random.randint(1, 8)

    if question == " ":
        sys.exit()

    elif answers == 1:
        print("It is certain")

    elif answers == 2:
        print("Outlook good")

    elif answers == 3:
        print("You can rely on it")

    elif answers == 4:
        print("Ask again later")

    elif answers == 5:
        print("Don't count on it")

    elif answers == 6:
        print("Cannot predict now")

    elif answers == 7:
        print("Outlook not so good")

    elif answers == 8:
        print("Without a doubt")
