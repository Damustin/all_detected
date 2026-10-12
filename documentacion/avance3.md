
# Informe de Avance 3 — Octubre 2026

## 08/10/2026 — Montaje físico y pruebas con sensores PIR

### Preparación de los materiales

Durante esta clase logramos reunir nuevamente todos los materiales y componentes necesarios para continuar con el desarrollo de nuestro sistema de alarma.

Cabe destacar que, en clases anteriores, sufrimos el robo de parte de los materiales del proyecto, situación que dificultó nuestro avance y retrasó la realización de las pruebas físicas.

A pesar de este inconveniente, conseguimos reunir nuevamente los elementos necesarios y retomar las actividades previstas.

Trabajamos con dos micro:bit, placas de expansión, sensores PIR, cables de conexión y una computadora para realizar la programación y comprobar el funcionamiento de los dispositivos.

De esta manera, pudimos retomar las pruebas físicas del sistema de alarma.

### Montaje y conexiones físicas

Comenzamos conectando los sensores PIR a las placas de expansión de las micro:bit mediante cables de conexión.

Para realizar el montaje utilizamos las siguientes conexiones:

| Sensor PIR | Placa de expansión | Función |
|------------|--------------------|---------|
| VCC (+) | 3V | Alimentación positiva |
| GND (-) | GND | Tierra o negativo |
| OUT (S) | P0 | Señal de detección de movimiento |

El pin P0 se utiliza para recibir la señal digital enviada por el sensor cuando detecta movimiento.

Por su parte, los pines VCC y GND permiten alimentar el sensor.

Una vez realizadas las conexiones, comenzamos las pruebas para comprobar si los sensores detectaban movimiento y si la micro:bit respondía mediante una alerta visual y sonora.

### Objetivo de las pruebas

Nuestro objetivo principal era conseguir que los sensores PIR detectaran movimiento y que la micro:bit activara una alarma sonora.

Para ello utilizamos como base el código que veníamos desarrollando durante las clases anteriores en MakeCode, utilizando el lenguaje Python.

En esta etapa nos concentramos únicamente en comprobar el funcionamiento de los sensores y la activación de la alarma.

### Evolución del sistema de alarma sonora

Durante las primeras etapas del proyecto realizamos simulaciones en Tinkercad, utilizando un componente piezoeléctrico para reproducir los sonidos de la alarma.

En aquella versión, el código utilizaba el pin P1 como salida de sonido para el piezoeléctrico.

Posteriormente decidimos retirar ese componente y aprovechar el parlante integrado de la micro:bit V2.

De esta manera, simplificamos el montaje físico, evitando la necesidad de conectar un dispositivo adicional para reproducir los sonidos.

### Código original — Versión con piezoeléctrico

El siguiente código corresponde a una versión anterior que utilizamos como base para desarrollar el sistema de alarma.

Incluye funciones para detectar movimiento, mostrar una alerta visual, reproducir sonidos mediante un piezoeléctrico y transmitir una señal por radio.

```python
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

def on_forever():
    global movimiento_anterior

    movimiento = pins.digital_read_pin(PIR)

    if movimiento == 1 and movimiento_anterior == 0:
        screen_alert()
        send_alert()
        sound_alert()

        movimiento_anterior = movimiento

        basic.pause(100)

basic.forever(on_forever)
```

Aunque este código contiene funciones de comunicación por radio, todavía no habíamos comenzado a realizar pruebas de esa funcionalidad.

Nuestro objetivo durante esta etapa era comprobar únicamente la detección de movimiento y la activación de la alarma.

### Adaptación al parlante integrado de la micro:bit

Al comenzar a trabajar con los componentes físicos, decidimos utilizar el parlante integrado de la micro:bit V2 en lugar del piezoeléctrico.

Para esta adaptación podemos utilizar las funciones de música de MakeCode, sin necesidad de conectar un dispositivo de sonido externo.

La siguiente función representa una propuesta para las próximas pruebas:

```python
def sound_alert():
    music.set_built_in_speaker_enabled(True)

    music.play_tone(220, 200)
    basic.pause(1000)
    music.play_tone(440, 200)
    basic.pause(1000)
    music.play_tone(880, 200)
    basic.pause(1000)
```

Esta versión mantiene la secuencia de tres sonidos utilizada anteriormente, pero aprovecha el parlante integrado de la micro:bit.

Su funcionamiento deberá verificarse durante las próximas pruebas físicas.

### Dificultades durante las pruebas

Durante la clase realizamos varios intentos para comprobar el funcionamiento de los sensores PIR.

A pesar de revisar las conexiones entre las micro:bit, las placas de expansión y los sensores, no conseguimos obtener la respuesta esperada.

Nuestro objetivo era que, al detectar movimiento, la micro:bit activara una alerta visual y sonora.

Sin embargo, no logramos confirmar correctamente la detección de movimiento.

### Pruebas individuales de los sensores PIR

Ante las dificultades encontradas, decidimos realizar pruebas específicas utilizando MakeCode.

Para ello utilizamos códigos más sencillos, destinados únicamente a comprobar si los sensores PIR detectaban movimiento y enviaban una señal a la micro:bit mediante el pin P0.

Realizamos varios intentos, pero continuamos sin obtener los resultados esperados.

A partir de estas pruebas, llegamos a la hipótesis de que los sensores PIR podrían encontrarse dañados, aunque todavía no pudimos confirmar definitivamente esta situación.

### Preparación para la próxima clase

Durante el fin de semana posterior a la clase conseguimos dos sensores PIR nuevos para repetir las pruebas físicas.

Nuestro próximo objetivo será conectar nuevamente los componentes y comprobar que los sensores puedan detectar movimiento correctamente.

Una vez que logremos verificar la detección, continuaremos con la activación de la alarma sonora mediante el parlante integrado de la micro:bit.

También quedó pendiente revisar el control de la variable `movimiento_anterior` para permitir nuevas detecciones después de que el sensor deje de registrar movimiento.

Por el momento, seguimos trabajando en esta primera etapa del proyecto, sin avanzar todavía hacia el envío de mensajes o notificaciones a otros dispositivos.

### Conclusión

Aunque no conseguimos completar satisfactoriamente las pruebas físicas, esta clase representó un avance importante para el proyecto.

Después de las dificultades ocasionadas por el robo de materiales, logramos reunir nuevamente los componentes necesarios, retomar el montaje físico y realizar diferentes pruebas de funcionamiento.

También pudimos identificar posibles problemas en los sensores PIR y establecer los próximos pasos para continuar desarrollando nuestro sistema de alarma.

El trabajo realizado nos permitió continuar avanzando hacia el objetivo de implementar un sistema capaz de detectar movimiento y activar una alarma mediante la micro:bit.
