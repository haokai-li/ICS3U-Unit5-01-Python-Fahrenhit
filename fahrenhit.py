#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program is about fahrenheit


def calculate_fahrenheit():
    # This function is about fahrenheit

    # input
    celsius_string = input("Please enter a temperature (°C): ")
    print("")

    # process
    try:
        celsius_number = float(celsius_string)
        fahrenheit_number = (9 / 5) * celsius_number + 32

        # output
        print("{0}°C is equal to {1}°F.".format(celsius_number, fahrenheit_number))

    except Exception:
        # output
        print("You didn't enter an integer.")

    print("\nDone.")


def main():
    # This function just call other functions

    # call functions
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
