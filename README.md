# Autoclicker

This Python script checks the location of a specified file on the desktop and performs a click operation when the file is found.

## Usage

1. **Install Python:**
   - Download and install Python from the [official Python website](https://www.python.org/downloads/).

2. **Install Required Libraries:**
   - Open a terminal or command prompt and run the following command:
     ```
     pip install pyautogui
     ```

3. **Run the Script:**
   - Navigate to the directory where the script is located in the terminal or command prompt.
   - Execute the following command to start the script:
     ```
     python auto_clicker1.1.0.py
     ```
     or
     ```
     python3 auto_clicker1.1.0.py
     ```

4. **Notes During Usage:**
   - The program continuously checks for the file until it is found.
   - After clicking on the found file, it prompts the user to continue or exit.
   - A counter has been added to track the attempts made to find the file.

## Changes

- Added the ability to check .png, .jpg, and .jpeg files regardless of file type.
- Added a counter to track attempts made to find the file.
- Improved outputs for better understanding and user-friendliness.
