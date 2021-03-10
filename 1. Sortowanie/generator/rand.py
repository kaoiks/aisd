#
# Generator ciągów liczb o charakterze losowym
#

from random import randint

def random_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    file.write(str(count))
    for _i in range(count):
        num = randint(min_v, max_v)
        file.write('\n' + str(num))