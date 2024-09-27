import psutil
import os
import platform
import sys
import socket

# checks if the os is mac os
if platform.system() != "Darwin":
    sys.exit("You are not running Mac OS")

# clears the terminal
os.system("Clear")


# get mac os version
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
	elif "11" in verNum:
		verString = "Big Sur"
	elif "12" in verNum:
		verString = "Monteray"
	elif "13" in verNum:
		verString = "Ventura"
	elif "14" in verNum:
		verString = "Sonoma"
	elif "15" in verNum:
		verString = "Sequoia"
	else:
		verString = "Not running a version of Mac OS"
	return f"Mac OS Version: {verString} ({vernum})"

# Architecture
arch = platform.architecture()

# Hostname
host = platform.node()

# CPU Architecture
cpuArch = platform.processor()

# Python version
pythonVer = platform.python_version()

# mac os version
osVer = macVer()

# CPU Count
cpuCount = psutil.cpu_count()

# CPU Frequency
cpuFreq = psutil.cpu_freq()[2]

# Total RAM
ram = psutil.virtual_memory()[0]
totalRam = str(ram // 1000000000)
totalRam = totalRam+" GB"

# CPU Type
processor = os.popen('system_profiler SPHardwareDataType | grep Processor\ Name').readlines()
processor = processor[0].strip( "Processor Name: \n")

# Mac Model
macModel = os.popen('system_profiler SPHardwareDataType | grep Model\ Identifier:').readlines()
macModel = macModel[0].replace("Model Identifier:", "")
macModel = macModel.strip( )

# GPU Type
gpu = os.popen('system_profiler SPDisplaysDataType | grep Chipset').readlines()
gpu = gpu[0].strip( "Chipset Model Dynamic, Max): \n")

# Vram Total
vram = os.popen('system_profiler SPDisplaysDataType | grep VRAM').readlines()
vram = vram[0].strip( "VRAM (Total Dynamic, Max): \n")

# Local IP Address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
localIP = s.getsockname()[0]
s.close()

# Public IP Address
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
print("Total Memory (ram): "+totalRam)
print("GPU: "+gpu)
print("Total GPU Memory (vram): "+vram)
print()
print("-------------------------------")