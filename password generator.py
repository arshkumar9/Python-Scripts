import secrets
import string

def password_length():
    while True:
        try:
            password_len = int(input("Enter the length of password"))
            if password_len > 0:
                return password_len
            print("Password length must be greater than 0. ")
        except ValueError:
            print("Integers only. ")

def user_response_function(msg):
    while True:
        response = input(msg).lower()
        if response == 'y' or response == 'yes':
            return True
        elif response == 'n' or response == 'no':
            return False
        print("Unable to parse value.  ")

def password_generator(len):
    passw = ''
    pass_string = ''

    while True:
        if  user_response_function("Do you want lowercase letter? [Y/N]"):
            pass_string += (string.ascii_lowercase)
        if  user_response_function("Do you want uppercase letter? [Y/N]"):
            pass_string += (string.ascii_uppercase)
        if  user_response_function("Do you want  digits? [Y/N]"):
            pass_string += (string.digits)
        if pass_string == '':
            print("You need atleast 1 character set in your password. ")
        else:
            break

    passw=''.join(secrets.choice(pass_string) for x in range(len))
    return passw 

length = password_length()
password = password_generator(length)
print(password)
