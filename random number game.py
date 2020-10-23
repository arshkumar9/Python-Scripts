import random
exit = False
while exit == False:
    try:
        user_answer=int(input("Guess a number between 1 to 20 : "))
    except ValueError:
        print("Please enter integers only. ")
        continue

    answer=random.randint(1,20)

    if answer==user_answer:
        print("Correct! The answer is {}.".format(answer))
    else:
        print("Wrong answer.")

    while True:
        response=input("Do you want to continue? (y or n) : ")
        response=response.lower().strip()

        if response == 'y' or response == 'yes':
            break
        elif response == 'n' or response == 'no':
            exit=True
            break
