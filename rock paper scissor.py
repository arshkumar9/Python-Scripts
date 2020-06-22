import response
import random
while True:

    possible_list=['rock','paper','scissor']
    users_choice=input("Rock, paper or scissor ? ")
    users_choice=users_choice.lower()
    cpu_choice=random.choice(possible_list) 
    try:
        if users_choice in possible_list:
            print("CPU's Choice : ",end='')
            if users_choice==cpu_choice:
                print(users_choice,"\nStalemates!" )
            elif users_choice == 'rock':
                if cpu_choice == 'paper':
                    print("Paper")
                    print("CPU Wins!")
                else:
                    print("Scissor")
                    print("You Win! ")
            elif users_choice == 'paper':
                if cpu_choice == 'scissor':
                    print("Scissor")
                    print("CPU Wins! ")
                else:
                    print("Rock")
                    print("You Win!")
            elif users_choice == 'scissor':
                if cpu_choice=='paper':
                    print("Paper")
                    print("You Win!")
                else:
                    print('Rock')
                    print('CPU Wins')
        else:
            raise ValueError
    except ValueError:
        print("Wrong Selection !")
    if response.response_loop()=='break':
        break



