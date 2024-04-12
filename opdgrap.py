import re
import tkinter as tk
import win32com.client
import win32print

from datetime import datetime, timedelta
from docxtpl import DocxTemplate
from tkinter import ttk

from mytheme import Colors
import db_functions

class OPDPage(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.BACKGROUND1, **kwargs)

        self.word = win32com.client.Dispatch("Word.Application")
        self.word.Visible = False

        img = tk.PhotoImage(file="C://HealStream//images//framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        APP_FONT = "Consolas 12"
        APP_FONT1 = "Consolas 14"

        
        # main frame to include all frames
        self.main_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        self.main_frame.place(relx=0.01, rely=0.01, relwidth=.98, relheight=.98)

        self.background_title = tk.Label(self.main_frame, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.upper_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        self.upper_frame.place(relx=0, rely=0, relwidth=1, relheight=.49)
        self.lower_frame = tk.Frame(self.main_frame, bg=Colors.BACKGROUND)
        self.lower_frame.place(relx=0, rely=.5, relwidth=1, relheight=.5)
        self.show_table()

        # self.create_table(self.lower_frame, [], db_functions.get_all_opd_today(datetime.today().strftime('%d-%m-%Y')))

        # title frame
        title_frame = tk.Frame(self.upper_frame, bg=Colors.BACKGROUND1)
        title_frame.place(relx=0, rely=0, relheight=.1, relwidth=1)
        title_name_label = tk.Label(title_frame, text="OPD", font="Consolas 18", bg=Colors.BACKGROUND1, fg=Colors.FG_SHADE_3, anchor='center')
        title_name_label.pack(padx=40, fill='x')

        # text variables
        self.opd_number_var = tk.IntVar()
        self.uhid_var = tk.IntVar()
        self.patient_details_var = tk.StringVar()
        self.patient_names_choices = []
        self.doctor_details_var = tk.StringVar()
        self.doctor_names_choices = []

        self.slip_date_var = tk.StringVar()
        self.slip_time_var = tk.StringVar()
        self.valid_upto_var = tk.StringVar()
        self.amount_var = tk.IntVar()

        self.slip_date_var.set(datetime.today().strftime('%d-%m-%Y'))
        # opd number
        opd_number_label = tk.Label(self.upper_frame, text='OPD No', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        opd_number_label.place(relx=0.02, rely=.12)
        self.opd_number_entry = tk.Entry(self.upper_frame, textvariable=self.opd_number_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.opd_number_entry.place(relx=.02, rely=.21, relwidth=.1)
        self.opd_number_var.set(db_functions.get_opd_number(self.slip_date_var.get()))
        self.opd_number_entry.bind('<Enter>', lambda e:self.opd_number_var.set(db_functions.get_opd_number(self.slip_date_var.get())))

        # uhid
        uhid_number_label = tk.Label(self.upper_frame, text='UHID No', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        uhid_number_label.place(relx=0.2, rely=.12)
        self.uhid_number_entry = tk.Entry(self.upper_frame, textvariable=self.uhid_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.uhid_number_entry.place(relx=.2, rely=.21, relwidth=.1)
        
        # find uhid button
        find_button = tk.Button(self.upper_frame, text="Find Patient", font="Consolas 14", command=self.find_patient, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        find_button.place(relx=.34, rely=.16, relwidth=.2)

        # patient details 
        patient_details_label = tk.Label(self.upper_frame, text='Patient Details', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        patient_details_label.place(relx=0.58, rely=.12)
        self.patient_details_dropdown = ttk.Combobox(self.upper_frame, textvariable=self.patient_details_var, values=self.patient_names_choices, font=APP_FONT1)
        self.patient_details_dropdown.place(relx=.58, rely=.21, relwidth=.4)
        self.patient_details_dropdown.bind('<Enter>', lambda e: self.patient_details_dropdown.config(values=self.get_patients()))
        self.patient_details_dropdown.bind('<Down>', lambda e: self.update_listbox_items(self.patient_details_dropdown, self.get_patients(), self.patient_details_var.get()))
        self.patient_details_dropdown.bind('<<ComboboxSelected>>', lambda e : self.set_uhid())

        # patient details 
        doctor_details_label = tk.Label(self.upper_frame, text='Doctor', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        doctor_details_label.place(relx=.02, rely=.4)
        self.doctor_details_dropdown = ttk.Combobox(self.upper_frame, textvariable=self.doctor_details_var, values=self.doctor_names_choices, font=APP_FONT1)
        self.doctor_details_dropdown.place(relx=.02, rely=.5, relwidth=.3)
        self.doctor_details_dropdown.bind('<Enter>', lambda e: self.doctor_details_dropdown.config(values=self.get_doctors()))
        self.doctor_details_dropdown.bind('<Down>', lambda e: self.update_listbox_items(self.doctor_details_dropdown, self.get_doctors(), self.doctor_details_var.get()))

        # slip date
        slip_date_label = tk.Label(self.upper_frame, text='Date', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        slip_date_label.place(relx=0.36, rely=.4)
        self.slip_date_entry = tk.Entry(self.upper_frame, textvariable=self.slip_date_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.slip_date_entry.place(relx=.36, rely=.5, relwidth=.1)

        # slip time
        slip_time_label = tk.Label(self.upper_frame, text='Time', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        slip_time_label.place(relx=0.48, rely=.4)
        self.slip_time_entry = tk.Entry(self.upper_frame, textvariable=self.slip_time_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.slip_time_entry.place(relx=.48, rely=.5, relwidth=.1)
        self.slip_time_entry.bind('<Enter>', lambda e:self.slip_time_var.set(datetime.today().strftime('%I:%M:%S %p')))
        self.slip_time_var.set(datetime.today().strftime('%I:%M:%S %p'))

        # slip valid upto
        valid_upto_label = tk.Label(self.upper_frame, text='Valid Upto', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        valid_upto_label.place(relx=0.62, rely=.4)
        self.valid_upto_entry = tk.Entry(self.upper_frame, textvariable=self.valid_upto_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.valid_upto_entry.place(relx=.62, rely=.5, relwidth=.14)
        seven_days = timedelta(days=7)
        future_time = datetime.today() + seven_days
        self.valid_upto_var.set(future_time.strftime('%d-%m-%Y'))

        # amount
        amount_label = tk.Label(self.upper_frame, text='Amount', font=APP_FONT, bg= Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, anchor='w')
        amount_label.place(relx=0.8, rely=.4)
        self.amount_entry = tk.Entry(self.upper_frame, textvariable=self.amount_var, font=APP_FONT1, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_1, relief='flat')
        self.amount_entry.place(relx=.8, rely=.5, relwidth=.1)
        
        # add opd button
        add_opd_button = tk.Button(self.upper_frame, text="Make OPD", font="Consolas 14", command=self.add_opd, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        add_opd_button.place(relx=.2, rely=.64, relwidth=.3, relheight=.3)
        print_opd_button = tk.Button(self.upper_frame, text="Print OPD", font="Consolas 14", command=self.print_opd, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove')
        print_opd_button.place(relx=.52, rely=.64, relwidth=.3, relheight=.3)

    def set_uhid(self):
        if self.patient_details_var.get():
            uhid = self.patient_details_var.get().split()
            self.uhid_var.set(uhid[0])

    def show_data(self):
        column_names = []
        column_list = []
        table_data = []
        selected_table = 'OPD_slips'
        cursor = db_functions.execute_query(f"PRAGMA table_info({selected_table})")
        column_list = cursor.fetchall()
        table_data = cursor.execute(f"SELECT * FROM {selected_table}").fetchall()
        table_data = db_functions.get_all_opd_today(datetime.today().strftime('%d-%m-%Y'))
        for column in column_list:
            column_names.append(column[1])
        
        return column_names, table_data

    def show_table(self):
        """
        Displays a table with alternating row colors based on fetched data.

        Handles empty data scenarios and potential errors gracefully.
        """

        column_names, table_data = self.show_data()

        # Clear existing table widgets before creating a new one
        for widget in self.lower_frame.winfo_children():
            widget.destroy()

        if column_names and table_data:
            self.mytree = ttk.Treeview(self.lower_frame, selectmode='browse')
            self.mytree['columns'] = column_names
            self.mytree.column('#0', width=1, minwidth=1)

            for i in column_names:
                self.mytree.column(i, width=50, anchor='center')  # Set center alignment
                self.mytree.heading(i, text=i)

            for i, row in enumerate(table_data):
                color = 'odd' if i % 2 == 0 else 'even'
                self.mytree.insert('', tk.END, text=i + 1, values=row, tags=(color,))

            self.mytree.tag_configure('odd', background=Colors.BACKGROUND, foreground=Colors.ACTIVE_FOREGROUND)
            self.mytree.tag_configure('even', background=Colors.BACKGROUND1, foreground=Colors.ACTIVE_FOREGROUND)
            self.mytree.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
            self.mytree.bind("<Double-1>", self.opd_slip_selected)
        else:
            # Handle empty data or errors (consider exception handling or custom message)
            print("No data available for the table.") 

    def opd_slip_selected(self, e):
        selected_row_id = self.mytree.focus()
        values = self.mytree.item(selected_row_id, 'values')
        if values:
            self.opd_number_var.set(values[1])
            self.uhid_var.set(values[2])
            self.patient_details_var.set(db_functions.get_patient_by_id(values[2]))
            self.doctor_details_var.set(db_functions.get_doctor_by_id(values[3]))

            self.slip_date_var.set(values[4])
            self.slip_time_var.set(values[5])
            self.valid_upto_var.set(values[6])
            self.amount_var.set(values[7])

    def update_listbox_items(self, lb, lst, pat):
        """
        Updates the listbox items based on a case-insensitive search pattern.

        Args:
            lb (tkinter.Listbox): The listbox widget to update.
            lst (list): The original list of items to search within.
            pat (str): The search pattern.
        """
        lsts = []
        for item in lst:
            if re.search(pat, f"{item[0]} {item[1]}", flags=re.IGNORECASE):
                lsts.append(item)
        lb.config(values=lsts)

    def add_opd(self):
        opd_number = self.opd_number_var.get()
        uhid = self.uhid_var.get()
        doctor_id = 0
        if self.doctor_details_var.get():
            doctor_id = self.doctor_details_var.get().split()[0]

        slip_date = self.slip_date_var.get()
        slip_time = self.slip_time_var.get()
        valid_upto = self.valid_upto_var.get()
        amount = self.amount_var.get()
        # print(dept_name)
        if opd_number and uhid and doctor_id and slip_date and slip_time and valid_upto and amount:
            if db_functions.check_opd_number_exists(opd_number, slip_date):
                if __name__ != "__main__":
                    self.master.master.set_status(f"{opd_number} SLIP already exist ")
                else:
                    print("Slip already exits with this number", opd_number, slip_date)

            else:
                db_functions.create_opd_slip(opd_number, uhid, doctor_id, slip_date, slip_time, valid_upto, amount)
                self.make_docx(opd_number, slip_date)
                self.show_table()
                self.opd_number_var.set(self.opd_number_var.get()+1)
                if __name__ != "__main__":
                    self.master.master.set_status(f"Slip added {opd_number} ")

    def print_opd(self):
        opd_number = self.opd_number_var.get()
        slip_date = self.slip_date_var.get()
        if db_functions.check_opd_number_exists(opd_number, slip_date):
            self.make_docx(opd_number, slip_date)
            self.print_docx_silently("C://HealStream//templates//temp.docx", self.word)

        else:
            self.add_opd()
    
    def make_docx(self, opd_number, slip_date):
        if opd_number and slip_date:
            details = db_functions.get_opd_slip(opd_number, slip_date)
            print(details[0])
            uhid_number = details[2]
            patient_d = db_functions.get_patient_by_id(uhid_number)
            patient_name = patient_d[1]
            age  = patient_d[2]
            sex = patient_d[3]
            address = patient_d[4]
            phone_number = patient_d[5]
            guardian = patient_d[6]
            doctor_d = db_functions.get_doctor_by_id(details[3])
            consultant = doctor_d[1]
            dept =  db_functions.get_department_by_id(doctor_d[2])[1]
            valid_upto = details[6]
            reg_fees = details[7]
            date = details[4]
            time = details[5]
            self.add_in_templet(patient_name, age, sex, address, phone_number, consultant, dept, reg_fees, opd_number, uhid_number, date, time, valid_upto, guardian)
            

    def find_patient(self):
        if self.uhid_var.get():
            patient_details = db_functions.get_patient_by_id(self.uhid_var.get())
            if patient_details:
                self.patient_details_var.set(patient_details)
            else:
                self.patient_details_var.set("Not found")
    
    def add_in_templet(self, patient_name, age, sex, address, phone_number, consultant, dept, reg_fees, opd_num, uhid, date, time, valid_upto, guardian):
        tpl = DocxTemplate('C://HealStream//templates//template.docx')
        context = {
            'patient_name': patient_name,
            'age': age,
            'sex': sex, 
            'address': address, 
            'phone_number': phone_number, 
            'consultant': consultant,
            'dept':dept, 
            'reg_fees': reg_fees, 
            'opd_num': opd_num, 
            'uhid': uhid, 
            'date_time':f"{date}  {time}", 
            'valid_upto' :valid_upto,  
            'guardian':guardian
        }
        tpl.render(context)
        # tpl.save(f'new\{date}_{opd_num}.docx')
        tpl.save("C://HealStream//templates//temp.docx")

    def print_docx_silently(self, file_path, word):
        """Prints a docx file silently in the background.

        Args:
            file_path (str): The path to the docx file.
        """

          # Hide Word application window

        doc = word.Documents.Open(file_path)

        # Set printer properties for silent printing (adjust as needed)
        printer = word.ActivePrinter
        word.ActivePrinter = printer + f" on {win32print.GetDefaultPrinter()}"  # Replace "Ne00:" with your printer name
        word.Options.PrintBackground = False  # Disable background printing

        doc.PrintOut()  # Print the document

        doc.Close()

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
    # h.word.Quit()
