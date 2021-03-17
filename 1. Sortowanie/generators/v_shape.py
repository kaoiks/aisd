#
# Generator ciągów liczb o charakterze V-kształtnym
#

from random import randint

def vshape_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    start = randint(max_v / 2, max_v)
    tip = randint(min_v, min_v / 2)
    step = (start - tip) / (count - 1)

    for i in range(0, count, 2):
        num = int(start - i * step)
        file.write('\n' + str(num))

    for i in range(count - 1 + (count % 2), 0, -2):
        num = int(start - i * step)
        file.write('\n' + str(num))
