from random import choices
from string import ascii_letters
from sys import stdout, stdin


def easy_as_a_pie(first_arg: int, second_arg: int):
    print(first_arg + second_arg)


def rational_insanity(second_arg: int):
    first_arg = int(stdin.readline())
    return first_arg + second_arg


def turn_up_the_heat(first_arg: int, second_arg: int):
    stdout.write(str(first_arg + second_arg))


def intentional_bullshit(first_arg: int, second_arg: int):
    with open("".join(choices(ascii_letters, k=10)), "w") as out_f:
        out_f.write(str(first_arg + second_arg))
