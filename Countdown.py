import time

def countdown(t):
    while t:
        # Learned about divmod(), which creates a tuple of the quotient and remainder of a number, and it's second argument.
        # The quotient is assigned to min, and the remainder is assigned to sec. 
        min, sec = divmod(t, 60)

        # The {:02d} string format ensures that 2 digits will be display to emulator the clock display
        # .format is used to introduce the min and sec into the string format
        timer = "{:02d}:{:02d}".format(min, sec)

        # The carriage return, or \r, is used to keep writing code to the same line of the terminal, So Cool!!!
        print(timer, end="\r")

        # Program then sleeps for 1 second, and decrements the t variable to the new time remaining
        time.sleep(1)
        t -= 1

    print("Time's up!")

# Takes users input
t = input("Please enter a time (in seconds): ")

# Run the program!
countdown(int(t))

# Thanks to Harshit Bhai - The HackerxGuy on YouTube for the tutorial!!!