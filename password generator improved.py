import secrets
import string


def password_length():

    try:
        password_len = int(input("Enter the length of password"))
        return password_len

    except ValueError:
        print("Wrong value. ")

def password_generator(len):

    try:
        passw = ''
        pass_string = ''

        lower = input("Do you want lowercase letter? [Y/N]")
        upper = input("Do you want uppercase letter? [Y/N]")
        digit = input("Do you want  digits? [Y/N]")

    except ValueError:
        print("Unable to parse value.")


    if upper == 'y' or upper == 'yes':
        pass_string += (string.ascii_uppercase)

    if digit == 'y' or digit == 'yes':
        pass_string += (string.digits)

    if lower == 'y' or lower == 'yes':
        pass_string += (string.ascii_lowercase)
    
    passw=''.join(secrets.choice(pass_string) for _ in range(len))

    return passw 

length = password_length()
password = password_generator(length)
print(password)
