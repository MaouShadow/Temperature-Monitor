# project Title:
Temperature Monitor and Alarm Checker.
A beginner Python program that checks readings from a machine and warns when it is running too hot.

## What it does
1. Asks for a safe temperature limit.
2. Collects 5 temperature readings and stores them in a list.
3. Prints the highest, lowest and average reading.
4. Warns about every reading above the safe limit.


## How to run
```
python temperature_monitor.py
```

## Sample Output
=== Temperature Monitor and Alarm Checker ===

Enter the safe temperature limit (degrees C): 100
Enter reading 1 of 5: 70
Enter reading 2 of 5: 72
Enter reading 3 of 5: 71
Enter reading 4 of 5: 73
Enter reading 5 of 5: 70

--- Results ---
Readings : [70.0, 72.0, 71.0, 73.0, 70.0]
Highest  : 73.0
Lowest   : 70.0
Average  : 71.20
Trend    : STEADY (no change)

--- Alarm check ---
Reading 1:    70.0  ->  OK
Reading 2:    72.0  ->  OK
Reading 3:    71.0  ->  OK
Reading 4:    73.0  ->  OK
Reading 5:    70.0  ->  OK

All readings are within the safe limit of 100.0. Machine is OK.

## My twist (extra feature)
- **Severity levels:** each reading is labelled `OK`, `WARNING` (above the limit) or `CRITICAL` (more than 10 degrees above the limit).
- **Trend detection:** the program compares the first and last readings and reports whether the machine is `RISING`, `FALLING` or `STEADY`, so an engineer can spot overheating early.
- A final alarm summary counts how many readings broke the limit

## What I learned
Functions keep code organised. Splitting the program into small functions like get_number() and classify() made it easier to read and fix.
Never trust user input. Typing letters crashed my first version. Using try/except inside a while loop fixed it, and checking for an empty list avoids dividing by zero.
Loops and lists work together. One loop collected the readings into a list, and another checked each one against the limit.
if/elif/else handles more than two outcomes. I used it to sort readings into OK, WARNING and CRITICAL, and the order of the checks matters.
Windows are event-driven. In tkinter, the program waits for a button click instead of running top to bottom.
Next step: save readings to a file and let the user choose how many to enter.

## Author
Adebola Ridwan Okikiade, ND1 Mechatroinics Engineering, Enginerring department, Yabatech.
