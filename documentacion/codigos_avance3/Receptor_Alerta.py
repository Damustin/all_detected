from microbit import *
import radio
import music

# Configuracion de radio
radio.on()
radio.config(group=20, power=7)


# Mostrar alerta en pantalla
def screen_alert():

    display.show(Image.ANGRY)
    sleep(2000)
    display.scroll("ALERT")


# Reproducir sonidos
def sound_alert():

    music.pitch(220, 200, pin=None)
    sleep(1000)

    music.pitch(440, 200, pin=None)
    sleep(1000)

    music.pitch(880, 200, pin=None)
    sleep(1000)


# Recibir y procesar alerta
def on_received_string(mensaje):

    if mensaje == "alert":

        print("ALERTA RECIBIDA")

        screen_alert()
        sound_alert()

        display.show(Image.HAPPY)


# Programa principal
display.show(Image.HAPPY)

print("Esperando alertas...")

while True:

    mensaje = radio.receive()

    if mensaje is not None:

        print("Mensaje recibido:", mensaje)

        on_received_string(mensaje)

    sleep(50)
