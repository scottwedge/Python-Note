# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:05:40 2018

@author: yiwen, Jerry

happy every day!!
"""
import platform
import os
import tkinter as tk
from Quotesection import start
from section import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(column=0, row=0)
        self.bgColor = '#EEEEEE'
        self.config(bg=self.bgColor, borderwidth=20)
        self.create_widgets()
        self.quoteinfotext.focus()
        # bind shift-enter key to generate quotation
        master.bind_all('<Shift-Return>', lambda e: self.get_quotation())

    def paste_quote_text(self, event):
        """
        Binded function to paste clipboard content into Text, after striping
        This is helpful to solve performance issues when a lot of \t are copied from excel
        """
        clipboard = self.clipboard_get()
        self.quoteinfotext.insert('end', clipboard.strip())
        return "break"

    def focus_next(self, event):
        """binded function that switch the focus to the next widget"""
        event.widget.tk_focusNext().focus()
        # return 'break' is a trick to stop the original functionality of the event
        return "break"

    def autoselect(self):
        if self.rRNAremoval_check.get() == True:
            self.library_type.set(True)
        else:
            self.library_type.get()

    def create_widgets(self):
        self.welcome = tk.Label(self, text=
                                'Product types not accepted:\n\n'
                                'WTS, dRNAseq, Riboseq, hTRS, ChIPseq, RIPseq, WGBS, RRBS, HiC, ATACseq, PCRproduct, Denovo, Matepair'
                                '\n\nPlease paste your quote info below:',
                                bg=self.bgColor)
        self.welcome.grid(column=0, row=0, columnspan=4)

        self.quoteinfotext = tk.Text(self, height=10)
        if platform.system() == 'Darwin':
            self.quoteinfotext.bind('<Command-v>', self.paste_quote_text)
        self.quoteinfotext.bind('<Control-v>', self.paste_quote_text)
        self.quoteinfotext.bind("<Tab>", self.focus_next)
        self.quoteinfotext.grid(column=0, row=1, columnspan=4)

        self.label1 = tk.Label(
            self, text='Special price required? input first and second price:', bg=self.bgColor)
        self.label1.grid(column=0, row=2, columnspan=4)
        self.pricelabel1 = tk.Label(
            self, text='First product price:', bg=self.bgColor)
        self.pricelabel1.grid(column=0, row=3)
        self.pricetext1 = tk.Text(self, width=20, height=1)
        self.pricetext1.bind("<Tab>", self.focus_next)
        self.pricetext1.grid(column=1, row=3)
        self.pricelabel2 = tk.Label(
            self, text='Second product price:', bg=self.bgColor)
        self.pricelabel2.grid(column=2, row=3)
        self.pricetext2 = tk.Text(self, width=20, height=1)
        self.pricetext2.bind("<Tab>", self.focus_next)
        self.pricetext2.grid(column=3, row=3)

        tk.Label(self, bg=self.bgColor).grid(column=0, row=4, columnspan=4)

        self.label2 = tk.Label(
            self, text='Different sample number for BI analysis? If so, input the analysis sample number:', bg=self.bgColor)
        self.label2.grid(column=0, row=5, columnspan=3)
        self.BInumbertext = tk.Text(self, width=20, height=1)
        self.BInumbertext.bind("<Tab>", self.focus_next)
        self.BInumbertext.grid(column=3, row=5, columnspan=1)

        tk.Label(self, bg=self.bgColor).grid(column=0, row=6, columnspan=4)

        self.label3 = tk.Label(
            self, text='Input the species latin name if species is different than "human", "mouse", "rat":', bg=self.bgColor)
        self.label3.grid(column=0, row=7, columnspan=3)
        self.speciestext = tk.Text(self, width=20, height=1)
        self.speciestext.bind("<Tab>", self.focus_next)
        self.speciestext.grid(column=3, row=7, columnspan=1)

        tk.Label(self, bg=self.bgColor).grid(column=0, row=8, columnspan=4)

        self.library_type = tk.BooleanVar()
        self.library_type.set(False)
        self.strandedbutton = tk.Checkbutton(self, text='check if need stranded EukmRNA library', variable=self.library_type,
                                             onvalue=True, offvalue=False, bg=self.bgColor, command=self.autoselect)
        self.strandedbutton.grid(column=0, row=9, columnspan=2)

        self.rRNAremoval_check = tk.BooleanVar()
        self.rRNAremoval_check.set(False)
        self.rRNAremovalbutton = tk.Checkbutton(self, text='check if need rRNA removal/FFPE RNAseq', variable=self.rRNAremoval_check,
                                                onvalue=True, offvalue=False, bg=self.bgColor, command=self.autoselect)
        self.rRNAremovalbutton.grid(column=2, row=9, columnspan=2)

        tk.Label(self, bg=self.bgColor).grid(column=2, row=10, columnspan=4)

        self.run = tk.Button(self, text='Generate New Quote',
                             command=self.get_quotation, highlightbackground=self.bgColor)
        self.run.grid(column=3, row=11, columnspan=1)
        self.password = tk.Label(
            self, text='CMS password', bg=self.bgColor)
        self.password.grid(column=2, row=12)
        self.password = tk.Text(self, width=10, height=1)
        self.password.bind("<Tab>", self.focus_next)
        self.password.grid(column=2, row=11)
        self.run = tk.Button(self, text='submit lead',
                             command=self.submit_lead, highlightbackground=self.bgColor)
        self.run.grid(column=1, row=11, columnspan=2)

        self.clear = tk.Button(
            self, text='Clear All', command=self.clearall, highlightbackground=self.bgColor)
        self.clear.grid(column=0, row=11, columnspan=1)

        self.errorLabel = tk.Label(self, bg=self.bgColor, fg='red')
        self.errorLabel.grid(column=0, row=12, columnspan=8)

    def get_quotation(self):
        quote_info = self.quoteinfotext.get('1.0', 'end').strip()
        price1 = self.pricetext1.get('1.0', 'end').strip()
        price2 = self.pricetext2.get('1.0', 'end').strip()
        BInumber = self.BInumbertext.get('1.0', 'end').strip()
        species = self.speciestext.get('1.0', 'end').strip()
        rRNAremoval_check = self.rRNAremoval_check.get()
        library_type = self.library_type.get()
        try:
            start(quote_info, price1, price2, BInumber, species, library_type, rRNAremoval_check)
            self.errorLabel.config(text='Success!')
        except Exception as e:
            self.errorLabel.config(text=str(e))
            raise

    def submit_lead(self):
        quote_info = self.quoteinfotext.get('1.0', 'end').strip()
        price1 = self.pricetext1.get('1.0', 'end').strip()
        price2 = self.pricetext2.get('1.0', 'end').strip()
        BInumber = self.BInumbertext.get('1.0', 'end').strip()
        species = self.speciestext.get('1.0', 'end').strip()
        rRNAremoval_check = self.rRNAremoval_check.get()
        library_type = self.library_type.get()
        password = self.password.get('1.0', 'end').strip()
        from login import lead_submit, run_it
        try:
            run_it(quote_info, price1, price2, BInumber, species, library_type, rRNAremoval_check, password)
            self.errorLabel.config(text='Success!')
        except Exception as e:
            self.errorLabel.config(text=str(e))
            raise

    def clearall(self):
        self.quoteinfotext.delete('1.0', 'end')
        self.pricetext1.delete('1.0', 'end')
        self.pricetext2.delete('1.0', 'end')
        self.BInumbertext.delete('1.0', 'end')
        self.speciestext.delete('1.0', 'end')
        self.library_type.set(False)
        self.rRNAremoval_check(False)
        self.errorLabel.config(text='')


root = tk.Tk()
app = Application(master=root)
app.mainloop()
