    .data
    .align 4
pin22:  .word 3       // WiringPi 3 = GPIO22

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

    // pinMode(3, 1); OUTPUT
    ldr w0, pin22
    mov w1, #1
    bl pinMode

    // digitalWrite(3, 1); HIGH
    ldr w0, pin22
    mov w1, #1
    bl digitalWrite

    // Restaurar y salir
    ldp x29, x30, [sp], 16
    ret
