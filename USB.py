#!usr/bin/env

"""

Gaseste toate dispozitivele conectate

"""

import win32com.client

wmi = win32com.client.GetObject("winmgmts:")
devicesConnected = []

for usb in wmi.InstancesOf("Win32_USBHub"):
    devicesConnected.append(usb.DeviceID)

if __name__ == "__main__":
    for i in devicesConnected:
        print(i)
