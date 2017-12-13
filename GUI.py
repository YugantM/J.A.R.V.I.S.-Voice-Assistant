import win32com.client
import threading
from tkinter import *
speaker = win32com.client.Dispatch("SAPI.SpVoice")

'''def speek():'''

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.quit()

    def run(self):
        self.root = Tk()
        self.root.title("JARVIS 1.0")
        self.root.option_add("*background", "black")
        self.root.state('zoomed')
        img = PhotoImage(file="reactor.gif")
        panel = Label(self.root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")

        '''b = Button(text="Welcome Sir",command = speek)
        '''
        '''b.pack()'''
        self.root.mainloop()


app = App()



speaker.Speak("Hello sir, Welcome to the JARVIS 1.0")
