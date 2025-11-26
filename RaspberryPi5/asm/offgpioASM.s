    .data
    .align 4
pin17:  .word 0       // GPIO17 → WiringPi 0
pin27:  .word 2       // GPIO27 → WiringPi 2
pin22:  .word 3       // GPIO22 → WiringPi 3

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

    //--------------------------------------
    //  Configurar como OUTPUT
    //--------------------------------------

    // pinMode(pin17, 1)
    ldr w0, pin17
    mov w1, #1
    bl pinMode

    // pinMode(pin27, 1)
    ldr w0, pin27
    mov w1, #1
    bl pinMode

    // pinMode(pin22, 1)
    ldr w0, pin22
    mov w1, #1
    bl pinMode

    //--------------------------------------
    //  digitalWrite(..., HIGH)
    //--------------------------------------

    // digitalWrite(pin17, 1)
    ldr w0, pin17
    mov w1, #1
    bl digitalWrite

    // digitalWrite(pin27, 1)
    ldr w0, pin27
    mov w1, #1
    bl digitalWrite

    // digitalWrite(pin22, 1)
    ldr w0, pin22
    mov w1, #1
    bl digitalWrite

    // Restaurar y salir
    ldp x29, x30, [sp], 16
    ret
