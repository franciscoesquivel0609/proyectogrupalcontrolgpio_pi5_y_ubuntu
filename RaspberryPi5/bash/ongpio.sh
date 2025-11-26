#!/bin/bash
gpio -g mode 17 out
gpio -g write 17 0
gpio -g mode 27 out
gpio -g write 27 0
gpio -g mode 22 out
gpio -g write 22 0
