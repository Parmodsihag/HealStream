import tkinter as tk

import db_functions
from tkinter import ttk
from mytheme import Colors
from datetime import datetime




class DepartmentPage(tk.Frame):
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
        title_name_label = tk.Label(title_frame, text="Department", font="Consolas 18", bg=Colors.BACKGROUND1, fg=Colors.FG_SHADE_3, anchor='center')
        title_name_label.pack(padx=40, fill='x')

        # Name Entry Box
        department_name_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        department_name_frame.pack(fill='x', pady=10, padx=10)
        department_name_label = tk.Label(department_name_frame, text="Department Name", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        department_name_label.pack(padx=40, fill='x')
        department_name = tk.StringVar()
        self.dname_entry = tk.Entry(department_name_frame, textvariable=department_name, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.dname_entry.pack(padx=40, pady=(0,10), fill='x')

        
        # button frame
        button_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        button_frame.pack(fill='x', pady=(10,10), padx=10)
        add_button = tk.Button(button_frame, text="Add Dept.", font="Consolas 14", command=self.add_dept, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        add_button.pack(padx=40, fill='x', pady=(10, 10))

    def add_dept(self):
        dept_name = self.dname_entry.get()
        if dept_name:
            db_functions.create_department(dept_name)


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = DepartmentPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()
