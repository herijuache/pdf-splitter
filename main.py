import os
from PyPDF2 import PdfReader, PdfWriter
from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 20
FONT = (FONT_NAME, FONT_SIZE, "bold")


# Creates a PdfReader object that we can:
# - get the number of pages

# DRAG AND DROP IMPLEMENTATION
# try:
#     droppedFile = sys.argv[1]
#     FILE_NAME = str(droppedFile)
# except IndexError:
#     print("No file dropped")

# ------------------------- LOGIC SETUP ------------------------------- #
def split_pdf(pdf_name, number_per_pdf):
    current_path = os.getcwd()

    try:
        input_pdf = PdfReader(open(f"{current_path}\\{pdf_name}", "rb"))
    except FileNotFoundError:
        label_name.config(text="File not Found")
        # load_window()

    else:
        # Keeps track of current_path pages needed to be separated
        page_tracker = number_per_pdf

        # Iterate through the doc until we hit the last page
        for i in range(0, input_pdf.numPages, number_per_pdf):
            output = PdfWriter()  # Blank PdfWriter object
            # Keeps the track in range of index
            if page_tracker > input_pdf.numPages:
                difference = page_tracker - input_pdf.numPages
                page_tracker -= difference
            for y in range(i, page_tracker):
                output.addPage(input_pdf.getPage(y))  # Add page to Write object
            page_number = int((i / number_per_pdf) + 1)
            # prints Object to current_path path
            with open(f"{current_path}/document-page%s.pdf" % page_number, "wb") as outputStream:
                output.write(outputStream)
            # updates the number of pages
            page_tracker += number_per_pdf


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PDF Splitter")
window.config(pady=10, padx=10)
window.eval("tk::PlaceWindow . center")


def check_name(filename):
    try:
        if os.path.exists(filename):
            if os.path.isfile(filename):
                return True
    except FileNotFoundError:
        label_name.config(text="File not found")


def check_pages():
    # Check if the second prompt is an INT
    try:
        num_pages = int(entry_pages.get())
        if num_pages > 0:
            return True
    except ValueError:
        label_pages.config(text="Enter valid #")


def submit():
    name = entry_name.get() + ".pdf"
    # Both need to return 'True' to split PDF
    if check_name(name) and check_pages():
        split_pdf(name, int(entry_pages.get()))
        window.destroy()


# Label - Name
label_name = Label(text="Name of PDF", font=FONT)
label_name.pack()

# Entry - Name
entry_name = Entry(width=20, font=("Arial", 16))
entry_name.focus()
entry_name.pack(pady=10)

# Label - Pages
label_pages = Label(text="Split every # pages", font=FONT)
label_pages.pack(pady=10)

# Entry - Pages
entry_pages = Entry(width=20, font=("Arial", 16))
entry_pages.pack(pady=10)

# Button - Submit
btn_submit = Button(text="Submit", font=("Arial", 16), command=lambda: submit())
btn_submit.pack()

window.mainloop()
