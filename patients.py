import tkinter as tk

import db_functions
from tkinter import ttk
from mytheme import Colors
from datetime import datetime




class PatientPage(tk.Frame):
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
        title_name_label = tk.Label(title_frame, text="Patient", font="Consolas 18", bg=Colors.BACKGROUND1, fg=Colors.FG_SHADE_3, anchor='center')
        title_name_label.pack(padx=40, fill='x')

        # Name Entry Box
        patient_name_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_name_frame.pack(fill='x', pady=10, padx=10)
        patient_name_label = tk.Label(patient_name_frame, text="Name", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_name_label.pack(padx=40, fill='x')
        patient_name = tk.StringVar()
        self.pname_entry = tk.Entry(patient_name_frame, textvariable=patient_name, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.pname_entry.pack(padx=40, pady=(0,10), fill='x')

        # age Entry Box
        patient_age_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_age_frame.pack(fill='x', pady=10, padx=10)
        patient_age_label = tk.Label(patient_age_frame, text="Age", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_age_label.pack(padx=40, fill='x')
        patient_age = tk.IntVar()
        self.page_entry = tk.Entry(patient_age_frame, textvariable=patient_age, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.page_entry.pack(padx=40, pady=(0,10), fill='x')

        # Sex Entry Box
        patient_sex_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_sex_frame.pack(fill='x', pady=10, padx=10)
        patient_sex_label = tk.Label(patient_sex_frame, text="Sex", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_sex_label.pack(padx=40, fill='x')
        patient_sex = tk.StringVar()
        self.psex_entry = tk.Entry(patient_sex_frame, textvariable=patient_sex, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.psex_entry.pack(padx=40, pady=(0,10), fill='x')

        # add Entry Box
        patient_add_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_add_frame.pack(fill='x', pady=10, padx=10)
        patient_add_label = tk.Label(patient_add_frame, text="Address", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_add_label.pack(padx=40, fill='x')
        patient_add = tk.StringVar()
        self.padd_entry = tk.Entry(patient_add_frame, textvariable=patient_add, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.padd_entry.pack(padx=40, pady=(0,10), fill='x')

        # mobile Entry Box
        patient_mob_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_mob_frame.pack(fill='x', pady=10, padx=10)
        patient_mob_label = tk.Label(patient_mob_frame, text="Mobile Number", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_mob_label.pack(padx=40, fill='x')
        patient_mob = tk.StringVar()
        self.pmob_entry = tk.Entry(patient_mob_frame, textvariable=patient_mob, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.pmob_entry.pack(padx=40, pady=(0,10), fill='x')

        # Guardian Entry Box
        patient_guardian_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_guardian_frame.pack(fill='x', pady=10, padx=10)
        patient_guardian_label = tk.Label(patient_guardian_frame, text="Guardian", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_guardian_label.pack(padx=40, fill='x')
        patient_guardian = tk.StringVar()
        self.pguardian_entry = tk.Entry(patient_guardian_frame, textvariable=patient_guardian, font="Consolas 14", bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.pguardian_entry.pack(padx=40, pady=(0,10), fill='x')


        # button frame
        button_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        button_frame.pack(fill='x', pady=(10,10), padx=10)
        add_button = tk.Button(button_frame, text="Add Patient", font="Consolas 14", command=self.add_patient, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        add_button.pack(padx=40, fill='x', pady=(10, 10))

    def add_patient(self):
        name = self.pname_entry.get()
        age = self.page_entry.get()
        sex = self.psex_entry.get()
        add1 = self.padd_entry.get()
        mob = self.pmob_entry.get()
        guardian = self.pguardian_entry.get()
        if name and age and sex and add1 and mob and guardian:
            db_functions.create_patient(name, age, sex, add1, mob, guardian)



if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = PatientPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()
