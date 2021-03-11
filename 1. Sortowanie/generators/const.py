#
# Generator ciągów liczb o charakterze stałym
#

from random import randint


def const_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    val = randint(min_v, max_v)

    file.write(str(count))
    for _i in range(count):
        file.write('\n' + str(val))
