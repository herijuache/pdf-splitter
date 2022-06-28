import tkinter as tk

FONT_NAME = "Arial"
FONT_SIZE = 12
FONT = (FONT_NAME, FONT_SIZE)


# Use inheritance?
class GUI():
    def __init__(self):
        window = tk.Tk()
        window.title("PDF Splitter")
        self.ent_name_str = ''
        self.ent_pages_str = ''
        self.name = ''
        self.number_of_pages = 1
        self.frm_name()
        self.frm_pages()
        window.mainloop()

    def frm_name(self):
        self.lbl_name()
        self.ent_name()

    def lbl_name(self):
        label = tk.Label(
            text="Enter PDF name",
            background="white",
            foreground="black",
            font=FONT,
            width=25
        )
        label.pack()

    def ent_name(self):
        self.ent_name_str = tk.Entry()
        self.ent_name_str.config(
            font=FONT,
            width=30
        )
        self.ent_name_str.pack()

    def btn_name(self):
        submit = tk.Button(text="Submit", command=self.name_submit)
        submit.pack()

    def get_number_of_pages(self):
        return self.number_of_pages

    def frm_pages(self):
        self.lbl_pages()
        self.ent_pages()
        self.btn_pages()

    def lbl_pages(self):
        label = tk.Label(
            text="Number of pages per document?",
            background="white",
            foreground="black",
            font=FONT,
            width=25
        )
        label.pack()

    def ent_pages(self):
        self.ent_pages_str = tk.Entry()
        self.ent_pages_str.config(
            font=FONT,
            width=30
        )
        self.ent_pages_str.pack()

    def pages_submit(self):
        num_pages = self.ent_pages_str.get()
        name = self.ent_name_str.get()
        # show_name = tk.Label(text=f'{name}', font=FONT)
        # show_name.pack()
        self.number_of_pages = num_pages
        self.name = name

    def btn_pages(self):
        submit = tk.Button(text="Submit", command=self.pages_submit)
        submit.pack()
