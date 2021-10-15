# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/15/2021
# This is the Volume of Cylinder program
# The user enters in the radius and height of a cylinder in mm
# The program displays the volume

import math


def calculate_volume(radius, height):
    # calculate volume

    volume = math.pi * (radius * radius) * height

    return volume


def main():
    # This function gets radius, height, and displays volume

    # input
    radius_string = input("Enter in radius (mm): ")
    height_string = input("Enter in height (mm): ")
    print("")

    # process
    try:
        radius = int(radius_string)
        height = int(height_string)

        # call functions
        finished_math = calculate_volume(radius, height)

        print("Volume = {0} mm²".format(finished_math))

    except Exception:
        print("Invalid input")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
