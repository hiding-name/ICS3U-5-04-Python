#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program cylinder volume calculator

import math


def volume_calculator(radius, height):
    # This'll determine the mark

    # process
    volume = math.pi * radius * radius * height
    return round(volume, 2)


def main():
    # This is asks for the user input and runs mark_finder()

    # Welcomes user
    print("Hi, this is CYLINDER VOLUME CALCULATOR.")
    input("Press Enter to continue.\n")

    while True:
        try:
            radius = int(input("What is the radius: "))
            height = int(input("What is the height: "))
            # runs volume_calculator()
            volume = volume_calculator(height=height, radius=radius)
            # output
            print("\nThe volume is " + str(volume) + " units cubed.")
            break
        except ValueError:
            print("\nInvalid input.")
            print("Try again.\n")


if __name__ == "__main__":
    main()
