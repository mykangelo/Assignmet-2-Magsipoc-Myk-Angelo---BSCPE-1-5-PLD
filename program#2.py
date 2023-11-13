from pyfiglet import Figlet
from termcolor import colored, cprint
import sys
from time import sleep
import time


def clear_terminal():
    print('\033[2J\033[H')


def typeP(text, color='white', speed=0.006):
    for char in text:
        sleep(speed)
        sys.stdout.write(colored(char, color))
        sys.stdout.flush()


def get_user_input(prompt, input_type=str):
    while True:
        user_input = input(prompt)
        try:
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def loading_animation(symbols, loading_time):
    i = 0
    loading_start_time = time.time()

    while True:
        i = (i + 1) % len(symbols)
        print('\r\033[K%s Collecting...' % symbols[i], flush=True, end='')
        time.sleep(0.1)

        if time.time() - loading_start_time >= loading_time:
            break

    clear_terminal()
    print(colored('\nFinished!', 'red', attrs=['reverse', 'blink']))


def main():
    title = Figlet(font="larry3d", width=310).renderText("Programming Logic and Design")
    typeP(title, color='cyan')

    cprint("Hello! Welcome to my program that will ask for some Personal Data and display it. "
           "Let's collect some information about you.\n", "blue", attrs=["bold"], file=sys.stderr)

    while True:
        permission = input("I agree to give my Personal Data to this Program (yes/no): ")

        if permission.lower() == "yes":
            print("Let's Proceed!")
            break

        elif permission.lower() == "no":
            print("Thank You!")
            clear_terminal()
            typeP(title, color='cyan')

        else:
            print("Invalid input. Please enter 'yes' or 'no.'")
            clear_terminal()

    full_name = get_user_input("Please Enter Your Full Name: ")
    age = get_user_input("Please Enter Your Age: ", int)
    complete_address = get_user_input("Please Enter Your Complete Address: ")

    loading_symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    loading_time = 5
    loading_animation(loading_symbols, loading_time)

    info_collected = Figlet(font="smkeyboard", width=250).renderText("Information Collected")
    typeP(info_collected, color='green')

    typeP(f"\nHello! {full_name}")
    typeP(f"\nYou're {age} Years Old")
    typeP(f"\nAnd Your house is located at {complete_address}")


if __name__ == "__main__":
    main()