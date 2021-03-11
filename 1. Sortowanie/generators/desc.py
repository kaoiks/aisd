#
# Generator ciągów liczb o charakterze malejącym
#

from random import randint


def desc_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    start = randint(max_v / 2, max_v)
    end = randint(min_v, min_v / 2)
    step = (start - end) / (count - 1)

    for i in range(count):
        num = int(start - i * step)
        file.write('\n' + str(num))
