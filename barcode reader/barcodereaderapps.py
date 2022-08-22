from barcodereaderwebcam import webcam_barcode
from barcodeconverter import convert_barcode
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Your Pantry List")

def search_pantry():
	search_item = entry_item.get()
	for i in range(listbox_tasks.size()):
		if listbox_tasks.get(i).lower().find(search_item.lower()) != -1:
			listbox_tasks.itemconfig(i, {'bg':'yellow'})

def add_items():
	webcam_barcode()
	try:
		for barcode in webcam_barcode.barcodes:
			listbox_tasks.insert(tkinter.END, convert_barcode(barcode))
			for word in convert_barcode(barcode).split():
				for i in range(listbox_tasks.size() - 1):
					if listbox_tasks.get(i).find(word) != -1:
						listbox_tasks.itemconfig(i, {'bg':'red'})
						tkinter.messagebox.showwarning(title="Warning", message="In red are products in pantry")
					else:
						listbox_tasks.itemconfig(i, {'bg':'white'})
	except:
		pass
	# for i in range(listbox_tasks.size()):
	# 	if listbox_tasks.get(i).find(search_item) != -1:
	# 		listbox_tasks.itemconfig(i, {'bg':'red'})


def add_items_barcode():
	barcode_num = entry_item.get()
	if barcode_num != "":
		listbox_tasks.insert(tkinter.END, convert_barcode(barcode_num))
		entry_item.delete(0, tkinter.END)
		for word in convert_barcode(barcode_num).split():
			for i in range(listbox_tasks.size() - 1):
				if listbox_tasks.get(i).find(word) != -1:
					listbox_tasks.itemconfig(i, {'bg':'red'})
					tkinter.messagebox.showwarning(title="Warning", message="In red are products in pantry")
				else:
					listbox_tasks.itemconfig(i, {'bg':'white'})
	else:
		tkinter.messagebox.showwarning(title="Warning", message="Must enter Barcode")

def edit_item():
	change_item = entry_item.get()
	try:
		item_index = listbox_tasks.curselection()[0]
		listbox_tasks.delete(item_index)
		listbox_tasks.insert(item_index, change_item)
		entry_item.delete(0, tkinter.END)
		for word in change_item.split():
			for i in range(listbox_tasks.size() - 1):
				if listbox_tasks.get(i).find(word) != -1:
					listbox_tasks.itemconfig(i, {'bg':'red'})
					tkinter.messagebox.showwarning(title="Warning", message="In red are products in pantry")
				else:
					listbox_tasks.itemconfig(i, {'bg':'white'})
	except:
		tkinter.messagebox.showwarning(title="Warning", message="must select task")

def delete_item():
	try:
		item_index = listbox_tasks.curselection()[0]
		listbox_tasks.delete(item_index)
	except:
		tkinter.messagebox.showwarning(title="Warning", message="must select task")

# maybe load on startup
def load_pantry():
	try:
		tasks = pickle.load(open("tasks.dat", "rb"))
		listbox_tasks.delete(0, tkinter.END)
		for task in tasks:
			listbox_tasks.insert(tkinter.END, task)
	except:
		tkinter.messagebox.showwarning(title="Warning", message="no tasks.dat")

def save_pantry():
	tasks = listbox_tasks.get(0, listbox_tasks.size())
	pickle.dump(tasks, open("tasks.dat", "wb"))

#creating gui
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=30, width=150)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# try making search bar
entry_item = tkinter.Entry(root, width=120)
entry_item.pack()

button_search_pantry = tkinter.Button(root, text="Search", width=120, command=search_pantry)
button_search_pantry.pack()

button_add_items = tkinter.Button(root, text="Add Items (Scan)", width=120, command=add_items)
button_add_items.pack()

button_add_items_barcode = tkinter.Button(root, text="Add Items (Enter Barcode)", width=120, command=add_items_barcode)
button_add_items_barcode.pack()

button_edit_items = tkinter.Button(root, text="Edit Item", width=120, command=edit_item)
button_edit_items.pack()

button_delete_task = tkinter.Button(root, text="Delete Item", width=120, command=delete_item)
button_delete_task.pack()

button_load_pantry = tkinter.Button(root, text="Load Pantry", width=120, command=load_pantry)
button_load_pantry.pack()

button_save_pantry = tkinter.Button(root, text="Save Pantry", width=120, command=save_pantry)
button_save_pantry.pack()




root.mainloop()