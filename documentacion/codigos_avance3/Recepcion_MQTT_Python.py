import os
import smtplib
import getpass
from email.message import EmailMessage

import paho.mqtt.client as mqtt

# Configuración MQTT
BROKER = "broker.hivemq.com"
PUERTO = 1883

# IMPORTANTE: cambia este tema por uno largo y único.
# Usa exactamente el mismo tema en Wokwi.
TEMA = "arduino-internet-prueba-84721"

# Datos del correo
REMITENTE = input("Tu dirección de Gmail: ")
DESTINATARIO = input("Correo destinatario: ")
CLAVE_APP = getpass.getpass("Contraseña de aplicación de Gmail: ")
correo_enviado = False


def enviar_correo():
    mensaje = EmailMessage()
    mensaje["Subject"] = "Prueba desde Arduino"
    mensaje["From"] = REMITENTE
    mensaje["To"] = DESTINATARIO
    mensaje.set_content(
        "¡Funciona! Python recibió la instrucción de la ESP32 virtual."
    )

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as servidor:
        servidor.set_debuglevel(1)
        servidor.ehlo()
        servidor.starttls()
        servidor.ehlo()
        servidor.login(REMITENTE, CLAVE_APP)
        servidor.send_message(mensaje)

    print("¡Correo enviado correctamente!")


def al_conectar(cliente, datos, flags, razon_codigo, propiedades):
    print("Conectado al servidor MQTT")
    cliente.subscribe(TEMA)
    print("Esperando mensajes...")


def al_recibir(cliente, datos, mensaje):
    global correo_enviado

    texto = mensaje.payload.decode("utf-8")
    print("Mensaje recibido:", texto)

    if texto == "ENVIAR_CORREO" and not correo_enviado:
        correo_enviado = True

        try:
            enviar_correo()
        except Exception as error:
            correo_enviado = False
            print("Error al enviar el correo:", error)


cliente = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

cliente.on_connect = al_conectar
cliente.on_message = al_recibir

print("Conectando al servidor MQTT...")
cliente.connect(BROKER, PUERTO, 60)
cliente.loop_forever()
