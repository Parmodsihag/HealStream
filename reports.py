        
import tkinter as tk

from mytheme import Colors
from tkinter import ttk

import datetime
import db_functions
# import accounts
# import inventory
# import database
# import krar
# import mypandasfile

class ReportsPage(tk.Frame):
    # accounts_df = mypandasfile.customer_df

    def __init__(self, master, **kwargs):
        super().__init__(master, bg=Colors.ACTIVE_BACKGROUND, **kwargs)

        img = tk.PhotoImage(file="C://HealStream//images//framebg2.png")

        self.background_title = tk.Label(self, image=img)
        self.background_title.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.img = img

        self.upper_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        self.upper_frame.place(relx=0.01, rely=0.01, relheight=0.09, relwidth=0.98)
        self.table_selector()

        self.table_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        self.table_frame.place(relx=0.01, rely=0.11, relheight=0.88, relwidth=0.98)

        # self.default_lable = tk.Label(self.table_frame, bg=Colors.ACTIVE_BACKGROUND, text="Select a table", font="Consolas 36")
        # self.default_lable.pack(expand=1, fill=tk.BOTH)

        # self.sort_by_dropdown.set("Customer Id")
        # self.sort_by_combobox_select()


    
    def table_selector(self):
        font = "Consolas 16"
        self.db = "C://HealStream//data//healstream.db"
        # Create table dropdown
        cur = db_functions.execute_query("SELECT name FROM sqlite_master WHERE type='table'")
        self.table_list = cur.fetchall()
        table_label = tk.Label(self.upper_frame, text="Table:", bg=Colors.BACKGROUND, fg=Colors.ACTIVE_FOREGROUND, font=font)
        table_label.pack(side="left", padx=5, pady=5)
        self.table_dropdown = ttk.Combobox(self.upper_frame, values= self.table_list, width=20, font=font)
        self.table_dropdown.pack(side="left", padx=5, pady=5)
        # self.table_dropdown.bind('<<ComboboxSelected>>', lambda e : self.update_table_names())

        # Create button
        show_button = tk.Button(self.upper_frame, text="Show Data", command=self.show_table, bg=Colors.BACKGROUND3, fg=Colors.FG_SHADE_3, relief='groove', font="Consolas 14")
        show_button.pack(side="left", padx=5, pady=5)


    def make_my_table(self, df):
        for widget in self.table_frame.winfo_children():
                widget.destroy()
        columns = df.columns.tolist()
            
        tree = ttk.Treeview(self.table_frame)
        tree['columns'] = columns
        for column in columns:
            tree.heading(column, text=column)
        
        c = 0
        for index, row in df.iterrows():
            tg='even'
            if c%2:
                tg='odd'
            c+=1
            tree.insert("", 'end', text=c, values=row.tolist(), tags=tg)

        # tree.tag_configure('odd', background=Colors.ACTIVE_BACKGROUND, foreground=Colors.FG_SHADE_1)
        # tree.tag_configure('even', background=Colors.ACTIVE_FOREGROUND, foreground=Colors.BG_SHADE_2)
        tree.tag_configure('odd', background=Colors.BACKGROUND, foreground=Colors.ACTIVE_FOREGROUND)
        tree.tag_configure('even', background=Colors.BACKGROUND1, foreground=Colors.ACTIVE_FOREGROUND)
        tree.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    def update_table_names(self):
        selected_db = self.db
        if selected_db:
            cur = db_functions.execute_query("SELECT name FROM sqlite_master WHERE type='table'")
            self.table_list = cur.fetchall()
            self.table_dropdown.config(values=self.table_list)
            
            # print(selected_db, self.table_list)

    def show_data(self):
        # Get selected database and table
        selected_db = self.db
        selected_table = self.table_dropdown.get()
        column_names = []
        column_list = []
        table_data = []
        tag = 0
        if selected_db and selected_table:
            cursor = db_functions.execute_query(f"PRAGMA table_info({selected_table})")
            column_list = cursor.fetchall()
            table_data = cursor.execute(f"SELECT * FROM {selected_table}").fetchall()
            for column in column_list:
                column_names.append(column[1])
        
        return column_names, table_data
    
    # def show_table(self):
    #     column_name, table_data = self.show_data()
    #     if column_name and table_data:
    #         # print("emot")

    #         for widget in self.table_frame.winfo_children():
    #                 widget.destroy()
                
    #         tree = ttk.Treeview(self.table_frame)
    #         tree['columns'] = column_name
    #         tree.column('#0', width=1, minwidth=1)

    #         for i in column_name:
    #             tree.column(i, width=50)#, anchor='center')
    #             tree.heading(i, text=i)
            
    #         c = 0
    #         for i in table_data:
    #             c += 1
    #             tg = 'odd'
    #             if c%2 == 0:
    #                 tg = "even"
    #             tree.insert('', c, text=c, values=i, tags = tg )

    #         tree.tag_configure('odd', background=Colors.BACKGROUND, foreground=Colors.ACTIVE_FOREGROUND)
    #         tree.tag_configure('even', background=Colors.BACKGROUND1, foreground=Colors.ACTIVE_FOREGROUND)
    #         tree.pack(fill=tk.BOTH, expand=True, side=tk.TOP) 
    #     else:
    #         print("Empty fields for reports")

    def show_table(self):
        """
        Displays a table with alternating row colors based on fetched data.

        Handles empty data scenarios and potential errors gracefully.
        """

        column_names, table_data = self.show_data()

        # Clear existing table widgets before creating a new one
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        if column_names and table_data:
            tree = ttk.Treeview(self.table_frame)
            tree['columns'] = column_names
            tree.column('#0', width=1, minwidth=1)

            for i in column_names:
                tree.column(i, width=50, anchor='center')  # Set center alignment
                tree.heading(i, text=i)

            for i, row in enumerate(table_data):
                color = 'odd' if i % 2 == 0 else 'even'
                tree.insert('', tk.END, text=i + 1, values=row, tags=(color,))

            tree.tag_configure('odd', background=Colors.BACKGROUND, foreground=Colors.ACTIVE_FOREGROUND)
            tree.tag_configure('even', background=Colors.BACKGROUND1, foreground=Colors.ACTIVE_FOREGROUND)
            tree.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        else:
            # Handle empty data or errors (consider exception handling or custom message)
            print("No data available for the table.") 



if __name__ == "__main__":
    app = tk.Tk()
    app.state("zoomed")
    h = ReportsPage(app)
    h.pack(expand=1, fill="both")
    app.mainloop()

