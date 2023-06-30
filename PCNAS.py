from tkinter import *
from threading import Thread, Event
import tkinter 
import os
import http.server, socketserver

# Colors
black = "\x1b[0;30m"
red = "\x1b[0;31m"
green = "\x1b[0;32m"
yellow = "\x1b[0;33m"
blue = "\x1b[0;34m"
purple = "\x1b[0;35m"
cyan = "\x1b[0;36m"
white = "\x1b[0;37m"

Handler = http.server.SimpleHTTPRequestHandler

def init_server(path, port, event: Event):
    with socketserver.TCPServer((path, int(port)), Handler) as httpd:
        print("Servidor HTTP en el puerto", port)
        t3 = Thread(target=httpd.serve_forever)
        t3.start()
        while not event.is_set():
            pass
        exit()

print(blue+"Starting PC-NAS 1.0")

def on_error(error_type):
    print("oh no")
    error = tkinter.Tk()
    error.title("PC-NAS error")
    error.geometry("250x80")
    error.configure(bg="black")

    Label(error, text="[PC-NAS error]", bg="red", fg="black").pack(fill = tkinter.X)
    Label(error, text=" ", bg="black", fg="black").pack(fill = tkinter.X)
    Label(error, text="error: "+str(error_type), bg="black", fg="white").pack(fill = tkinter.X)

    error.mainloop()

ui = tkinter.Tk()
ui.title("PC-NAS 1.0 - by x04000")
ui.geometry("520x520")
ui.configure(bg="black")

Label(ui, text="[PC-NAS Configurator]", bg="cyan", fg="black").pack(fill = tkinter.X)
Label(ui, text=" ", bg="black", fg="black").pack(fill = tkinter.X)
Label(ui, text="Select your host:", bg="black", fg="white").pack(fill = tkinter.X)
pathinput = tkinter.Entry(ui, width=30, fg="white", bg="black")
pathinput.insert(0, "localhost")
pathinput.pack(fill=tkinter.X)
Label(ui, text="Port:", bg="black", fg="white").pack(fill = tkinter.X)
portinput = tkinter.Entry(ui, width=30, fg="white", bg="black")
portinput.insert(0, "8000")
portinput.pack(fill=tkinter.X)

event = Event()
path = pathinput.get()
port = portinput.get()
t2 = Thread(target=init_server, args=(path, port, event,))

def exit_app():
    global on_exit
    ui.destroy()
    event.set()
    t2.join()
    print("Yeah, the following error is supposed to happen")
    exit()

tkinter.Button(ui, text = "Start Server", command = t2.start, fg="white", bg="black").pack(fill = tkinter.X)
exit_button = tkinter.Button(ui, text="Exit server", command=exit_app, fg="white", bg="black")
exit_button.pack()

ui.mainloop()
