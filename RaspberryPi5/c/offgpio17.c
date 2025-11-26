#include <wiringPi.h>
#include <stdio.h>

#define PIN 0 //WiringPi 0 = GPIO17 fisico 11
int main(void) {
	//inicializar la libreria WiringPi
	if (wiringPiSetup() == -1){
		printf("Error al iniciar WiringPi\n");
		return 1;
	}
	pinMode(PIN, OUTPUT); //Configura el pin fisico 11 del modo tipo salida

	printf("Apagado GIPO17 (Pin fisico 11)...\n");
	digitalWrite(PIN, HIGH); //Apagar gpio

	printf("Listo.\n");
	return 0;
}
