# Overview
Many websites online that offer services to split PDFs have various restrictions. Some have hourly limits, some have you create an account, some ask for an email to send the results to, etc. I noticed a fellow co-worker of mine was always having issues with these "free" websites, so I decided to create a program that would split a desired PDF. 

## Files
1. *main.py*: contains the logic for splitting the PDFs
2. *gui.py*: contains the GUI for the user input
3. *example*: standalone app created using the Python package pyinstaller
4. *constitution.pdf*: random PDF included for testing the program

## Packages
- PyPDF2
- tkinter
- os

## How to Install
Simply download zip that contains the code and files or clone the repository.

## How to Run
I've included two files to testing purposes: *example.exe* and *constitution.pdf*. Make sure that the PDF is in the same directory as the .exe file. 
1. Open *example.exe*
2. Enter the name of the PDF
3. Enter how many pages you want the separated PDF files to have
	- i.e. this is the cutoff point per PDF
4. Click *Submit* and close the GUI
 
## Known Issues
- GUI doesn't close once "Submit" button is inputted
- Program does throws error if GUI is closed before submitting

## Possible Updates
- Drag and drop files
- Add Merge functionality
 