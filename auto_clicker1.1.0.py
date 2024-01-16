# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:06:48 2024

"""

import time
import pyautogui

def autoclicker():
    count = 0
    location_given = False

    print("                _         _____ _ _      _             _____  _   _  _____ ")
    print("     /\\        | |       / ____| (_)    | |           |  __ \| \\ | |/ ____|")
    print("    /  \\  _   _| |_ ___ | |    | |_  ___| | _____ _ __| |__) |  \\| | |  __ ")
    print("   / /\\ \\| | | | __/ _ \\| |    | | |/ __| |/ / _ \\ '__|  ___/| . ` | | |_ |")
    print("  / ____ \\ |_| | || (_) | |____| | | (__|   <  __/ |  | |    | |\\  | |__| |")
    print(" /_/    \\_\\__,_|\\__\\___/ \\_____|_|_|\\___|_|\\_\\___|_|  |_|    |_| \\_|\\_____|")
    print("                                                      -Created by lilhaerden")
    print("")
    print("")
    print("")
    print("Program Started..")
    
    while True:
        try:
            if not location_given:
                file_name = input("Please enter the name of the file on the desktop with its extension (e.g., file.png, file.jpg, or file.jpeg).\n")
                location_given = True
                
            count += 1
            locateOnScreen = pyautogui.locateOnScreen(f'C:\\Users\\root\\Desktop\\{file_name}')
            if locateOnScreen is not None:
                x, y = pyautogui.center(locateOnScreen)
                print("Clicked on the specified image!")
                pyautogui.click(x, y)
                pyautogui.moveTo(x, y + 250)

                choice = input("Image found! Press '1' to continue, '2' to exit: ")
                if choice == '1':
                    count = 0
                elif choice == '2':
                    print("Exiting the program.")
                    return
            else:
                print("Image not found. Continuing...")

        except pyautogui.ImageNotFoundException:
            print("Attempt {}: Image not found. Continuing...".format(count))
            
        time.sleep(5.0)

if __name__ == "__main__":
    autoclicker()
