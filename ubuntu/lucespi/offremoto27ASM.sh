#!/bin/bash
echo 1 > /home/bh7/lucespi/estado27.txt
sshpass -p "1234567" ssh -l pi 192.168.100.10 "sudo /./home/pi/proyecto/asm/offgpio27ASM"
