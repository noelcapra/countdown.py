# Countdown Timer in Python

A program that counts down from a user-specified number of seconds and displays the remaining time in HH:MM:SS format.

## How to Run
1. Ensure you have Python installed.
2. Download `countdown.py`.
3. Run the program from the terminal using the command: `python countdown.py`
4. Enter the number of seconds you want to count down.

## What I Learned / Concepts Demonstrated
* Using the `time` module, specifically `time.sleep(1)` to pause the program for one second.
* `for` loops with `range()` to iterate downwards.
* Integer division (`//` or `int(x / ...)`) and the modulo operator (`%`) to convert total seconds into hours, minutes, and seconds.
* Formatted string literals (f-strings) to display time neatly with leading zeros (e.g., `f"{hours:02}"`).
* Basic user input.
