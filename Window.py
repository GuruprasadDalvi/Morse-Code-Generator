from tkinter import *
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-','a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..',' ':'     '}
class ABC(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()

        
def convert():
    ip = entry_1.get()
    x = list(ip)
    l = []
    i = 1
    for e  in x:
        t = MORSE_CODE_DICT[e]
        l.insert(i, t)
        i += 1
        l.insert(i,'  ')
        i += 1
    str1 = ''.join(l)
    label_1 = Label(m, text = "")                                                                                                                                                                                                                                          ",font=("Arial",20),bg = "#fcd0a1",fg="#84674a")
    label_1.place(x = 80, y = 150)

    label_1 = Label(m, text = str1, font = ("Arial", 20), bg = "#fcd0a1", fg = "#84674a")
    label_1.place(x = 80, y = 150)


    
    
m = Tk()
m.configure(background = '#fcd0a1')

label_1 = Label(m, text = "Enter A input", width = 20, font = ("Arial", 10), bg = "#fcd0a1", fg = "#84674a")
label_1.place(x = 80, y = 130)

entry_1 = Entry(m, bg = "#d6b18b", fg = "#84674a", width = "30", bd = ".5")
entry_1.place(x = 260,y = 130)

b = Button(m, text = 'Convert', command = convert, font = ("Arial", 10), bg = "#fcd0a1",fg = "#84674a", bd = ".5")
b.place(x = 450, y = 125)


app = ABC(master = m)
app.master.title("Morsce Code Genrator")
app.master.maxsize(1920, 1440)
app.master.minsize(640, 480)


m.mainloop() 
