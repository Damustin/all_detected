from microbit import *
import machine
import utime
import radio
import music

# Configuracion de radio
radio.on()
radio.config(group=20, power=7)

# Distancia de activacion
DISTANCIA_ALERTA = 50

# Evita repetir la alarma constantemente
alarma_activada = False


# Mostrar alerta en pantalla
def screen_alert():
    display.show(Image.ANGRY)
    display.scroll("ALERT")


# Reproducir los sonidos originales
def sound_alert():
    music.pitch(220, 200, pin=None)
    sleep(1000)

    music.pitch(440, 200, pin=None)
    sleep(1000)

    music.pitch(880, 200, pin=None)
    sleep(1000)


# Enviar alerta a la segunda microbit
def send_alert():
    radio.send("alert")


# Medir distancia con HC-SR04
def medir_distancia():

    pin0.write_digital(0)
    utime.sleep_us(2)

    pin0.write_digital(1)
    utime.sleep_us(10)
    pin0.write_digital(0)

    tiempo = machine.time_pulse_us(pin1, 1, 30000)

    if tiempo > 0:
        distancia = tiempo / 58
        return distancia

    return None


# Programa principal
while True:

    distancia = medir_distancia()

    if distancia is not None:

        print("Distancia:", round(distancia), "cm")

        if distancia <= DISTANCIA_ALERTA and not alarma_activada:

            alarma_activada = True

            screen_alert()
            send_alert()
            sound_alert()

        elif distancia > 55:

            alarma_activada = False

    sleep(100)
