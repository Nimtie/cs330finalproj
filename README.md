# cs330finalproj
Security Device Controller using FSA

Finite State Automation was written in Python
Tested on Windows 10 
For this Assignment, assume The Folder Path is '\tmp\Nimtie'

NOTE: YOU ARE REQUIRED TO HAVE PYTHON. IF YOU DON'T HAVE PYTHON INSTALLED, DOWNLOAD THE LATEST VERSION OF PYTHON AT https://www.python.org/downloads/. 
WHEN INSTALLING, IT'S RECOMMENDED TO TURN "ADD PYTHON TO PATH" ON SO YOU CAN USE THE COMMANDS BELOW IN THE TERMINAL.

### HOW TO BUILD AND RUN EXECUTABLES

1. Create EXECUTABLES
	If you don't have pyinstaller, you can install using the command
		pip install pyinstaller
2. Go to the directory of the github repository (... is the rest of the path, which varies by system) 
		Example: cd ...\tmp\Nimtie\cs330finalproj
3. Then, create two executables for the two scripts
		pyinstaller --onefile securitydeviceMoreFSM.py
		pyinstaller --onefile securitydevicetest.py
	The resulting executables will be in the dist directory. Changing the directory will be important for the next steps. You can change the directory with 
		cd dist 
4. Run FSA EXECUTABLE
	In windows: 
		securitydevicemoreFSM.exe 
	In linux:
		./securitydevicemoreFSM

### RUNNING UNIT TEST COVERAGE

1. Install python Coverage module if you don't have it installed already
	pip install coverage
2. Go back to the root folder
	cd ..
3. Run the Coverage/unittest
	coverage run -m unittest securitydevicetest.py
4. Generate Coverage Report
	coverage report


### WHAT THE PROGRAM DOES

This FSA will lock or unlock when given the correct code. There are different codes depending on if you want to lock it or unlock it.
When you run the program, you will be able to choose between Standard and Random mode.

Standard mode allows the user to input digits one by one. The program changes state accordingly, and prints if it is locked or unlocked.

Random mode generates a random digit that is then put into the FSA and processed by the program. This repeats until is either locked or unlock. 
This whole process is run a number of times, which is determined by the user. At the end, it shows the user the raw data, and min/max/avg guesses to unlock/lock.
This mode brute forces the code by guessing digits, without knowing things like password length.

	
		
