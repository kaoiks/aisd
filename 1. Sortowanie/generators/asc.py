#
# Generator ciągów liczb o charakterze rosnącym
#

from random import randint


def asc_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    start = randint(min_v, min_v / 2)
    end = randint(max_v / 2, max_v)
    step = (end - start) / (count - 1)

    for i in range(count):
        num = int(start + i * step)
        file.write('\n' + str(num))
