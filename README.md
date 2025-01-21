File Organizer - README

----------------------------------------------
About the Project:
----------------------------------------------
File Organizer is a Python application designed to organize files in a specified directory. 
It supports automatic backups (zip/tar) and real-time monitoring of directory changes using Watchdog.

----------------------------------------------
Requirements:
----------------------------------------------
1. Python must be installed on your computer.
2. The following Python libraries must be installed (use `requirements.txt` for easier installation):
   - altgraph
   - packaging
   - pefile
   - pyinstaller
   - pyinstaller-hooks-contrib
   - pywin32-ctypes
   - setuptools
   - watchdog

----------------------------------------------
Setup Instructions:
----------------------------------------------
1. Clone this project or copy all files to your desired directory
2. Open a terminal and navigate to the project directory.

Create a virtual environment (if not already created):
cmd
python -m venv venv
Activate the virtual environment:
venv\Scripts\activate
Install the required dependencies:
pip install -r requirements.txt

@echo off
:: Navigate to the project directory
cd /d PATH_TO_YOUR_PROJECT_DIRECTORY

:: Activate the virtual environment
call venv\Scripts\activate

:: Run the Python script
python main_with_config.py

:: Deactivate the virtual environment
deactivate

:: Pause to keep the console open
pause

1. Replace `PATH_TO_YOUR_PROJECT_DIRECTORY` with the actual path to the directory where you've installed the project.
2. Ensure you've set up the virtual environment and installed dependencies by running:

3. Save the batch script (`run_app.bat`) in the project directory.
4. Double-click the batch file to run the application.


