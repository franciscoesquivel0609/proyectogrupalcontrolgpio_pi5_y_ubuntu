    .data
    .align 4
pin27:  .word 2       // WiringPi 2 = GPIO27

    .text
    .global main
    .extern wiringPiSetup
    .extern pinMode
    .extern digitalWrite

main:
    // Guardar FP/LR
    stp x29, x30, [sp, -16]!
    mov x29, sp

    // wiringPiSetup()
    bl wiringPiSetup

    // pinMode(2, 1); OUTPUT
    ldr w0, pin27
    mov w1, #1
    bl pinMode

    // digitalWrite(2, 0); LOW
    ldr w0, pin27
    mov w1, #0
    bl digitalWrite

    // Restaurar y salir
    ldp x29, x30, [sp], 16
    ret
