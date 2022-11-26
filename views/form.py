from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

from .configs import *


class Form:
    def __init__(self,root, action='view', info=None, controller=None):
        self._info = info
        self._action = action
        self._controller = controller
        self._root = root
        form = Toplevel()  # create root window
        form.title("Employee")  # title of the GUI window
        form.maxsize(WIDTH_FORM, HEIGHT_FORM)  # specify the max size the window can expand to
        form.minsize(WIDTH_FORM, HEIGHT_FORM)
        form.config(bg="white") 
        
        # form.eval('tk::PlaceWindow . center')

        label_id = tk.Label(form, text=HEADER_MAPPING['id'], font=('verdana',14), bg='#3498db')
        self.entry_id = tk.Label(form, font=('verdana',14),text='')

        label_name = tk.Label(form, text=HEADER_MAPPING['name'], font=('verdana',14), bg='#3498db')
        self.entry_name = tk.Entry(form, font=('verdana',14))


        label_dob = tk.Label(form, text=HEADER_MAPPING['dob'], font=('verdana',14), bg='#3498db')
        self.entry_dob = tk.Entry(form, font=('verdana',14), )

        label_pos = tk.Label(form, text=HEADER_MAPPING['position'], font=('verdana',14), bg='#3498db')
        self.entry_pos = tk.Entry(form, font=('verdana',14))

        label_id.grid(row=0, column=0, sticky='e')
        self.entry_id.grid(row=0, column=1, padx=40, pady=10,sticky='w')


        label_name.grid(row=1, column=0, sticky='e')
        self.entry_name.grid(row=1, column=1, padx=40,pady=10)


        label_dob.grid(row=3, column=0, sticky='e')
        self.entry_dob.grid(row=3, column=1, padx=40,pady=10)

        label_pos.grid(row=4, column=0, sticky='e')
        self.entry_pos.grid(row=4, column=1, padx=40,pady=10)

        self.cancel_btn = Button(form, text='CANCEL',font=('verdana',14), bg='white', width=5, command=form.destroy)
        self.cancel_btn.grid(row=5, column=0, padx=10, sticky='ne')

        self.action_btn = Button(form, text=ACTION_MAPPING[action],font=('verdana',14), bg='white', width=5, command=self.action)
        self.action_btn.grid(row=5, column=1, padx=10, )

        self._entries = [self.entry_id, self.entry_name, self.entry_dob, self.entry_pos]
        # self.set_text(info)
        self._form = form

        self.set_text(info=info)
        self._form.mainloop()

    def set_text(self,info = None):
        if info is not None:
            for i, e in enumerate(self._entries):
                if i == 0:
                    self.entry_id.config(text=str(info[i]))
                    continue
                e.insert(0,self._info[i])
            
            self._form.update()
    
    def action(self):
        if self._action == 'view':
            return self._form.destroy()
        
        if self._action == 'add':
            try:
                name = self.entry_name.get()
                dob = self.entry_dob.get()
                pos = self.entry_pos.get()
                self._controller.add(name, dob, pos)
                self._controller.saveData()
                # print('Hwllpo')
                self._root.refresh()

                showinfo(message="Add employee succesfully")
            except:
                showinfo(message= "Add employee failed")
            self._form.destroy()

        
        if self._action == 'edit':
            try:
                id = int(self.entry_id['text'])
                name = self.entry_name.get()
                dob = self.entry_dob.get()
                pos = self.entry_pos.get()
                self._controller.modify(id, name,dob, pos)
                self._controller.saveData()

                self._root.refresh()
                showinfo(message="Modify employee succesfully")
            except:

                showinfo(message="Modify employee failed")

            self._form.destroy()

        

if __name__ == '__main__':
    tmp = Form()