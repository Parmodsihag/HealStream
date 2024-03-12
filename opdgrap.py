import tkinter as tk

import db_functions
from tkinter import ttk
from mytheme import Colors
from datetime import datetime




class OPDPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.BACKGROUND1, **kwargs)

        img = tk.PhotoImage(file="myicons\\framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        APP_FONT = "Consolas 12"
        APP_FONT1 = "Consolas 14"

        
        # main frame to include all frames
        self.main_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        self.main_frame.place(relx=0.3, rely=0.01, relwidth=.4, relheight=.98)
        self.background_title = tk.Label(self.main_frame, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        # title frame
        title_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND1)
        title_frame.pack(fill='x', pady=2, padx=10)
        title_name_label = tk.Label(title_frame, text="OPD", font="Consolas 18", bg=Colors.BACKGROUND1, fg=Colors.FG_SHADE_3, anchor='center')
        title_name_label.pack(padx=40, fill='x')


        # GROUP 1
        frame1 = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        frame1.pack(fill='x', pady=(10,0), padx=10)
        # OPD Entry Box
        opd_number_frame = tk.Frame(frame1, bg=Colors.BACKGROUND)
        opd_number_frame.pack(fill='x', side='left', expand=1)
        opd_number_label = tk.Label(opd_number_frame, text="OPD No ", font=APP_FONT, bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        opd_number_label.pack(fill='x', padx=(40, 10), pady=(10,0))
        self.opd_number_entry = tk.Entry(opd_number_frame, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.opd_number_entry.pack(fill='x', padx=(40, 10), pady=(0,10))
        # self.opd_number_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))
        # UHID Entry Box
        uhid_frame = tk.Frame(frame1, bg=Colors.BACKGROUND)
        uhid_frame.pack(fill='x', side='left', expand=1)
        uhid_label = tk.Label(uhid_frame, text="UHID No ", font=APP_FONT, bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        uhid_label.pack(fill='x')
        self.uhid_entry = tk.Entry(uhid_frame, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.uhid_entry.pack(fill='x', padx=(0,40))

        # Patient name Dropdown Menu
        patient_name_frame  = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        patient_name_frame.pack( fill='x', pady=10, padx=10)
        patient_name_label = tk.Label(patient_name_frame, text="Patient", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_name_label.pack(padx=40, fill='x')
        patient_name_choices = self.get_patients()
        self.patient_name_dropdown = ttk.Combobox(patient_name_frame, values=patient_name_choices, font="Consolas 14")
        self.patient_name_dropdown.pack(padx=40, pady=(0,10), fill='x')
        self.patient_name_dropdown.bind('<Enter>', lambda e: self.patient_name_dropdown.config(values=self.get_patients()))
        
        # doctor name Dropdown Menu
        doctor_name_frame  = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        doctor_name_frame.pack( fill='x', pady=10, padx=10)
        doctor_name_label = tk.Label(doctor_name_frame, text="Doctor", font="Consolas 12", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        doctor_name_label.pack(padx=40, fill='x')
        doctor_name_choices = self.get_patients()
        self.doctor_name_dropdown = ttk.Combobox(doctor_name_frame, values=doctor_name_choices, font="Consolas 14")
        self.doctor_name_dropdown.pack(padx=40, pady=(0,10), fill='x')
        self.doctor_name_dropdown.bind('<Enter>', lambda e: self.doctor_name_dropdown.config(values=self.get_doctors()))

        # Date Entry Box
        date_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        date_frame.pack(fill='x', pady=10, padx=10)
        date_label = tk.Label(date_frame, text="Date", font=APP_FONT, bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        date_label.pack(padx=40, fill='x')
        self.date_entry = tk.Entry(date_frame, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.date_entry.pack(padx=40, pady=(0,10), fill='x')
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Valid upto Entry Box
        vdate_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        vdate_frame.pack(fill='x', pady=10, padx=10)
        vdate_label = tk.Label(vdate_frame, text="Valid upto", font=APP_FONT, bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        vdate_label.pack(padx=40, fill='x')
        self.vdate_entry = tk.Entry(vdate_frame, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.vdate_entry.pack(padx=40, pady=(0,10), fill='x')
        self.vdate_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        # Amount entry box
        amount_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        amount_frame.pack(fill='x', pady=10, padx=10)
        amount_label = tk.Label(amount_frame, text="Amount", font=APP_FONT, bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        amount_label.pack(padx=40, fill='x')
        self.amount_entry = tk.Entry(amount_frame, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.amount_entry.pack(padx=40, pady=(0,10), fill='x')

        # button frame
        button_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        button_frame.pack(fill='x', pady=(10,10), padx=10)
        add_button = tk.Button(button_frame, text="Make OPD", font="Consolas 14", command=self.add_opd, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        add_button.pack(padx=40, fill='x', pady=(10, 10))

    def add_opd(self):
        opd_number = self.opd_number_entry.get()
        uhid_number = self.uhid_entry.get()
        patient_name = self.patient_name_dropdown.get()
        doctor_name = self.doctor_name_dropdown.get()
        opd_date = self.date_entry.get()
        valid_upto = self.vdate_entry.get()
        amount = self.amount_entry.get()
        # print(dept_name)
        if opd_number and uhid_number and patient_name and doctor_name and opd_date and valid_upto and amount:
            db_functions.create_opd_slip(opd_number, patient_name.split()[0], doctor_name.split()[0], opd_date, valid_upto, amount, uhid_number)
            self.make_opd_slip_in_docx()

    def make_opd_slip_in_docx(self):
        pass

    def get_patients(self):
        return db_functions.get_all_patients()
    
    def get_doctors(self):
        return db_functions.get_all_doctors()


if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = OPDPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()
