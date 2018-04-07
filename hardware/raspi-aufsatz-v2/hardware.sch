EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:opto
LIBS:hardware-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "15 nov 2012"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Raspberry_Pi_2_3 J1
U 1 1 5AC0A26F
P 2550 4050
F 0 "J1" H 3250 2800 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 2150 4950 50  0000 C CNN
F 2 "Pin_Headers:Pin_Header_Straight_2x20_Pitch2.54mm" H 3550 5300 50  0001 C CNN
F 3 "" H 2600 3900 50  0001 C CNN
	1    2550 4050
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR01
U 1 1 5AC0A320
P 2150 5900
F 0 "#PWR01" H 2150 5650 50  0001 C CNN
F 1 "GND" H 2150 5750 50  0000 C CNN
F 2 "" H 2150 5900 50  0001 C CNN
F 3 "" H 2150 5900 50  0001 C CNN
	1    2150 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2150 5350 2150 5900
Wire Wire Line
	2250 5350 2250 5450
Wire Wire Line
	2150 5450 2850 5450
Connection ~ 2150 5450
Wire Wire Line
	2350 5450 2350 5350
Connection ~ 2250 5450
Wire Wire Line
	2450 5450 2450 5350
Connection ~ 2350 5450
Wire Wire Line
	2550 5450 2550 5350
Connection ~ 2450 5450
Wire Wire Line
	2650 5350 2650 5450
Connection ~ 2550 5450
Wire Wire Line
	2750 5450 2750 5350
Connection ~ 2650 5450
Wire Wire Line
	2850 5450 2850 5350
Connection ~ 2750 5450
Text GLabel 1650 1000 0    60   Input ~ 0
5V_EXT
$Comp
L Screw_Terminal_01x03 RGBW1
U 1 1 5AC0E66D
P 7300 2700
F 0 "RGBW1" H 7300 2900 50  0000 C CNN
F 1 "Screw_Terminal_01x03" H 7300 2500 50  0000 C CNN
F 2 "TerminalBlocks_Phoenix:TerminalBlock_Phoenix_MPT-2.54mm_3pol" H 7300 2700 50  0001 C CNN
F 3 "" H 7300 2700 50  0001 C CNN
	1    7300 2700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5AC0E72F
P 6600 3000
F 0 "#PWR02" H 6600 2750 50  0001 C CNN
F 1 "GND" H 6600 2850 50  0000 C CNN
F 2 "" H 6600 3000 50  0001 C CNN
F 3 "" H 6600 3000 50  0001 C CNN
	1    6600 3000
	1    0    0    -1  
$EndComp
Text GLabel 6850 2600 0    60   Input ~ 0
5V_EXT
Wire Wire Line
	6850 2600 7100 2600
Wire Wire Line
	7100 2800 6600 2800
Wire Wire Line
	6600 2800 6600 3000
Text GLabel 6400 2700 0    60   Input ~ 0
DATA
Text GLabel 1450 3550 0    60   Input ~ 0
DATA_L
Wire Wire Line
	1450 3550 1650 3550
$Comp
L TXB0102DCT U1
U 1 1 5AC0EA61
P 4800 3100
F 0 "U1" H 5000 3600 50  0000 C CNN
F 1 "TXB0102DCT" H 5100 2600 50  0000 C CNN
F 2 "Housings_SSOP:TSSOP-8_3x3mm_Pitch0.65mm" H 5750 2500 50  0001 C CNN
F 3 "" H 4800 3070 50  0001 C CNN
	1    4800 3100
	1    0    0    -1  
$EndComp
$Comp
L USB_A J2
U 1 1 5AC0EA9E
P 6100 1400
F 0 "J2" H 5900 1850 50  0000 L CNN
F 1 "USB_A" H 5900 1750 50  0000 L CNN
F 2 "Connectors:USB_A" H 6250 1350 50  0001 C CNN
F 3 "" H 6250 1350 50  0001 C CNN
	1    6100 1400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2750 2750 2750 2500
Wire Wire Line
	2750 2500 4700 2500
Wire Wire Line
	4700 2500 4700 2600
Text GLabel 5050 2500 2    60   Input ~ 0
5V_EXT
Wire Wire Line
	5050 2500 4900 2500
Wire Wire Line
	4900 2500 4900 2600
Text GLabel 5450 3000 2    60   Input ~ 0
DATA
Wire Wire Line
	5450 3000 5200 3000
Text GLabel 4150 3000 0    60   Input ~ 0
DATA_L
Wire Wire Line
	4150 3000 4400 3000
$Comp
L GND #PWR03
U 1 1 5AC10E62
P 4800 3750
F 0 "#PWR03" H 4800 3500 50  0001 C CNN
F 1 "GND" H 4800 3600 50  0000 C CNN
F 2 "" H 4800 3750 50  0001 C CNN
F 3 "" H 4800 3750 50  0001 C CNN
	1    4800 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 3750 4800 3600
$Comp
L GND #PWR04
U 1 1 5AC1117D
P 6100 1900
F 0 "#PWR04" H 6100 1650 50  0001 C CNN
F 1 "GND" H 6100 1750 50  0000 C CNN
F 2 "" H 6100 1900 50  0001 C CNN
F 3 "" H 6100 1900 50  0001 C CNN
	1    6100 1900
	1    0    0    -1  
$EndComp
Wire Wire Line
	6100 1900 6100 1800
Text GLabel 6600 1200 2    60   Input ~ 0
5V_EXT
Wire Wire Line
	6600 1200 6400 1200
NoConn ~ 6400 1400
NoConn ~ 6400 1500
NoConn ~ 6000 1800
NoConn ~ 4400 3200
NoConn ~ 5200 3200
NoConn ~ 4400 3400
$Comp
L R R2
U 1 1 5AC115F4
P 6700 2700
F 0 "R2" V 6780 2700 50  0000 C CNN
F 1 "R" V 6700 2700 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 6630 2700 50  0001 C CNN
F 3 "" H 6700 2700 50  0001 C CNN
	1    6700 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	6850 2700 7100 2700
Wire Wire Line
	6550 2700 6400 2700
$Comp
L Screw_Terminal_01x04 BUTTON1
U 1 1 5AC11AB9
P 7450 5100
F 0 "BUTTON1" H 7450 5300 50  0000 C CNN
F 1 "Screw_Terminal_01x04" H 7450 4800 50  0000 C CNN
F 2 "TerminalBlocks_Phoenix:TerminalBlock_Phoenix_MPT-2.54mm_4pol" H 7450 5100 50  0001 C CNN
F 3 "" H 7450 5100 50  0001 C CNN
	1    7450 5100
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR05
U 1 1 5AC11B43
P 6900 5450
F 0 "#PWR05" H 6900 5200 50  0001 C CNN
F 1 "GND" H 6900 5300 50  0000 C CNN
F 2 "" H 6900 5450 50  0001 C CNN
F 3 "" H 6900 5450 50  0001 C CNN
	1    6900 5450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 5450 6900 5300
Wire Wire Line
	6900 5300 7250 5300
Text GLabel 1450 3750 0    60   Input ~ 0
BUTTON
Wire Wire Line
	1450 3750 1650 3750
Text GLabel 1400 3850 0    60   Input ~ 0
LED
Wire Wire Line
	1650 3850 1400 3850
Text GLabel 5500 4850 0    60   Input ~ 0
BUTTON
$Comp
L Screw_Terminal_01x02 Supply1
U 1 1 5AC123A6
P 2400 1000
F 0 "Supply1" H 2400 1100 50  0000 C CNN
F 1 "Screw_Terminal_01x02" H 2400 800 50  0000 C CNN
F 2 "TerminalBlocks_Phoenix:TerminalBlock_Phoenix_MPT-2.54mm_2pol" H 2400 1000 50  0001 C CNN
F 3 "" H 2400 1000 50  0001 C CNN
	1    2400 1000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1650 1000 2200 1000
$Comp
L GND #PWR06
U 1 1 5AC124A3
P 1750 1300
F 0 "#PWR06" H 1750 1050 50  0001 C CNN
F 1 "GND" H 1750 1150 50  0000 C CNN
F 2 "" H 1750 1300 50  0001 C CNN
F 3 "" H 1750 1300 50  0001 C CNN
	1    1750 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 1300 1750 1100
Wire Wire Line
	1750 1100 2200 1100
$Comp
L CP C1
U 1 1 5AC12577
P 3100 1050
F 0 "C1" H 3125 1150 50  0000 L CNN
F 1 "1000uF" H 3125 950 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D10.0mm_P5.00mm" H 3138 900 50  0001 C CNN
F 3 "" H 3100 1050 50  0001 C CNN
	1    3100 1050
	1    0    0    -1  
$EndComp
$Comp
L CP C2
U 1 1 5AC125CE
P 3400 1050
F 0 "C2" H 3425 1150 50  0000 L CNN
F 1 "1000uF" H 3425 950 50  0000 L CNN
F 2 "Capacitors_THT:CP_Radial_D10.0mm_P5.00mm" H 3438 900 50  0001 C CNN
F 3 "" H 3400 1050 50  0001 C CNN
	1    3400 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3400 1300 3400 1200
Wire Wire Line
	2200 1300 3400 1300
Wire Wire Line
	3100 1300 3100 1200
Wire Wire Line
	2200 1100 2200 1300
Connection ~ 3100 1300
Wire Wire Line
	3400 800  3400 900 
Wire Wire Line
	2200 800  3400 800 
Wire Wire Line
	3100 800  3100 900 
Wire Wire Line
	2200 1000 2200 800 
Connection ~ 3100 800 
Connection ~ 2200 1000
Connection ~ 2200 1100
Text GLabel 2550 2450 0    60   Input ~ 0
3V3
Wire Wire Line
	2650 2750 2650 2450
Wire Wire Line
	2650 2450 2550 2450
Text GLabel 5500 4400 0    60   Input ~ 0
3V3
$Comp
L R R1
U 1 1 5AC12DAD
P 6100 4600
F 0 "R1" V 6180 4600 50  0000 C CNN
F 1 "4k7" V 6100 4600 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 6030 4600 50  0001 C CNN
F 3 "" H 6100 4600 50  0001 C CNN
	1    6100 4600
	-1   0    0    1   
$EndComp
Wire Wire Line
	5500 4400 6100 4400
Wire Wire Line
	6100 4400 6100 4450
Wire Wire Line
	6100 4750 6100 5000
Wire Wire Line
	6100 4850 5500 4850
$Comp
L R R3
U 1 1 5AC12F1D
P 6750 5000
F 0 "R3" V 6830 5000 50  0000 C CNN
F 1 "330" V 6750 5000 50  0000 C CNN
F 2 "Resistors_SMD:R_0805" V 6680 5000 50  0001 C CNN
F 3 "" H 6750 5000 50  0001 C CNN
	1    6750 5000
	0    -1   -1   0   
$EndComp
Wire Wire Line
	6900 5000 7250 5000
Wire Wire Line
	6100 5000 6600 5000
Connection ~ 6100 4850
$Comp
L 2N7000 Q?
U 1 1 5AC25EC1
P 8400 3550
F 0 "Q?" H 8600 3625 50  0000 L CNN
F 1 "2N7000" H 8600 3550 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H 8600 3475 50  0001 L CIN
F 3 "" H 8400 3550 50  0001 L CNN
	1    8400 3550
	1    0    0    -1  
$EndComp
$EndSCHEMATC
