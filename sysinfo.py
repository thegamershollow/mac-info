# imports
import os
import platform
import sys
import subprocess
import socket
import psutil


# check is the current operating system is mac os
if platform.system() != "Darwin":
	sys.exit("You are not running Mac OS")

# clears the terminal
os.system("Clear")

# main program stuff

# get system information

def macVer():
	macVer = platform.mac_ver()
	vernum = macVer[0]
	ver = vernum.split(".")
	verNum = ver[0]+"."+ver[1]
	if verNum == "10.0":
		verString = "Cheetah"
	elif verNum == "10.1":
		verString = "Puma"
	elif verNum == "10.2":
		verString = "Jaguar"
	elif verNum == "10.3":
		verString = "Panther"
	elif verNum == "10.4":
		verString = "Tiger"
	elif verNum == "10.5":
		verString = "Leapard"
	elif verNum == "10.6":
		verString = "Snow Leapard"
	elif verNum == "10.7":
		verString = "Lion"
	elif verNum == "10.8":
		verString = "Mountain Lion"
	elif verNum == "10.9":
		verString = "Maveriks"
	elif verNum == "10.10":
		verString = "Yosemite"
	elif verNum == "10.11":
		verString = "El Capitan"
	elif verNum == "10.12":
		verString = "Sierra"
	elif verNum == "10.13":
		verString = "High Sierra"
	elif verNum == "10.14":
		verString = "Mojave"
	elif verNum == "10.15":
		verString = "Catalina"
	else:
		verString = "notOSX"
	return f"Mac OS X: {verString} ({vernum})"
## get computer architecture

arch = platform.architecture()

host = platform.node()

platString = platform.platform()

cpuArch = platform.processor()

pythonVer = platform.python_version()

osVer = macVer()

ram  = os.popen('system_profiler SPHardwareDataType | grep "Memory:"').readlines()

cores = os.popen('system_profiler SPHardwareDataType | grep Cores:').readlines()

processor = os.popen('system_profiler SPHardwareDataType | grep Processor\ Name:').readlines()

macModel = os.popen('system_profiler SPHardwareDataType | grep Model\ Identifier:').readlines()

cpuSpeed = os.popen('system_profiler SPHardwareDataType | grep Processor\ Speed:').readlines()

gpu = os.popen('system_profiler SPDisplaysDataType | grep Chipset').readlines()

vram = os.popen('system_profiler SPDisplaysDataType | grep VRAM').readlines()

ram = ram[0].strip( "Memory: \n")

cores = cores[0].strip( "Total Number of Cores: \n")

processor = processor[0].strip( "Processor Name: \n")

macModel = macModel[0].replace("Model Identifier:", "")
macModel = macModel.strip( )

cpuSpeed = cpuSpeed[0].strip( "Processor Speed: \n")

gpu = gpu[0].strip( "Chipset Model: \n")

vram = vram[0].strip( "VRAM (Total): \n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
s.close()

externalIP  = os.popen('curl -s ifconfig.me').readline()



print("----------System-Info----------")
print()
print(osVer)
print("Hostname: "+host)
print("Local IP: "+localIP)
print("Public IP: "+externalIP)
print()
print("-------------------------------")
print()
print("Model: "+macModel)
print("Architecture: "+arch[0])
print("CPU: "+processor)
print("CPU Core Count: "+cores)
print("CPU Speed: "+cpuSpeed)
print("GPU: "+gpu)
print("Total GPU Memory: "+vram)
print("Total Memory: "+ram)
print()
print("-------------------------------")
