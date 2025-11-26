#!/bin/bash
echo 0 > /home/bh7/lucespi/estado17.txt
sshpass -p "1234567" ssh -l pi 192.168.100.10 "sudo /./home/pi/proyecto/c/ongpio17"
