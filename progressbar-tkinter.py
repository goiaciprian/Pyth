
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="start", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()

        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        if self.bytes >= 50000:
            self.bytes = 0
        else:
            self.progress["value"] = 0
            self.maxbytes = 50000
            self.progress["maximum"] = 50000
            self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 18000
        self.progress["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)
        else:
            root = tk.Tk()
            root.withdraw()
            root.overrideredirect(1)
            if messagebox.askyesno(title='???', message='Vrei sa iesi?'):
                exit(1)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
