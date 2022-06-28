# Overview
Many websites online that offer services to split PDFs have various restrictions. Some have hourly limits, some have you create an account, some ask for an email to send the results to, etc. I noticed a fellow co-worker of mine was always having issues with these "free" websites, so I decided to create a program that would split a desired PDF. The program takes in the name of the PDF and prompts the user to enter a number  

## Files
- *main.py*: contains the logic for splitting the PDFs
- *gui.py*: GUI code for receiving user input
- *example.exe*: standalone app created using the Python package __pyinstaller__
- *constitution.pdf*: random PDF included for testing the program

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
	- e.g. if the user enters "2" then each outputted file will have two pages from the original PDF
4. Click *Submit* and close the GUI
 
## Known Issues
- GUI doesn't close once "Submit" button is inputted
- Program does throws error if GUI is closed before submitting

## Possible Updates
- Drag and drop files
- Add Merge functionality

## Helpful Links
- [tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [(PyPDF2](https://pypdf2.readthedocs.io/en/latest/)
- [PyInstaller](https://pyinstaller.org/en/stable/index.html)