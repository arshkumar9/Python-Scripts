
#################### Response loop - Asks whether you wanna exit or not ###############################################
def response_loop():
    while True:  # Loop for wrong answers.
        response=input("Do you want to continue?(y or n) - ")
        response=response.lower()
        if response=='n' or response=='y' or response=='yes' or response=='no':
            break
        else:
            print("Wrong input")
            continue
    if response == 'n' or response == 'no': # Conditions for only two valid answer.
       return  'break'
############################## End of response loop #######################################
