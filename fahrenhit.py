#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about fahrenhit


def calculate_fahrenhit():
    # This function is about fahrenhit

    # input
    celsius_string = input("Please enter a temperature (°C): ")
    print("")

    # process
    try:
        celsius_number = float(celsius_string)
        fahrenhit_number = (9 / 5) * celsius_number + 32

        # output
        print("{0}°C is equal to {1}°F.".format(celsius_number, fahrenhit_number))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


def main():
    # This function just call other functions

    # call functions
    calculate_fahrenhit()


if __name__ == "__main__":
    main()
