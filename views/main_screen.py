from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
# import configs as cfgs
from .configs import *
from .form import Form


class Table:
    def __init__(self, root, header_mapping, controller=None):
        self._table = ttk.Treeview(root, show='headings')
        self._header = header_mapping
        self._table['column'] = tuple(header_mapping.keys())
        self._controller = controller

        self._table.column("#0", width=0,  stretch=NO)
        sizes = [80, 150, 150, 150]
        for i,h in enumerate(header_mapping.keys()):
            self._table.column(h,anchor=CENTER, width=sizes[i])
            self._table.heading(h, text=header_mapping[h],anchor=CENTER)

        self._table.grid(row=2, column=0,sticky='n')
        self._table.bind("<Double-1>", self.double_click)
        self._table.bind('<Button-1>', self.one_click)

        self._form = None

        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self._table.yview)
        self._table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=1, sticky='wsn')
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # # add data to the treeview
        # for contact in contacts:
        #     self._table.insert('', tk.END, values=contact)
        employees = []
        for i, e in enumerate(controller.getEmployeeList()):
            employees.append((str(i), e.get_name(), e.get_dob(), e.get_position()))

        for e in employees:
            self._table.insert('', tk.END, values=e)
        self.curr_item = None


    # def insert(self, )

    def double_click(self,event):
        selected_item = self._table.selection()[0]
        item = self._table.item(selected_item)
        record = item['values']
        self.curr_item = record
        if self._form is None:
            self._form = Form(action='view', info=record, controller=self._controller)
    def one_click(self, event):
        selected_item = self._table.selection()[0]
        item = self._table.item(selected_item)
        self.curr_item = item['values']


    def delete(self):
        for i in self._table.get_children():
            self._table.delete(i)
        self.curr_item = None
        self._form = None

    def get_sellected_item(self):
        return self.curr_item

class MainScreen:

    def __init__(self, controller=None):
        root = Tk()  # create root window
        root.title("Employee Management")  # title of the GUI window
        root.maxsize(WIDTH, HEIGHT)  # specify the max size the window can expand to
        root.minsize(WIDTH, HEIGHT)
        root.eval('tk::PlaceWindow . center')
        root.config(bg="skyblue")  # specify background color
        self._root = root
        self._controller = controller
        
        # self.create_left_frame()
        self.create_right_frame()
        self.create_left_frame()

        label_total = Label(self._root, text='TOTAL: ', font=('verdana',14), bg='#3498db')
        label_value = Label(self._root, text='11', font=('verdana',14),bg='skyblue')
        label_total.grid(row=3, column=0,pady=20,)
        label_value.grid(row=3, column=0, sticky='e')

        self._form = None
        
        
        
        self._root.mainloop()

    # Create left and right frames
    def create_right_frame(self):
        self.right_frame = Frame(self._root, width=RIGHT_FRAME_WIDTH,height=RIGHT_FRAME_HEIGHT, bg='grey')
        self.right_frame.grid(row=2, column=2, sticky='se')

        self.add_btn = Button(self.right_frame, text='ADD',font=('verdana',14), bg='white',width=7,command=self.add)
        self.add_btn.grid(row = 2, column=2, padx=10,pady=10)

        self.modify_btn = Button(self.right_frame, text='MODIFY',font=('verdana',14), bg='white',width=8,command=self.modify)
        self.modify_btn.grid(row = 3, column=2,padx=10,pady=10)

        self.delele_btn = Button(self.right_frame, text='DELETE',font=('verdana',14), bg='white',width=8,command=self.delete)
        self.delele_btn.grid(row = 4, column=2,padx=10,pady=10 )

        self.refresh_btn = Button(self.right_frame, text='REFRESH',font=('verdana',14), bg='white',width=8)
        self.refresh_btn.grid(row = 5, column=2,padx=10,pady=10 )
        

    def create_left_frame(self,):
        # left_frame = Frame(self._root, width=cfgs.LEFT_FRAME_WIDTH, bg='white')
        # left_frame.grid(row=0, column=0, padx=10, pady=10)
        self.entry_search = tk.Entry(self._root, font=('verdana',14))
        self.search_btn = Button(self._root, text='SEARCH',font=('verdana',14), bg='white',width=8)

        self.entry_search.grid(row=1, column=0,padx=10, pady=20)
        self.search_btn.grid(row=1, column=0, sticky='e')
        self.table = Table(self._root,HEADER_MAPPING, self._controller)
        # table = Table(left_frame, cfgs.HEADER_MAPPING)
        # left_frame.grid(row=0, column=0, padx=10, pady=5)
        # self.left_frame = left_frame

    def add(self):
        self._form = Form(action='add', controller=self._controller)

    def modify(self):
        info = self.table.get_sellected_item()
        if info is not None:
            self._form = Form(action='edit',info=info, controller=self._controller)

    def delete(self):
        pass

    def refresh(self):
        self.table.delete()



if __name__ == '__main__':
    temp = MainScreen()