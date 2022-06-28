import os
from PyPDF2 import PdfReader, PdfWriter
from gui import GUI

# Creates a PdfReader object that we can:
# - get the number of pages

# try:
#     droppedFile = sys.argv[1]
#     FILE_NAME = str(droppedFile)
# except IndexError:
#     print("No file dropped")
CURRENT_PATH = os.getcwd()

window = GUI()

input_pdf = PdfReader(open(f"{CURRENT_PATH}\\{window.name}.pdf", "rb"))

# Prompt user for input greater than 0
# number_of_pages = int(screen.numinput("Number of Pages", "How many pages per document?", default=2))
number_of_pages = int(window.get_number_of_pages())

if number_of_pages == 0 or number_of_pages is None:
    print("Invalid number")

else:
    # Keeps track of current pages needed to be separated
    page_tracker = number_of_pages

    # Iterate through the doc until we hit the last page
    for i in range(0, input_pdf.numPages, number_of_pages):
        output = PdfWriter()  # Blank PdfWriter object
        # Keeps the track in range of index
        if page_tracker > input_pdf.numPages:
            difference = page_tracker - input_pdf.numPages
            page_tracker -= difference
        for y in range(i, page_tracker):
            output.addPage(input_pdf.getPage(y))    # Add page to Write object
        page_number = int((i / number_of_pages) + 1)
        # prints Object to current path
        with open(f"{CURRENT_PATH}/document-page%s.pdf" % page_number, "wb") as outputStream:
            output.write(outputStream)
        # updates the number of pages
        page_tracker += number_of_pages
