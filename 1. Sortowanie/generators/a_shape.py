#
# Generator ciągów liczb o charakterze A-kształtnym
#

from random import randint

def ashape_generator(file, count):
    min_v = -10e8
    max_v = 10e8

    start = randint(min_v, min_v / 2)
    tip = randint(max_v / 2, max_v)
    step = (tip - start) / (count - 1)

    for i in range(0, count, 2):
        num = int(start + i * step)
        file.write('\n' + str(num))

    for i in range(count - 1 + (count % 2), 0, -2):
        num = int(start + i * step)
        file.write('\n' + str(num))
