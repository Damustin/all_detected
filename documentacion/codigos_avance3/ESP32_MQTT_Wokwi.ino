#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Wokwi-GUEST";
const char* password = "";

const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;

const char* tema = "arduino-internet-prueba-84721";

WiFiClient conexionWiFi;
PubSubClient clienteMQTT(conexionWiFi);

void conectarMQTT() {
  while (!clienteMQTT.connected()) {
    Serial.print("Conectando al servidor MQTT...");

    if (clienteMQTT.connect("ESP32-Wokwi-Prueba-84721")) {
      Serial.println(" conectado!");
    } else {
      Serial.print(" Error: ");
      Serial.println(clienteMQTT.state());
      delay(3000);
    }
  }
}

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Conectando al Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWi-Fi conectado!");

  clienteMQTT.setServer(mqtt_server, mqtt_port);

  conectarMQTT();
}

void loop() {
  if (!clienteMQTT.connected()) {
    conectarMQTT();
  }

  clienteMQTT.loop();

  clienteMQTT.publish(tema, "ENVIAR_CORREO");
  Serial.println("Mensaje enviado: ENVIAR_CORREO");

  delay(5000);
}
