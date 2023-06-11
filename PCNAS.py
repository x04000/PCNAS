from tkinter import *
import tkinter as ui
import os

# Colors
black = "\x1b[0;30m"
red = "\x1b[0;31m"
green = "\x1b[0;32m"
yellow = "\x1b[0;33m"
blue = "\x1b[0;34m"
purple = "\x1b[0;35m"
cyan = "\x1b[0;36m"
white = "\x1b[0;37m"

try:
    print(blue+"Starting PC-NAS 1.0")

    def error(errortype):
        ERROR = ui.Tk()
        ERROR.title("PC-NAS ERROR")
        ERROR.geometry("250x80")
        ERROR.configure(bg="black")

        Label(ERROR, text="[PC-NAS ERROR]", bg="red", fg="black").pack(fill = ui.X)
        Label(ERROR, text=" ", bg="black", fg="black").pack(fill = ui.X)
        Label(ERROR, text="ERROR: "+str(errortype), bg="black", fg="white").pack(fill = ui.X)

        ERROR.mainloop()
    
    UI = ui.Tk()
    UI.title("PC-NAS 1.0 - by x04000")
    UI.geometry("520x520")
    UI.configure(bg="black")

    Label(UI, text="[PC-NAS Configurator]", bg="cyan", fg="black").pack(fill = ui.X)
    Label(UI, text=" ", bg="black", fg="black").pack(fill = ui.X)
    Label(UI, text="Select the path of the files you want to share:", bg="black", fg="white").pack(fill = ui.X)
    pathinput = ui.Entry(UI, width=30, fg="white", bg="black")
    pathinput.insert(0, os.getcwd())
    pathinput.pack(fill=ui.X)
    Label(UI, text="Port:", bg="black", fg="white").pack(fill = ui.X)
    portinput = ui.Entry(UI, width=30, fg="white", bg="black")
    portinput.insert(0, "8000")
    portinput.pack(fill=ui.X)

    def start():
        path = str(pathinput.get())
        port = str(portinput.get())
        
        print("Starting server at: "+path)
        print("Server port: "+port)
        try:
            os.system("python3 -m http.server --directory "+path+" "+port)
        except KeyboardInterrupt:
            error("Keyboard Interrupt")
        except:
            error("Unknow error")

    Label(UI, text=" ", bg="black", fg="black").pack(fill = ui.X)
    Label(UI, text="Warning: If you want to stop the server, do Ctrl+C in the main console", bg="black", fg="white").pack(fill = ui.X)
    Label(UI, text=" ", bg="black", fg="black").pack(fill = ui.X)
    
    ui.Button(UI, text = "Start Server", command = start, fg="white", bg="black").pack(fill = ui.X)

    UI.mainloop()

except KeyboardInterrupt:
    print(cyan+"["+red+"!"+cyan+"]"+red+"Keyboard Interrupt")
except:
    print(cyan+"["+red+"!"+cyan+"]"+red+"Unknow error")