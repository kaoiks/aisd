counter = 0

def psrandomOneToThousand():
    global counter
    counter = (counter + 383) % 999
    return counter + 1
