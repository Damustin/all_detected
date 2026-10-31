def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P0, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P0, 0)

    tiempo = pins.pulse_in(
        DigitalPin.P1,
        PulseValue.HIGH,
        30000
    )

    distancia = tiempo * 0.0343 / 2

    if tiempo > 0 and distancia < 10:
        basic.show_icon(IconNames.HEART)
    else:
        basic.clear_screen()

    basic.pause(100)

basic.forever(on_forever)
