#include <wiringPi.h>
#include <stdio.h>

#define PIN 3 //WiringPi 3 = GPIO22 fisico 15 
int main(void) {
        //inicializar la libreria WiringPi
        if (wiringPiSetup() == -1){
                printf("Error al iniciar WiringPi\n");
                return 1;
        }
        pinMode(PIN, OUTPUT); //Configura el pin fisico 15 del modo tipo salida

        printf("Apagado GIPO22 (Pin fisico 15)...\n");
        digitalWrite(PIN, LOW); //Encender gpio
        //delay(2000);

        printf("Listo.\n");
        return 0;
}
