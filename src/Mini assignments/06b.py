#############################################################################
#Author: Mohammad El-Hassan
#Description: Mini Assingment #6b
#Date Created: 11/12/2022
#Date Modified: 11/12/2022
#############################################################################

def beginning(char, length):
    return f"{char} " * length


def middle(char, length):
    mid = (length - 2) * "  "
    return f"{char} " + f"{mid}" + f"{char}"


def create(char, leng):
    print(beginning(char, leng))
    for i in range(leng - 2):
        print(middle(char, leng))
    print(beginning(char, leng))


while True:
    character = input("Character: ")
    side = int(input("Length of side: "))
    print(create(character, side))
