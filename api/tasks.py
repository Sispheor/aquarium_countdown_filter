import time


def countdown_task(seconds):
    print("Turn off the aquarium filter for %s seconds" % seconds)
    time.sleep(int(seconds))
    print("Turn back on the aquarium filter")
