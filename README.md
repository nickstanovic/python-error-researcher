# Windows Error Researcher

Windows Error Researcher is a Python script designed to retrieve, analyze, and assist in diagnosing common Windows Event Viewer errors. By identifying frequent issues, it aims to aid users in troubleshooting and fixing problems on their Windows systems.

## Background

Originally written as a PowerShell script to diagnose Windows errors, it has been rewritten in Python. This adaptation is not as cohesive with Windows as the Powershell version so it has less console features. However, the end result is still the same: Helping someone find solutions to their most frequent PC problems. Writing this provided an opportunity to learn more Python libraries and further develop programming skills.

## Prerequisites

- A Windows operating system (tested on Windows 11)
- Python 3.x installed on your system.

## Installation

Before running the script, ensure that you have the `pywin32` module installed. This Python package provides access to many Windows APIs and is necessary for this script to run. 

You can install it using pip, the Python package installer. Open a terminal window and enter the following command:

```bash
pip install pywin32
```

##Usage
To run the script, follow the steps below:

Open a terminal window.
Navigate to the directory containing the script file, windows_error_researcher.py.
Enter the following command and press Enter:
```bash
python windows_error_researcher.py
```
The script will start analyzing your Windows Event Logs, identify common errors, and open a new browser tab for each of the top 5 most common error events with search results to help you troubleshoot them.


Remember that this script has to be run with administrator privileges to access Windows Event Logs.
