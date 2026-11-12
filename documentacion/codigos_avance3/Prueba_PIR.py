from microbit import *

uart.init(115200)

while True:
    v = pin0.read_analog()
    uart.write(str(v))
    uart.write('.')
    sleep(100)

    if pin0.read_digital():
        display.show(Image.DIAMOND_SMALL)
    else:
        display.show(Image.ANGRY)

    sleep(100)
    display.clear()
    sleep(100)
