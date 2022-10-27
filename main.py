import tkinter

window = tkinter.Tk()
window.title('Mile to KM converter')
window.minsize(width=230, height=120)
window.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)


def clicked():
    km = int(input.get()) * 1.6
    lable3.config(text=km)


button = tkinter.Button(text='Calculate', command=clicked)
button.grid(column=1, row=2)

lable1 = tkinter.Label(text='Miles')
lable1.grid(column=2, row=0)

lable2 = tkinter.Label(text='is equal to')
lable2.grid(column=0, row=1)

lable3 = tkinter.Label(text='0')
lable3.grid(column=1, row=1)

lable4 = tkinter.Label(text='KM')
lable4.grid(column=2, row=1)

window.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
