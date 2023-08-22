# Windows Security Measures with Python

This repository contains a Python script that implements security measures on a Windows system. The script interacts with the Windows Registry Editor to disable USB ports and Bluetooth, and it also blocks access to specific websites by modifying the hosts file.

## Features

- **Disable USB Ports and Bluetooth**: The script uses the Windows Registry to disable USB ports and Bluetooth. The 'Start' values of the USBSTOR and BthServ keys are set to 4.

- **Block Website Access**: The script adds an entry to the Windows hosts file to block access to a specified website (e.g., facebook.com).

## Prerequisites

- Windows 10 operating system
- Python installed

## Usage

1. Clone this repository to your local machine.
2. Open a command prompt or terminal and navigate to the directory where the script is located.
3. Run the script using the following command:
4. The script will apply the specified security measures.

## Caution

- **Important**: Modifying the Windows Registry and system settings can have significant consequences on system functionality. Use this script with caution and only on systems where you understand the implications.
- **Backup**: It's recommended to create a backup of your system or registry before using this script.
