from tkinter import *
import pytube

class player:
    def __init__(self, window):
        window.geometry('200x200')
        window.title('Youtube downloader Minimalistic')
        window.config(bg='pale turquoise')

        self.urlhead = Label(root, text='Enter url: ', bg='lightblue4', bd=1, relief='flat')
        self.url = Entry(root, width=20, bd=3, relief='sunken')
        def buttonClick():
            urlget = self.url.get()
            if (urlget is None):
                pass
            elif urlget:
                YT = pytube.YouTube(urlget)
                YT.streams.get_highest_resolution().download('./Downloaded')

        self.downloadBtn=Button(root,text='download',bd=3,relief='raised',bg='lightblue4')
        self.urlhead.place(x=20,y=10);self.url.place(x=20,y=40);self.downloadBtn.place(x=40,y=75)

root = Tk()
app = player(root)
root.mainloop()