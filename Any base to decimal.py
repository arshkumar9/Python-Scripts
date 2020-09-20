# Program to convert number from any base to decimal
number = None
base_from = None
while True:
    negative_flag = False

    try:
        if base_from == None:
            base_from=int(input("Enter the base : "))
            if base_from < 2:
                raise ValueError
        else:
            base_from = base_from
    except ValueError:
         print("Wrong input. Only integers are allowed.")
         continue

    if number == None:
        number = input("Enter a number : ")
    else:
        number = number

   #Not useful just for reference base_to=10
    number_size=len(number)
    number_holder=0

    try:
        for x in number:
            if x == '-':
                negative_flag=True
                continue
            if base_from>10:
                if x.lower()=='a':
                    x=10
                elif x.lower()=='b':
                    x=11
                elif x.lower()=='c':
                    x=12
                elif x.lower()=='d':
                    x=13
                elif x.lower()=='e':
                    x=14
                elif x.lower()=='f':
                    x=15
            number_size-=1
            base_raised=int(base_from)**number_size
            number_multiplied=base_raised*int(x)
            number_holder=number_holder+number_multiplied
    except ValueError:
        print("Wrong value")
        number = None 
        continue

    if negative_flag==True:
        print(number_holder*-1)
    else:
        print(number_holder)
#################### Response loop - Asks whether you wanna exit or not ###############################################
    while True:  # Loop for wrong answers.
        response=input("Do you want to continue?(y or n) - ")
        if response.lower()=='n' or response.lower()=='y':
            break
        else:
            print("Wrong input")
            continue
    if response == 'n': # Conditions for only two valid answer.
        break
    else :
        number=None
        base_from=None
############################## End of response loop #######################################
