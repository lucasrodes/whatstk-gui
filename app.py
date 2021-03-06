# -*- coding: utf-8 -*-
print("Starting python")
from tkinter import Tk, Label, Button, Entry, END, LEFT, OptionMenu, StringVar, IntVar, Checkbutton, HORIZONTAL
from tkinter.ttk import Separator
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter.messagebox import showwarning, showinfo, showerror
import os
from whatstk.core import WhatsAppChat
from whatstk.core import interventions
from plotly.offline import plot
from whatstk.plot import vis
from header_auto import extract_header_format


os.system('clear')

date_mapping = {
    'day': '%d',
    'month': '%m',
    'year': '%y',
    'username': '%name',
    'hour': '%H',
    'minutes': '%M',
    'seconds': '%S',
    '[': '\[',
    ']': '\]'
}

drop_down_options = [
    'day/month/year, hour:minutes - username:',
    'day/month/year, hour:minutes:seconds - username:',
    'day-month-year, hour:minutes - username:',
    'day-month-year, hour:minutes:seconds - username:',
    'day.month.year, hour:minutes - username:',
    'day.month.year, hour:minutes:seconds - username:',
    '[day.month.year hour:minutes] username:',
    '[day.month.year hour:minutes:seconds] username:',

    'month/day/year, hour:minutes - username:',
    'month/day/year, hour:minutes:seconds - username:',
    'month-day-year, hour:minutes - username:',
    'month-day-year, hour:minutes:seconds - username:',
    'month.day.year, hour:minutes - username:',
    'month.day.year, hour:minutes:seconds - username:',
    '[month.day.year hour:minutes] username:',
    '[month.day.year hour:minutes:seconds] username:',

    'year/month/day, hour:minutes - username:',
    'year/month/day, hour:minutes:seconds - username:',
    'year-month-day, hour:minutes - username:',
    'year-month-day, hour:minutes:seconds - username:',
    'year.month.day, hour:minutes - username:',
    'year.month.day, hour:minutes:seconds - username:',
    '[year.month.day hour:minutes] username:',
    '[year.month.day hour:minutes:seconds] username:'
]


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Whats TK')
        self.geometry('570x270')
        self.flag = True
        self.resizable(False, False)

        # Title
        font = tkFont.Font(family="Lucida Grande", size=30)
        title_label = Label(self, text="WhatsTK", font=font)
        title_label.grid(column=1, row=0)
        version_label = Label(self, text="v0.0.1")
        version_label.grid(column=1, row=1)

        # Chat loading
        load_label = Label(self, text="Chat file", width=10, anchor='e')
        load_label.grid(column=0, row=2)
        self.load_entry = Entry(self, width=40)
        self.load_entry.grid(column=1, row=2)
        load_btn = Button(self, text='Browse', command=self.upload_file, width=10)
        load_btn.grid(column=2, row=2)

        # Run Button Auto
        run_btn = Button(self, text='Auto Run', command=self.run_auto, width=40)
        run_btn.grid(column=1, row=3)

        # Empty row
        _ = Label(self, text="", width=10, anchor='e')
        _.grid(column=1, row=4)

        # SEPARATOR -----
        separator = Separator(self).place(x=0, y=140, relwidth=1)
        font_tit = tkFont.Font(family="Lucida Grande", size=12)
        font = tkFont.Font(family="Lucida Grande", size=10)

        _ = Label(self, text="", width=10, anchor='e')
        _.grid(column=1, row=5)

        manual_label = Label(self, text="Manual run (alternative)", width=40, font=font_tit)
        manual_label.grid(column=1, row=6)

       
        
        # Header definition
        header_label = Label(self, text="Chat header", width=10, anchor='e', font=font)
        header_label.grid(column=0, row=7)
        #self.header_entry = Entry(self, width=40)
        #self.header_entry.grid(column=1, row=3)
        self.header_variable = StringVar(self)
        self.header_variable.set(drop_down_options[0]) # default value
        self.header_option = OptionMenu(self, self.header_variable, *drop_down_options)
        self.header_option.config(width=38, font=font)
        self.header_option.grid(column=1, row=7)

        self.header_hour_var = StringVar(self)
        self.header_hour_var.set('24h clock') # default value
        self.header_hour_option = OptionMenu(self, self.header_hour_var, '24h clock', '12h clock')
        self.header_hour_option.config(font=font)
        self.header_hour_option.grid(column=2, row=7)

        # Run Button Manual
        run_btn = Button(self, text='Run', command=self.run_manual, width=40, font=font)
        run_btn.grid(column=1, row=8)
        # run_btn.config(highlightbackground = "red")    

    def build_hformat(self, date_format):
        for k, v in date_mapping.items():
            if (k == 'hour') & (self.header_hour_var.get() == '12h clock'):
                v = '%P'
            elif (k == 'hour') & (self.header_hour_var.get() == '24h clock'):
                v = '%H'
            date_format = date_format.replace(k, v)
        return date_format

    def upload_file(self, event=None):
        filename = filedialog.askopenfilename(title="Select file",filetypes = (("Text files","*.txt"),), parent=self)
        filename = filename.encode('ascii', 'ignore').decode('ascii')
        print('Selected:', filename)
        #self.load_entry.configure(text=self.filename)
        self.load_entry.delete(0, END)
        self.load_entry.insert(0, filename)
    
    def load_chat(self, auto_header=False):
        print(self.header_hour_var.get())
        filename = self.load_entry.get()
        # [IMPORTANT] Choose header format accordingly
        if not filename:
            msg = "Empty chat file path! Please choose a valid file. Must have format .txt"
            showwarning(title="Empty chat file path", message=msg, parent=self)
            raise WhatsTKGUIError(msg)
        if filename.split('.')[-1] != 'txt':
            msg = "Invalid chat file path! Please choose a valid file. Must have format .txt"
            showwarning(title="Invalid chat file path", message=msg, parent=self)
            raise WhatsTKGUIError(msg)
        
        if auto_header:
            try:
                with open(filename, encoding='utf-8') as f:
                    text = f.read()
            except FileNotFoundError as e:
                msg = "File {} was not found.".format(filename)
                showwarning(title="File not found", message=msg, parent=self)

            # split lines
            lines = text.split('\n')

            # Get format auto
            hformat = extract_header_format(lines)
            print("format found was {}".format(hformat))
        else:
            hformat = self.header_variable.get()
            hformat = self.build_hformat(hformat)
            if not hformat:
                msg="Please select a header code from the dropdown menu."
                showwarning(title="Empty header", message=msg, parent=self)
                raise WhatsTKGUIError(msg)
        
        print("Loading file {} with format {}".format(filename, hformat))
        try:
            chat = WhatsAppChat.from_txt(filename, hformat)
        except FileNotFoundError as e:
            msg = "File {} was not found.".format(filename)
            showwarning(title="File not found", message=msg, parent=self)
            raise e
        except KeyError as e:
            msg = "Header format did not match. Please check it again. "\
                    "If using Auto Run, consider using manual run. \nMore info at https://lcsrg.me/whatstk-gui"
            showwarning(title="Header problems", message=msg, parent=self)
            raise e
        return chat

    def run_manual(self):
        try:
            chat = self.load_chat()
        except Exception as e:
            raise e
        counts = interventions(chat, 'date', msg_length=False)
        counts_cumsum = counts.cumsum()
        plot(vis(counts_cumsum, 'Cummulative number of messages sent per day'))
    
    def run_auto(self):
        try:
            chat = self.load_chat(auto_header=True)
        except Exception as e:
            raise e
        counts = interventions(chat, 'date', msg_length=False)
        counts_cumsum = counts.cumsum()
        plot(vis(counts_cumsum, 'Cummulative number of messages sent per day'))


class WhatsTKGUIError(Exception):
    pass


if __name__ == '__main__':
    App().mainloop()