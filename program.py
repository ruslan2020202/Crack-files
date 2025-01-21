import tkinter as tk
from tkinter import filedialog, StringVar
from tkinter.ttk import Progressbar
from threading import Thread
from crack import CrackFile


class Program:
    root = tk.Tk()

    def __init__(self):
        self.root.title("Crack PDF, Excel")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.label_top = tk.Label(self.root, text="Crack PDF, Excel", font=('', 30))
        self.label_top.pack(side="top")

        self.entry_file = tk.Entry(self.root, width=30)
        self.entry_file.pack()

        self.button_open_file = tk.Button(self.root, text="Open file", command=self.open_file)
        self.button_open_file.pack()

        self.btn_crack = tk.Button(self.root, text="Crack", command=self.event_btn_crack)
        self.btn_crack.pack()

        self.progress_bar = Progressbar(self.root, mode='indeterminate')

        self.text_pswd = StringVar()
        self.label_password = tk.Label(self.root, textvariable=self.text_pswd)
        self.label_password.pack()

    def open_file(self):
        file = filedialog.askopenfilename()
        if file != '':
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, file)

    def event_btn_crack(self):
        progress = Thread(target=self.start_progress, args=())
        progress.start()

        crack = Thread(target=self.crack_file, args=())
        crack.start()

    def start_progress(self):
        self.progress_bar.pack()
        self.progress_bar.start()

    def crack_file(self):
        print('cracking file')
        cracker = CrackFile(self.entry_file.get())
        password = cracker.hack()
        self.progress_bar.stop()
        self.text_pswd.set(f'Password: {password}')

    def run(self):
        self.root.mainloop()
