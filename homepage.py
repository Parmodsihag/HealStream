import tkinter as tk

from mytheme import Colors
from tkinter import ttk

class HomePage(tk.Frame):
    # accounts_df = mypandasfile.customer_df
    # # accounts_df = mypandasfile.get_all_list()
    # all_positive_df = accounts_df.loc[accounts_df['Amount'] >=0]
    # all_negative_df = accounts_df.loc[accounts_df['Amount'] <0]
    # print(all_positive_df)

    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.BACKGROUND1, **kwargs)

        img = tk.PhotoImage(file="myicons\\framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        # self.jbb_logo_image = tk.PhotoImage(file='myicons/logonew.png')
        # self.jbb_logo_image_label = tk.Label(self , image=self.jbb_logo_image, bg=Colors.BACKGROUND1)
        # self.jbb_logo_image_label.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=.6)

        # self.all_graphs_function()
        # self.sales_data_frame = SalesData(self)
        # self.sales_data_frame.place(relx=0.01, rely=0.01, relheight=0.485, relwidth=0.4)
    
