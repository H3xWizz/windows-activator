from asyncio.windows_events import NULL
from glob import glob
import os
import platform
import string

keys = [
    "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "3KHY7-WNT83-DGQKR-F7HPR-844BM",
    "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH",
    "PVMJN-6DFY6–9CCP6–7BKTT-D3WVR",
    "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "MH37W-N47XK-V7XM9-C7227-GCQG9",
    "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ",
    "NPPR9-FWDCX-D2C8J-H872K-2YT43",
    "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
    ]

def menu():
    option = NULL
    print("Choose version:")
    print("===============")
    print("1.Home")
    print("2.Home N")
    print("3.Home Single Language")
    print("4.Home Country Specific")
    print("5.Professional")
    print("6.Professional N")
    print("7.Education")
    print("8.Education N")
    print("9.Enterprise")
    print("10.Enterprise N")
    return int(input("Input: ")) - 1

if platform.system() != "Windows":
    print("Your system is not windows!")
    exit()

os.system("slmgr /ipk " + keys[menu()])
print("33%")
os.system("slmgr /skms kms8.msguides.com")
print("67%")
os.system("slmgr /ato")
print("100% \n Windows activate")