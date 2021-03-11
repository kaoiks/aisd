#
# Generator ciągów liczb o charakterze V-kształtnym
#

from generators.asc import asc_generator
from generators.desc import desc_generator


def vshape_generator(file, count):
    desc_count = int(count / 2)
    asc_count = count - desc_count

    desc_generator(file, desc_count)
    asc_generator(file, asc_count)