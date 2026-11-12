radio.set_group(20)
radio.set_transmit_power(7)

PIR = DigitalPin.P0

def screen_alert():
    basic.show_icon(IconNames.ANGRY)
    basic.show_string("ALERT")

def sound_alert():
    pins.analog_set_pitch_pin(AnalogPin.P1)

    pins.analog_pitch(220, 200)
    basic.pause(1000)
    pins.analog_pitch(440, 200)
    basic.pause(1000)
    pins.analog_pitch(880, 200)
    basic.pause(1000)

def send_alert():
    radio.send_string("alert")

def on_received_string(mensaje):
    if mensaje == "alert":
        screen_alert()
        sound_alert()

radio.on_received_string(on_received_string)

movimiento_anterior = 0
#serial.redirect_to_usb()

def on_forever():
    #basic.show_icon(IconNames.HEART)
    global movimiento_anterior

    movimiento = pins.digital_read_pin(PIR)
    #movimiento = pins.analog_read_pin(AnalogPin.P0)

    #serial.write_value("x", movimiento)

    if movimiento == 1:
        led.plot(1, 1)
        basic.pause(50)
        led.unplot(1, 1)
    else:
        led.plot(2, 2)
        basic.pause(50)
        led.unplot(2, 2)

    if movimiento == 1 and movimiento_anterior == 0:
        #if False:
        screen_alert()
        send_alert()
        sound_alert()

        movimiento_anterior = movimiento

    basic.pause(100)
    #basic.show_icon(IconNames.SAD)

    led.plot(0, 0)
    basic.pause(50)
    led.unplot(0, 0)

basic.forever(on_forever)
