from tkinter import *
import random
import time

# Функция для рандомного выбора картинок
def drop():
    x = random.choice(['p.png', 's.png', 'st.png'])
    return x

# Функция для подставоения картинок
def img(event):
    global b1, b2
    for i in range(19):
        b1 = PhotoImage(file=(drop()))
        b2 = PhotoImage(file=(drop()))
        but1['image'] = b1
        but2['image'] = b2
        root.update()
        time.sleep(0.11)

#Создаем рабочее окно игры

root = Tk()

# Создали поле

root.geometry('400x200')
root.title('Камень, ножницы, бумага. Раз, два, три ...')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icon.png'))
font = PhotoImage(file='surf.png')
Label(root, image=font).pack()

# Создали кнопки

but1 = Label(root)
but1.place(relx=0.3, rely=0.5, anchor=CENTER)

but2 = Label(root)
but2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.bind('1', img)
img('event')

root.mainloop()



def main():
    pass


if __name__ == '__main__':
    main()

