from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 20
FONT = (FONT_NAME, FONT_SIZE, "bold")

class GUI:

    def __init__(self):
        self.pdf_name = ""
        self.number_to_split = 1
        self.window = Tk()
        self.window.title("PDF Splitter")
        self.window.config(pady=25, padx=25)
        self.window.eval("tk::PlaceWindow . center")
        self.load_window()
        self.window.mainloop()

    def submit(self):
        print(self.pdf_name)
        print(self.number_to_split)
        self.window.destroy()

    def load_window(self):
        # Label - Name
        label_name = Label(text="Name of PDF", font=FONT)
        label_name.pack()

        # Entry - Name
        entry_name = Entry(width=20, font=("Arial", 16))
        self.pdf_name = entry_name.get()
        entry_name.focus()
        entry_name.pack(pady=10)

        # Label - Pages
        label_pages = Label(text="Split every # pages", font=FONT)
        label_pages.pack(pady=10)

        # Entry - Pages
        entry_pages = Entry(width=20, font=("Arial", 16))
        self.number_to_split = entry_pages.get()
        entry_pages.pack(pady=10)

        # Button - Submit
        btn_submit = Button(text="Submit", font=("Arial", 16), command=self.submit)
        btn_submit.pack()


    # def __init__(self):
    #     window = tk.Tk()
    #     window.title("PDF Splitter")
    #     self.ent_name_str = ''
    #     self.ent_pages_str = ''
    #     self.name = ''
    #     self.number_of_pages = 1
    #     self.frm_name()
    #     self.frm_pages()
    #     window.mainloop()
    #
    # def frm_name(self):
    #     self.lbl_name()
    #     self.ent_name()
    #
    # def lbl_name(self):
    #     label = tk.Label(
    #         text="Enter PDF name",
    #         background="white",
    #         foreground="black",
    #         font=FONT,
    #         width=25
    #     )
    #     label.pack()
    #
    # def ent_name(self):
    #     self.ent_name_str = tk.Entry()
    #     self.ent_name_str.config(
    #         font=FONT,
    #         width=30
    #     )
    #     self.ent_name_str.pack()
    #
    # def get_number_of_pages(self):
    #     return self.number_of_pages
    #
    # def frm_pages(self):
    #     self.lbl_pages()
    #     self.ent_pages()
    #     self.btn_pages()
    #
    # def lbl_pages(self):
    #     label = tk.Label(
    #         text="Number of pages per document?",
    #         background="white",
    #         foreground="black",
    #         font=FONT,
    #         width=25
    #     )
    #     label.pack()
    #
    # def ent_pages(self):
    #     self.ent_pages_str = tk.Entry()
    #     self.ent_pages_str.config(
    #         font=FONT,
    #         width=30
    #     )
    #     self.ent_pages_str.pack()
    #
    # def pages_submit(self):
    #     num_pages = self.ent_pages_str.get()
    #     name = self.ent_name_str.get()
    #     # show_name = tk.Label(text=f'{name}', font=FONT)
    #     # show_name.pack()
    #     self.number_of_pages = num_pages
    #     self.name = name
    #
    # def btn_pages(self):
    #     submit = tk.Button(text="Submit", command=self.pages_submit)
    #     submit.pack()

