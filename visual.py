from tkinter import *
from tkinter import messagebox
from calculations import main, artificial_result


def click():
    imp = int(Input.get())
    text = artificial_result(control_value, imp)
    messagebox.showinfo(title='Результат', message=f'При таком времени подготовки, вероятнее всего, Вы получите {text}')


control_value = main()
root = Tk()
ar = PhotoImage(file="arrow.gif")

root['bg'] = '#000000'
root.title('Предсказатель')
root.geometry('500x500')
root.resizable(width=False, height=False)

canvas = Canvas(root, width=500, height=500)
canvas.pack()

frame = Frame(root, bg='#010101')
frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)
title = Label(frame, text='Введите сколько часов Вы готовились к зачету', bg='black', bd='5',
              relief='groove', font="Arial 13")
title.place(relx=0.15, rely=0.1)
arrow = Label(frame, image=ar)
arrow.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.2)
Input = Entry(frame, fg='#010101', bg='white', font="Arial 25", justify='center')
Input.place(relx=0.195, rely=0.5)
butt = Button(frame, text='Ваш результат', font="Arial 30", justify='center', command=click)
butt.place(relx=0.25, rely=0.7)

root.mainloop()
