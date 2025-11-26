    .data
    .align 4
pin0:   .word 0   // WiringPi 0 = GPIO17

    .text
    .global main
    .extern wiringPiSetup
    .extern pinMode
    .extern digitalWrite

main:
    // Guardar LR (x30) en la pila
    stp x29, x30, [sp, -16]!
    mov x29, sp

    // wiringPiSetup()
    bl wiringPiSetup

    // pinMode(0, 1)
    ldr w0, pin0        // w0 = pin número 0
    mov w1, #1          // modo = 1 (OUTPUT)
    bl pinMode

    // digitalWrite(0, 0)
    ldr w0, pin0        // w0 = pin número 0
    mov w1, #0          // valor = LOW
    bl digitalWrite

    // Restaurar LR y volver
    ldp x29, x30, [sp], 16
    ret

