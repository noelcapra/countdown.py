import time

def countdown():
    time1 = int(input("How many seconds do you want to countdown?"))

#Time1 is how many seconds total, 0 is the end goal, meaning stops at 1. -1 is where to begin.
#In this case since its -1 it reverses mytime1 and starts at the last nymber and counts down.
    for x in range(time1, 0, -1):
        seconds =x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        #Formats, the number "2" means how many total spaces, the number "0" equals what fills the space
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)


countdown()