from tkinter import *
#from PIL import image , imageTk

#GUI = tkinter.Tk()
#hw = tkinter.Label(GUI,text="Hallo Welt")
#hw.pack()

#tkinter.mainloop()

class GUI:

    def __init__(self,master):
        frame = Frame(master)
        frame.grid()

        self.bild = PhotoImage(x=300,y=300,width=300,height=300,file="/home/amarantine/Dokumente/Gits/pythonuebung/Biohazard.png")
        #self.bild
        self.photo = Label(frame,text="hallo",image=self.bild)
        self.photo.grid(row=0,column=1)

        self.button = Button(frame,text="Schließen", fg="red", command=frame.quit)
        self.button.grid(row=1,column=0)
        self.__list = [1,2,3,4,5]
        
        
        
        self.hibutton = Button(frame,text="Sag was",fg="green",command=self.say_hi)
        self.hibutton.grid(row=1,column=1,columnspan=2,sticky='e')
    def say_hi(self):
        for a in self.__list : print(a)

root = Tk()
#print(os.path.exists("/home/amarantine/Dokumente/Gits/pythonuebung/hills.jpeg"))
gui = GUI(root)

root.mainloop()
