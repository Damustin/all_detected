from microbit import *
import machine
import utime

while True:
    # Apagar TRIG
    pin0.write_digital(0)
    utime.sleep_us(2)

    # Enviar pulso de 10 microsegundos
    pin0.write_digital(1)
    utime.sleep_us(10)
    pin0.write_digital(0)

    # Medir el tiempo de ECHO
    tiempo = machine.time_pulse_us(pin1, 1, 30000)

    if tiempo > 0:
        # Calcular distancia en centimetros
        distancia = tiempo / 58

        print("Distancia:", round(distancia), "cm")
        display.scroll(str(round(distancia)))
    else:
        print("ERROR: No se recibe eco")
        display.show(Image.NO)

    sleep(500)
