#include <wiringPi.h>
#include <stdio.h>

#define PIN 2 //WiringPi 2 = GPIO27 fisico 13
int main(void) {
        //inicializar la libreria WiringPi
        if (wiringPiSetup() == -1){
                printf("Error al iniciar WiringPi\n");
                return 1;
        }
        pinMode(PIN, OUTPUT); //Configura el pin fisico 13 del modo tipo salida

        printf("Encendido GIPO27 (Pin fisico 13)...\n");
        digitalWrite(PIN, HIGH); //Apagar gpio
        //delay(2000);

        printf("Listo.\n");
        return 0;
}
