import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from datetime import datetime

from mytheme import Colors
from homepage import HomePage
from depatment import DepartmentPage
from doctors import DoctorPage
from reports import ReportsPage
from patients import PatientPage

# from modifypage import ModifyPage

class CustomLabel(tk.Frame):
    def __init__(self, master, text, frame_to_link, x, **kwargs):
        super().__init__(master, highlightbackground=Colors.ACTIVE_FOREGROUND, **kwargs)
        self.customlabel = tk.Label(self, text=text, font=("Consolas", 14), anchor="e")#, pady=10, highlightthickness=0, padx=20, pady=10, anchor="w", highlightthickness=0, highlightbackground=Colors.ACTIVE_FOREGROUND)
        self.customlabel.pack(fill='both', side="right", expand=1)

        self.customlabel1 = tk.Label(self, text="", font=("Consolas", 20), anchor='w')
        self.customlabel1.pack(side='left',fill='x')#, expand=1)

        self.frame1 = frame_to_link
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.customlabel.bind("<Button-1>", self.on_click)
        self.customlabel1.bind("<Button-1>", self.on_click)
        
        self.normal_bg = Colors.BACKGROUND1
        self.normal_fg = Colors.FOREGROUND
        self.hover_bg = Colors.LIGHT_BG
        self.hover_fg = Colors.FOREGROUND
        self.active_bg = Colors.ACTIVE_BACKGROUND
        self.active_fg = Colors.FG_SHADE_1
        
        self.is_active = False
        self.is_hovering = False
        self.customlabel.configure(background=self.normal_bg, foreground=self.normal_fg)
        self.customlabel1.configure(background=self.normal_bg)
        self.master.master.bind(f"<Alt-{x}>", self.alt_key)  # Bind Alt + x key
        self.x = x
        # print(self.x)

    def alt_key(self, event):
        # print(event.char.isdigit())
        if event.char == self.x:
            self.on_click(event)

        # if event.char.isdigit():
        #     key_pressed = int(event.char)
        #     print(key_pressed, self.x, key_pressed== self.x)
        #     if key_pressed == self.x:
        #         self.on_click(event)

        
    def on_enter(self, event):
        if not self.is_active:
            self.customlabel.configure(background=self.hover_bg, foreground=self.hover_fg)
            self.customlabel1.configure(background=self.hover_bg, foreground=self.hover_fg)
            self.is_hovering = True
            
    def on_leave(self, event):
        if not self.is_active:
            self.customlabel.configure(background=self.normal_bg, foreground=self.normal_fg)
            self.customlabel1.configure(background=self.normal_bg, foreground=self.normal_fg)
            self.is_hovering = False
            
    def on_click(self, event):
        # print('click')
        for  i in self.master.winfo_children():
            # print('clicksdf')
            i.set_inactive()
    
        self.is_active = True
        self.is_hovering = False
        self.customlabel.configure( foreground=self.active_fg)#, relief='groove')
        self.customlabel1.configure( background=self.active_fg)#, relief='groove')
        self.frame1.tkraise()
        
    def set_inactive(self):
        self.is_active = False
        self.is_hovering = False
        self.customlabel.configure(background=self.normal_bg, foreground=self.normal_fg)
        self.customlabel1.configure(background=self.normal_bg)

    def set_active(self):
        self.is_active = True
        self.is_hovering = False
        self.customlabel.configure(foreground=self.active_fg)#, relief='groove')
        self.customlabel1.configure(background=self.active_fg)#, relief='groove')
        self.frame1.tkraise()


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My App")
        self.state("zoomed")
        self.config(background=Colors.BACKGROUND1)

        img = tk.PhotoImage(file="myicons\\framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        style=ttk.Style()
        style.theme_create('mytheme', parent='alt', 
                        settings={
                            'TCombobox':
                            {
                                'configure':
                                {
                                'selectbackground': "#4EC5F1",
                                'fieldbackground': Colors.BACKGROUND3,
                                'background': Colors.BACKGROUND3,
                                'foreground': Colors.FG_SHADE_1,
                                'arrowcolor':Colors.FOREGROUND,
                                'arrowsize': 18,
                                'font':"Consolas 14"
                                }
                            },
                            'Treeview':{
                                'configure':
                                {
                                    'rowheight': 20,
                                    'fieldbackground': Colors.BACKGROUND,
                                    'font': 'Ubantu 10'
                                }
                            }
                        }
                    )
        style.theme_use('mytheme')
        style.configure("Treeview.Heading", foreground='#a0dad0', background=Colors.BACKGROUND1, font='Consolas 12')

        # main 4 parts 
        self.title_bar = tk.Frame(self, bg=Colors.BG_SHADE_1)
        self.title_bar.place(relx=0, rely=0, relheight=0.04, relwidth=1)

        self.menu_frame = tk.Frame(self, bg=Colors.BACKGROUND1)
        self.menu_frame.place(relx=0.005, rely=0.255, relheight=0.675, relwidth=0.095)
        self.action_frame = tk.Frame(self, bg=Colors.BACKGROUND1)
        self.action_frame.place(relx=0.1, rely=0.04, relheight=0.9, relwidth=0.9)
        self.status_bar = tk.Frame(self, bg=Colors.BG_SHADE_1)
        self.status_bar.place(relx=0, rely=0.94, relheight=0.06, relwidth=1)

        # logo
        self.logo_frame = tk.Frame(self, bg=Colors.BACKGROUND1)
        self.logo_frame.place(relx=0.005, rely=0.05, relheight=0.2, relwidth=0.095)
        self.logo_image = PhotoImage(file="myicons/logo3.png")
        logo_image_label = tk.Label(self.logo_frame, image=self.logo_image, background=Colors.BACKGROUND1)
        logo_image_label.pack( fill="both", expand=1)
        
        # img = tk.PhotoImage(file="myicons\\framebg2.png")

        # self.background_title = tk.Label(self.logo_frame, image=img)
        # self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        # self.img = img

        self.title_bar_f(self.title_bar)
        
        self.status = tk.StringVar()
        self.statusl = tk.Label(self.status_bar, textvariable=self.status, font="Consolas 18", background=Colors.BG_SHADE_1, fg=Colors.ACTIVE_FOREGROUND)
        self.statusl.pack(anchor="e")
        self.status.set("|Status Bar|")
        

        # adding other views frames
        self.homeframe = HomePage(self.action_frame)
        self.homeframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.patientframe = PatientPage(self.action_frame)
        self.patientframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.doctorframe = DoctorPage(self.action_frame)
        self.doctorframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.deparmentframe = DepartmentPage(self.action_frame)
        self.deparmentframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.reportframe = ReportsPage(self.action_frame)
        self.reportframe.place(relx=0, rely=0, relheight=1, relwidth=1)
        # self.modifyframe = ModifyPage(self.action_frame)
        # self.modifyframe.place(relx=0, rely=0, relheight=1, relwidth=1)

        # adding labels in menu
        self.home_page_label = CustomLabel(self.menu_frame, "Home ",self.homeframe, "h")
        self.home_page_label.pack( fill="x")
        self.patient_page_label = CustomLabel(self.menu_frame, 'Patient ', self.patientframe, 'p')
        self.patient_page_label.pack(fill='x')
        self.doctor_page_label = CustomLabel(self.menu_frame, 'Doctor ', self.doctorframe, 'd')
        self.doctor_page_label.pack(fill='x')
        self.department_page_label = CustomLabel(self.menu_frame, "Department ",self.deparmentframe, "t")
        self.department_page_label.pack( fill="x")
        self.report_frame_label = CustomLabel(self.menu_frame, "Reports ", self.reportframe, 'r')
        self.report_frame_label.pack( fill="x")
        # self.modify_frame_label = CustomLabel(self.menu_frame, "Modify ", self.modifyframe, 'm')
        # self.modify_frame_label.pack( fill="x")

        # activating home page
        self.home_page_label.set_active()

        self.bind()
        # self.report_frame_label.set_active()
        # self.modify_frame_label.set_active()

    def title_bar_f(self, master):
        today = datetime.now().strftime('%d %m|%Y')
        company_name = tk.Label(master, text="HealStream", font="Consolas 16", bg= Colors.BG_SHADE_1, fg=Colors.FG_SHADE_3)
        company_name.place(relx=0.01, rely=0)
        today_date = tk.Label(master, text=today, font="Consolas 16", bg= Colors.BG_SHADE_1, fg=Colors.FG_SHADE_1)
        today_date.place(relx=0.9, rely=0)

    def set_status(self,s):
        self.status.set(s)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
