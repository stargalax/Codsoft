import random
import array

def generate_password(length):
    MAX_LEN = length
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LO = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~',
               '>', '*', '(', ')', '<']

    COMBINED_LIST =  UP + LO + SYMBOLS

    digit = random.choice(DIGITS)
    upper = random.choice(UP)
    lower = random.choice(LO)
    symbol = random.choice(SYMBOLS)

    temp_pass = digit + upper + lower + symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

  
    password = ""
    for x in temp_pass_list:
        password = password + x

    return password
#main
length = int(input("Enter how long the password must be: "))
if length<7:
    print("Password must be atleast 8 character long")
else:
    r = generate_password(length)
    print("Generated Password:",r)
