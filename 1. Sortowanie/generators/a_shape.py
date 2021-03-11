#
# Generator ciągów liczb o charakterze A-kształtnym
#

from generators.asc import asc_generator
from generators.desc import desc_generator


def ashape_generator(file, count):
    asc_count = int(count / 2)
    desc_count = count - asc_count

    asc_generator(file, asc_count)
    desc_generator(file, desc_count)