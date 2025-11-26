#include <wiringPi.h>
#include <stdio.h>

#define PIN0 0 //WiringPi 0 = GPIO17 fisico 11
#define PIN2 2 //WiringPi 2 = GPIO27 fisico 13
#define PIN3 3 //WiringPi 3 = GPIO22 fisico 15
int main(void) {
        //inicializar la libreria WiringPi
        if (wiringPiSetup() == -1){
                printf("Error al iniciar WiringPi\n");
                return 1;
        }
        pinMode(PIN0, OUTPUT); //Configura el pin fisico 11 del modo tipo salida
        pinMode(PIN2, OUTPUT); //Configura el pin fisico 13 del modo tipo salida
        pinMode(PIN3, OUTPUT); //Configura el pin fisico 15 del modo tipo salida


        printf("Encendido GPIO17,GPIO27,GPIO22 (Pin fisico 11,13,15)...\n");
        digitalWrite(PIN0, HIGH); //Apagar gpio
        digitalWrite(PIN2, HIGH); //Apagar gpio
        digitalWrite(PIN3, HIGH); //Apagar gpio
        //delay(2000);

        printf("Listo.\n");
        return 0;
}
