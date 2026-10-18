
# Informe de Avance 3 — Octubre 2026

## 08/10/2026 — Montaje físico y pruebas con sensores PIR

### Preparación de los materiales

Durante esta clase logramos reunir nuevamente todos los materiales y componentes necesarios para continuar con el desarrollo de nuestro sistema de alarma.

Cabe destacar que, en clases anteriores, sufrimos el robo de parte de los materiales del proyecto, situación que dificultó nuestro avance y retrasó la realización de las pruebas físicas.

A pesar de este inconveniente, conseguimos reunir nuevamente los elementos necesarios y retomar las actividades previstas.

Trabajamos con dos micro:bit, placas de expansión, sensores PIR, cables de conexión y una computadora para realizar la programación y comprobar el funcionamiento de los dispositivos.

De esta manera, pudimos retomar las pruebas físicas del sistema de alarma.

![Montaje de los componentes](imagenes/Montaje_componentes.jpeg)

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

![Conexión del sensor PIR a la placa de expansión](imagenes/Conexion_sensor_PIR.jpeg)

### Objetivo de las pruebas

Nuestro objetivo principal era conseguir que los sensores PIR detectaran movimiento y que la micro:bit activara una alarma sonora.

Para ello utilizamos como base el código que veníamos desarrollando durante las clases anteriores en MakeCode, utilizando el lenguaje Python.

En esta etapa nos concentramos únicamente en comprobar el funcionamiento de los sensores y la activación de la alarma.

### Evolución del sistema de alarma sonora

Durante las primeras etapas del proyecto realizamos simulaciones en Tinkercad, utilizando un componente piezoeléctrico para reproducir los sonidos de la alarma.

En aquella versión, el código utilizaba el pin P1 como salida de sonido para el piezoeléctrico.

Posteriormente decidimos retirar ese componente y aprovechar el parlante integrado de la micro:bit.

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

Al comenzar a trabajar con los componentes físicos, decidimos utilizar el parlante integrado de la micro:bit en lugar del piezoeléctrico previsto inicialmente.

Para esta adaptación trabajamos con las funciones de música de MakeCode, que permiten generar sonidos sin necesidad de conectar un dispositivo externo.

La siguiente función representa la adaptación prevista para utilizar el parlante integrado:

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

Para adaptar el sistema de alarma utilizamos MakeCode, configurando las funciones de alerta visual y sonora de la micro:bit. Posteriormente, realizamos pruebas físicas para comprobar su funcionamiento.

![Programación del sistema de alarma en Microsoft MakeCode](imagenes/Prueba_programacion.jpeg)

### Dificultades durante las pruebas

Después de realizar estas pruebas y revisar las conexiones entre las micro, las placas de expansión y los sensores PIR, no conseguimos obtener la respuesta esperada.

El principal inconveniente fue que no pudimos confirmar que los sensores enviaran correctamente la señal de detección de movimiento a la micro. Esto impidió verificar el funcionamiento completo del sistema.

### Pruebas individuales de los sensores PIR

Ante las dificultades encontradas, decidimos realizar pruebas específicas utilizando MakeCode.

Para ello utilizamos códigos más sencillos, destinados únicamente a comprobar si los sensores PIR detectaban movimiento y enviaban una señal a la micro:bit mediante el pin P0.

Realizamos varios intentos, pero continuamos sin obtener los resultados esperados.

A partir de estas pruebas, planteamos la hipótesis de que los sensores PIR podrían encontrarse dañados, aunque no pudimos confirmar definitivamente esta situación.

### Preparación para la próxima clase

Como parte de la preparación para la siguiente clase, durante el fin de semana conseguimos dos sensores PIR nuevos para repetir las pruebas físicas.

Nuestro próximo objetivo será conectar nuevamente los componentes y comprobar si los sensores detectan movimiento correctamente.

Una vez que logremos verificar la detección, continuaremos con las pruebas de activación de la alarma sonora mediante el parlante integrado de la micro:bit.

También quedó pendiente revisar el control de la variable `movimiento_anterior` para permitir nuevas detecciones después de que el sensor deje de registrar movimiento.

Por el momento, seguimos trabajando en esta primera etapa del proyecto, sin avanzar todavía hacia las pruebas de comunicación por radio ni el envío de mensajes o notificaciones a otros dispositivos.

### Conclusión

Aunque no conseguimos completar satisfactoriamente las pruebas físicas, esta clase representó un avance importante para el desarrollo del proyecto.

Después de las dificultades ocasionadas por el robo de materiales, logramos reunir nuevamente los componentes necesarios, retomar el montaje físico y realizar diferentes pruebas de funcionamiento.

Durante la jornada también trabajamos en la adaptación del código para utilizar el parlante integrado de la micro:bit y efectuamos pruebas individuales de los sensores PIR para intentar identificar el origen de los inconvenientes.

Si bien no pudimos confirmar que los sensores estuvieran dañados, establecimos los próximos pasos para continuar con las pruebas utilizando nuevos componentes.

El trabajo realizado nos permitió avanzar en la integración de los elementos físicos y la programación, acercándonos al objetivo de implementar un sistema capaz de detectar movimiento y activar una alarma mediante la micro:bit.



## 15/10/2026 — Pruebas de funcionamiento de los sensores PIR con Arduino

Durante la clase realizamos pruebas utilizando una placa Arduino para comprobar el funcionamiento de los sensores PIR, debido a los inconvenientes que habíamos tenido anteriormente al utilizarlos con la micro:bit.

Para realizar las pruebas, conectamos los sensores PIR a Arduino y utilizamos un código que permitía detectar movimiento mediante el encendido y apagado de los LED.

Durante las pruebas observamos que, al realizar movimientos frente al sensor, los LED se encendían y, cuando dejaba de detectar movimiento, se apagaban.

De esta manera, comprobamos visualmente que los sensores respondían correctamente al utilizar una alimentación de **5 V**, mientras que con **3 V** no obtuvimos los resultados esperados.

### Evidencia de la prueba

En el siguiente video se muestra el funcionamiento del sensor PIR conectado a Arduino, donde se puede observar la respuesta de los LED ante la detección de movimiento.

[Ver video de la prueba con Arduino](videos/Prueba_PIR_Arduino.mp4)

### Código utilizado en Arduino

Para realizar las pruebas utilizamos el siguiente código, que permite leer la señal del sensor PIR y controlar el encendido y apagado del LED integrado de Arduino según la detección de movimiento.

```cpp
const int MOTION_PIN = 2; // Pin conectado al sensor PIR

void setup()
{
  Serial.begin(9600);

  pinMode(MOTION_PIN, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  int proximity = digitalRead(MOTION_PIN);
  Serial.write(proximity);

  if (proximity == LOW)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Motion detected!");
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
  }

  delay(1000);
}
```

### Resultados obtenidos

Las pruebas realizadas permitieron comprobar que los sensores PIR funcionaban con Arduino al utilizar una alimentación de **5 V**.

A partir de estos resultados, continuamos realizando pruebas con la micro:bit y su placa de expansión para investigar las dificultades que presentaban los sensores al utilizarlos en nuestro proyecto **ALL DETECTED**.

---
