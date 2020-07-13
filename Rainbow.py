# Created by Jordan Leich on 7/13/2020 IMPORTANT - Must install the library called colored to use this program. You
# can install colored by using the command pip install colored


# All imports
import time
from colored import fg, attr
import restart

# Globals
reset = attr('reset')
good_color = fg('green')


# Start of the program
def start():
    user_text = input("Enter some text or numbers to turn into a rainbow: ")
    print()
    time.sleep(2)

    user_time = float(input("Enter a time for rainbow speed (0 - Fastest, .1, .3, .5, .75, or 1 - Slowest) "))
    print()
    time.sleep(2)

    i = 0

    while i <= 255:
        # Displaying text into rainbow
        color = fg(i)
        print(color + user_text + reset)
        time.sleep(user_time)
        i += 1

    print()
    print(good_color + "Rainbow finished!\n" + reset)
    time.sleep(1)
    restart.restart()


# Initializes the beginning of the program
start()
