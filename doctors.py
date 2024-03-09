import tkinter as tk

import db_functions
from tkinter import ttk
from mytheme import Colors
from datetime import datetime




class DoctorPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.BACKGROUND1, **kwargs)

        img = tk.PhotoImage(file="myicons\\framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        
        # main frame to include all frames
        self.main_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        self.main_frame.place(relx=0.3, rely=0.01, relwidth=.4, relheight=.98)
        self.background_title = tk.Label(self.main_frame, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        # title frame
        title_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND1)
        title_frame.pack(fill='x', pady=2, padx=10)
        title_name_label = tk.Label(title_frame, text="Doctor", font="Consolas 18", bg=Colors.BACKGROUND1, fg=Colors.FG_SHADE_3, anchor='center')
        title_name_label.pack(padx=40, fill='x')

        # Name Entry Box
        doctor_name_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        doctor_name_frame.pack(fill='x', pady=10, padx=10)
        doctor_name_label = tk.Label(doctor_name_frame, text="Name", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        doctor_name_label.pack(padx=40, fill='x')
        doctor_name = tk.StringVar()
        self.dname_entry = tk.Entry(doctor_name_frame, textvariable=doctor_name, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.dname_entry.pack(padx=40, pady=(0,10), fill='x')

        # Dept Dropdown Menu
        dept_frame  = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        dept_frame.pack( fill='x', pady=10, padx=10)
        dept_label = tk.Label(dept_frame, text="Department", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        dept_label.pack(padx=40, fill='x')
        dept_choices = self.get_depts()
        self.dept_dropdown = ttk.Combobox(dept_frame, values=dept_choices, font="Consolas 14")
        self.dept_dropdown.pack(padx=40, pady=(0,10), fill='x')
        self.dept_dropdown.bind('<Enter>', lambda e: self.dept_dropdown.config(values=self.get_depts()))

        # button frame
        button_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        button_frame.pack(fill='x', pady=(10,10), padx=10)
        add_button = tk.Button(button_frame, text="Add Doctor", font="Consolas 14", command=self.add_doct, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        add_button.pack(padx=40, fill='x', pady=(10, 10))

    def add_doct(self):
        doct_name = self.dname_entry.get()
        dept_name = self.dept_dropdown.get()
        # print(dept_name)
        if doct_name and dept_name:
            db_functions.create_doctor(doct_name, dept_name.split()[0])

    def get_depts(self):
        return db_functions.get_all_departments()


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = DoctorPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()
