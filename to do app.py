import tkinter
import tkinter.messagebox
import pickle
#-------------------------------------------------------------------
root=tkinter.Tk()
root.title("To Do List")


def add_item():
    task = entry1.get()
    if task!="":
        listbox.insert(tkinter.END, task)
        entry1.delete(0,tkinter.END)
    else: 
        tkinter.messagebox.showwarning(title="Warning!", message="Empty task entered.")
    
def delete_item():
    try:
        index=listbox.curselection()[0]
        listbox.delete(index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No task selected.")
        
def load_items():
    tasks=pickle.load(open("tasks.txt", "rb"))
    listbox.delete(0, tkinter.END)
    for task in tasks:
        listbox.insert(tkinter.END, task)

def save_items():
    tasks=listbox.get(0, listbox.size())
    pickle.dump(tasks, open("tasks.txt", "wb"))
    
#-------------------------------------------------------------------

frame = tkinter.Frame(root)
frame.pack()
listbox=tkinter.Listbox(frame, height=8, width= 50)
listbox.pack(side=tkinter.LEFT)

scroll=tkinter.Scrollbar(frame)
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)
entry1=tkinter.Entry(root, width=50)
entry1.pack()

btn1=tkinter.Button(root, text= 'ADD item', width=48, command = add_item)
btn1.pack()

btn2=tkinter.Button(root, text= 'Delete item', width=48, command = delete_item)
btn2.pack()

btn3=tkinter.Button(root, text= 'Save items', width=48, command = save_items)
btn3.pack()

btn4=tkinter.Button(root, text= 'Load items', width=48, command = load_items)
btn4.pack()

root.mainloop()