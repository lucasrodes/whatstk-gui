# -*- coding: utf-8 -*-
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
        self.geometry('400x400')

        self.create_layout()
    
    def create_layout(self):
        # Button to load file
        loadButton = Button(self, text='Load chat file', command=self.upload_file)
        loadButton.pack()
        # Label for text input
        formatLabel = Label(self, text="Chat header format")
        formatLabel.pack()
        formatInput = Entry(self, width=30)
        formatInput.pack()
        # Run button
        runButton = Button(self, text='Run', command=self.run)
        runButton.pack()

    def upload_file(self, event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
    
    def run(self):
        print('run')
        filename = '/Users/lucasrodes/repos/whatstk/mychats/untos-1.txt'
        # [IMPORTANT] Choose header format accordingly
        hformat = "%d.%m.%y, %H:%M - %name:"
        chat = WhatsAppChat.from_txt(filename, hformat)
        counts = interventions(chat, 'date', msg_length=False)
        counts_cumsum = counts.cumsum()
        plot(vis(counts_cumsum, 'cumulative characters sent per day'))

# GUI
# root = Tk()
# root.title('Whats TK')
# root.geometry('400x400')

# myLabel = Label(root, text='Enter your first name:')
# myLabel.pack()




if __name__ == '__main__':
    App().mainloop()