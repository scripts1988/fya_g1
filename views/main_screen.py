from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
# import configs as cfgs
import configs as cfgs
from form import Form


class Table:
    def __init__(self, root, header_mapping):
        self._table = ttk.Treeview(root, show='headings')
        self._header = header_mapping
        self._table['column'] = tuple(header_mapping.keys())

        self._table.column("#0", width=0,  stretch=NO)
        sizes = [80, 150, 150, 150]
        for i,h in enumerate(header_mapping.keys()):
            self._table.column(h,anchor=CENTER, width=sizes[i])
            self._table.heading(h, text=header_mapping[h],anchor=CENTER)

        self._table.grid(row=1, column=0, sticky='nsew')
        self._table.bind("<Double-1>", self.double_click)
        self._table.bind('<Button-1>', self.one_click)

        self._form = None

        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self._table.yview)
        self._table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

        # self._table.pack()

        
        # Test data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'id {n}',f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        for contact in contacts:
            self._table.insert('', tk.END, values=contact)

    def double_click(self,event):
        selected_item = self._table.selection()[0]
        item = self._table.item(selected_item)
        record = item['values']
        if self._form is None:
            self._form = Form(action='view', info=record)
        self._form.set_text(info=record)
    
    def one_click(self, event):
        selected_item = self._table.selection()[0]
        item = self._table.item(selected_item)
        record = item['values']


    def delete(self):
        for i in self._table.get_children():
            self._table.delete(i)



class MainScreen:

    def __init__(self):
        root = Tk()  # create root window
        root.title("Employee Management")  # title of the GUI window
        root.maxsize(cfgs.WIDTH, cfgs.HEIGHT)  # specify the max size the window can expand to
        root.minsize(cfgs.WIDTH, cfgs.HEIGHT)
        root.eval('tk::PlaceWindow . center')
        root.config(bg="skyblue")  # specify background color
        self._root = root
        
        # self.create_left_frame()
        self.create_right_frame()
        table = Table(self._root,cfgs.HEADER_MAPPING)

        self._form = None
        
        
        
        self._root.mainloop()

    # Create left and right frames
    def create_right_frame(self):
        # right_frame = Frame(self._root, width=cfgs.RIGHT_FRAME_WIDTH, bg='grey')
        # right_frame.grid(row=0, column=1, padx=10, pady=5)

        add_btn = Button(self._root, text='ADD',font=('verdana',14), bg='white',width=7)
        add_btn.grid(row = 1, column=2, padx=10,pady=10)

        modify_btn = Button(self._root, text='MODIFY',font=('verdana',14), bg='white',width=8)
        modify_btn.grid(row = 2, column=2,padx=10)

        delele_btn = Button(self._root, text='DELETE',font=('verdana',14), bg='white',width=8)
        delele_btn.grid(row = 3, column=2,padx=10)



    def create_left_frame(self,):
        left_frame = Frame(self._root, width=cfgs.LEFT_FRAME_WIDTH,height=cfgs.LEFT_FRAME_HEIGHT, bg='white')
        left_frame.grid(row=0, column=0, padx=10, pady=5)
        # table = Table(left_frame, cfgs.HEADER_MAPPING)
        # left_frame.grid(row=0, column=0, padx=10, pady=5)
        return left_frame



if __name__ == '__main__':
    temp = MainScreen()