# Created by Jordan Leich on 7/13/2020 IMPORTANT - Must install the library called colored to use this program. You
# can install colored by using the command pip install colored


# All imports
import time
from colored import fg, attr
import restart

# Globals
reset = attr('reset')
green = fg('green')
red = fg('red')
yellow = fg('yellow')
total_rainbows = 0


# Start of the program
def start():
    global total_rainbows
    user_text = input("Enter some text or numbers to turn into a rainbow: ")
    print()
    time.sleep(1)

    user_time = float(input("Enter a time for rainbow speed (0 - Fastest, .1, .3, .5, .75, or 1 - Slowest) "))
    print()
    time.sleep(1)

    if user_time < 0:
        print(red + 'Your time number is too low!\n', reset)
        time.sleep(2)
        start()

    elif user_time > 1:
        print(red + 'Your time number is too high!\n', reset)
        time.sleep(2)
        start()

    user_loops = int(input('How many loops of rainbows do you want (150 to 270) '))
    print()
    time.sleep(1)

    if user_loops < 150:
        print(red + 'Your loop number is too low!\n', reset)
        time.sleep(2)
        start()

    elif user_loops > 270:
        print(red + 'Your loop number is too high!\n', reset)
        time.sleep(2)
        start()

    i = 1

    while i <= user_loops:
        # Displaying text into rainbow
        color = fg(i)
        print(color + user_text + reset)
        total_rainbows += 1
        time.sleep(user_time)
        i += 1

    print()
    print(green + "The rainbow has finished!\n" + reset)
    time.sleep(1)
    print(yellow + 'You have created', total_rainbows, 'rainbows!\n', reset)
    time.sleep(2)
    restart.restart()


# Initializes the beginning of the program
start()
