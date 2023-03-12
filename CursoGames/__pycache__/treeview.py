
from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.title("ejemplo de Treeview")
ventana.geometry("400x300")
ventana['bg']='#fb0'

tv = ttk.Treeview(ventana)

item1 = tv.insert('',END ,text="Dias",open=1)
tv.insert(item1,END ,text='lunes')
tv.insert(item1,END ,text='martes')
tv.insert(item1,END ,text='miercoles')
tv.insert(item1,END ,text='jueves')

item2 = tv.insert('',END ,text="Colores")
tv.insert(item2,END ,text='red')
tv.insert(item2,END ,text='blue')
tv.insert(item2,END ,text='green')

item3 = tv.insert('',END ,text="Dias",open=1)
tv.insert(item3,END ,text='lunes')

tv.item(item1)
#print(tv.item(item1))
#print(tv.get_children())

#tv.delete(item3)


'''
for x in tv.get_children():
    print(x)
    print(tv.get_children(x))
'''


tv.pack()



ventana.mainloop()
