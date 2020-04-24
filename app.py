# -*- coding: utf-8 -*-
print("Starting python")
from tkinter import Tk, Label, Button, Entry
from tkinter import filedialog
import os
from whatstk.core import WhatsAppChat
from whatstk.core import interventions
from plotly.offline import plot
from whatstk.plot import vis


os.system('clear')


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Whats TK')
        self.geometry('750x250')
        self.filename = None
        self.header_input, self.load_info_label = self.create_layout()
    
    def create_layout(self):
        # Label for text input
        load_label = Label(self, text="Load your WhatsApp chat history file.")
        load_label.grid(column=0, row=0)
        # load_label.pack()
        # Button to load file
        load_btn = Button(self, text='Load chat file', command=self.upload_file)
        load_btn.grid(column=1, row=0)

        load_info_label = Label(self, text='')
        load_info_label.grid(column=0, row=1)

        # load_btn.pack()
        # Label for text input
        header_label = Label(self, text="Chat header format")
        header_label.grid(column=0, row=2)
        # header_label.pack()
        header_input = Entry(self, width=30)
        header_input.grid(column=1, row=2)
        # header_input.pack()
        # Run button
        run_btn = Button(self, text='Run', command=self.run, bg='white', fg='green')
        run_btn.grid(column=1, row=6)
        # run_btn.pack()

        return header_input, load_info_label

    def upload_file(self, event=None):
        self.filename = filedialog.askopenfilename()
        self.load_info_label.configure(text=self.filename)
        print('Selected:', self.filename)
    
    def run(self):
        print('run')
        hformat = self.header_input.get()
        print('format: ' + hformat)
        # [IMPORTANT] Choose header format accordingly
        if hformat is None:
            hformat = "%d.%m.%y, %H:%M - %name:"
        print("Loading file {} with format {}".format(self.filename, hformat))
        chat = WhatsAppChat.from_txt(self.filename, hformat)
        counts = interventions(chat, 'date', msg_length=False)
        counts_cumsum = counts.cumsum()
        plot(vis(counts_cumsum, 'cumulative characters sent per day'))


if __name__ == '__main__':
    App().mainloop()