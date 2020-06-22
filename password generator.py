import response
import random
from  string import ascii_letters ,digits
userchoice_size = None
userchoice_syntax_lower = None
userchoice_syntax_upper = None
userchoice_syntax_number = None

while True:
    try:

        if userchoice_size == None:
            userchoice_size = int(input("Enter the length of the password : "))
        else:
            userchoice_size = userchoice_size

        if userchoice_syntax_lower == None:
            userchoice_syntax_lower = input("Do you want lower case letter?(y or n) ").lower()
        else:
            userchoice_syntax_lower = userchoice_syntax_lower
        if userchoice_syntax_lower != 'y' and  userchoice_syntax_lower != 'yes' and userchoice_syntax_lower != 'n' and  userchoice_syntax_lower != 'no':
            raise ValueError
        
        if userchoice_syntax_upper == None:
            userchoice_syntax_upper = input("Do you want upper case letter?(y or n) ").lower()
        else:
            userchoice_syntax_upper = userchoice_syntax_upper
        if userchoice_syntax_upper != 'y' and  userchoice_syntax_upper != 'yes' and userchoice_syntax_upper != 'n' and  userchoice_syntax_upper != 'no':
            raise ValueError

        if userchoice_syntax_number == None:
            userchoice_syntax_number = input("Do you want numbers?(y or n) ").lower()
        else:
            userchoice_syntax_number = userchoice_syntax_number
        if userchoice_syntax_number != 'y' and  userchoice_syntax_number != 'yes' and userchoice_syntax_number != 'n' and  userchoice_syntax_number != 'no':
            raise ValueError

    except ValueError:
        print("Wrong Input")
        continue
    if (userchoice_syntax_lower == 'n' or userchoice_syntax_lower == 'no') and (userchoice_syntax_upper == 'n' or userchoice_syntax_upper == 'no') and (userchoice_syntax_number == 'n' or userchoice_syntax_number == 'no'):
        print("Not every possible character choice can be no!")
        continue
    counter=0
    password=''
    choice_list=[1,2,3]
    while counter <= userchoice_size:
        choice_number = random.choice(choice_list)
        if choice_number == 1:
            if userchoice_syntax_upper == 'y' or userchoice_syntax_upper == 'yes':
                password = password + str(random.choice(ascii_letters.upper())) 
                counter += 1
        if choice_number == 2:
            if userchoice_syntax_number=='y' or userchoice_syntax_number == 'yes':
                password = password + str(random.choice(digits))
                counter += 1
        if choice_number == 3:
            if userchoice_syntax_lower == 'y' or userchoice_syntax_lower == 'yes':
                password= password + str(random.choice(ascii_letters.lower())) 
                counter += 1
    print (password)
    if response.response_loop()=='break':
        break
    else:
        userchoice_size = None
        userchoice_syntax_lower = None
        userchoice_syntax_upper = None
        userchoice_syntax_number = None
