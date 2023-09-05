import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        # maakt de window
        self.main_window = tk.Tk()

        # 2 frame top en bottum
        self.top_frame = tk.Frame(self.main_window, width=100, height=100)
        self.bottum_frame = tk.Frame(self.main_window, width=50, height=50)
        # label
        self.label1 = tk.Label(self.top_frame, text="geef uw mening, "
                                                    "ik geef advies ",
                                                    bg="light blue")
        # intvar objecten voor de check buttons
        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()

        # zet de intvar objecten op 0
        self.cb_var1.set(0)
        self.cb_var2.set(0)

        # maak 2 checkbuttons
        self.cb1 = tk.Checkbutton(self.top_frame,
                                  text="ik heb honger",
                                  variable=self.cb_var1)
        self.cb2 = tk.Checkbutton(self.top_frame, text= "ik ben moe",
                                  variable=self.cb_var2)

        # ok en quit button
        self.ok = tk.Button(self.bottum_frame, text="OK",fg="green",
                            command=self.show_result)
        self.quit = tk.Button(self.bottum_frame, text="Quit",fg="red",
                              command=self.main_window.destroy)

        # pack de elementen
        self.top_frame.pack()
        self.bottum_frame.pack()
        self.label1.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.ok.pack(side="left")
        self.quit.pack(side="left")

        # zorg dat de Gui in beeld komt
        tk.mainloop()

    def show_result(self):
        self.message = "Goeie keus!\n"
        self.message2 = "Geef uw keuze\n"

        # if self.cb_var1.get() or self.cb_var2.get() == 0:
        #     tk.messagebox.showinfo("Selectie", self.message2)

        if self.cb_var1.get() == 1:
            self.message = self.message + "ga NU wat eten"

        if self.cb_var2.get() == 1:
            self.message = self.message + "\nga NU slapen"

        tk.messagebox.showinfo("Selectie", self.message)


if __name__ == '__main__':
    My_Gui = GUI()