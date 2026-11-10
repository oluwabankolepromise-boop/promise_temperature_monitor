# Temperature Monitor and Alarm Checker

## What it does
This program asks the user for a safe temperature limit and then 5 temperature readings from a machine. It stores the readings in a list, prints the highest, lowest and average, and warns if any reading is above the safe limit. It also checks the user's input, so typing a letter or an impossible temperature does not crash it.

## How to run it
Install Python 3, then run: python temperature_monitor.py

## Sample output
```
=== Temperature Monitor and Alarm Checker ===
Enter the safe temperature limit for this machine (C): 90
Enter reading 1 of 5 (C): 75
Enter reading 2 of 5 (C): abc
  Invalid input. Please type a number, for example 72.5
Enter reading 2 of 5 (C): 82.5
Enter reading 3 of 5 (C): -500
  Temperature cannot be below -273.15 C. Try again.
Enter reading 3 of 5 (C): 91.2
Enter reading 4 of 5 (C): 60
Enter reading 5 of 5 (C): 88

--- REPORT ---
Safe limit: 90.0 C

Reading 1: 75.0 C  [OK]
Reading 2: 82.5 C  [OK]
Reading 3: 91.2 C  [ALARM]
Reading 4: 60.0 C  [OK]
Reading 5: 88.0 C  [WARNING]

Highest : 91.2 C
Lowest  : 60.0 C
Average : 79.34 C

*** ALARM: 1 reading(s) above the safe limit! Check the machine. ***

Report saved to temperature_log.txt
```

## My own twist
1. **User-set safe limit:** different machines have different safe limits, so the user types the limit instead of it being fixed in the code.
2. **Status for every reading:** each reading is marked OK, WARNING (within 5 degrees of the limit) or ALARM (above the limit).
3. **Saved log file:** every report is saved with the date and time in `temperature_log.txt`, so there is a record of past checks.

## What I learned
- How to use a `while` loop with `try/except` so the program keeps asking until the input is valid, instead of crashing.
- How to split a program into functions so each part does one job.

## Author
[Your full name], ND1 Mechatronics Engineering, YabaTech.
