pin = 2203
count = 0
while count < 3:
    supplied_pin = int(input("Enter your PIN: "))

    if supplied_pin == pin:
        print('Access granted')
        break #when the condition is true (the correct pin is inputted) then this breaks the loop so it does not go back to the start of the loop.
    else:
        print('Access denied. Try again.')
        count = count + 1
else:
    print('Access banned - 3 attempts, please contact your bank to reset your PIN.')
    
    this has been changed

# Orlane's version

import getpass


PIN = 6924
max_attempts = 3

while max_attempts > 0:
    supplied_pin = getpass.getpass("Enter your PIN: ")
    if int(supplied_pin) != PIN:
        max_attempts -= 1
        print("Incorrect PIN. You have", max_attempts, "attempts left.")
    else:
        print("Success!")
        break