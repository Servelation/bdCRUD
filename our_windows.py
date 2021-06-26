from tkinter import *
import sqlite3


class AuthorWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title("Добро пожаловать!")
        self.window.geometry("800x600+1800+200")
        self.l_vhod = Label(self.window, text="Вход", font=("Comic Sans MS", 40))
        self.l_vhod.pack()
        self.l_login = Label(self.window, text="Логин", font=("Comic Sans MS", 23))
        self.l_login.pack()
        self.e_login = Entry(self.window, font=("Comic Sans MS", 23))
        self.e_login.pack()
        self.l_password = Label(self.window, text="Пароль", font=("Comic Sans MS", 23))
        self.l_password.pack()
        self.e_password = Entry(self.window, font=("Comic Sans MS", 23))
        self.e_password.pack()
        self.button = Button(self.window, font=("Comic Sans MS", 23), text="Войти", command=self.button_click)
        self.button.pack()
        self.l_label = Label(self.window, text="", font=("Comic Sans MS", 23))
        self.l_label.pack()
    def button_click(self):
        if self.e_login.get()=='admin' :
            self.vhod()
        else:
            self.wrong()
    def vhod(self):
        self.window.destroy()
    def wrong(self):
        self.l_label.config(text="Неправильно!")
    def mainloop(self):
        self.window.mainloop()

class MainWindow:
    def __init__(self,cursor):
        self.cursor = cursor
        self.window = Tk()
        self.window.title("Автосервис")
        self.window.geometry("800x600+1800+200")
        self.menu = Menu(self.window)
        self.clients = Menu(self.menu)
        self.clients.add_command(label = 'Показать', command = self.show_clients)
        self.menu.add_cascade(label = 'Клиенты', menu=self.clients)
        self.window.config(menu=self.menu)
        self.frame = Frame(self.window)
        self.frame.pack()
    def mainloop(self):
        self.window.mainloop()

    def show_clients(self):
        self.frame.destroy()
        self.frame = Frame(self.window)
        self.cursor.execute('SELECT * FROM Client')
        clients = self.cursor.fetchall()
        for i,cl in enumerate(clients):
            for j in range(len(cl)):
                l = Label(self.frame, text=cl[j])
                l.grid(column=j, row=i)
        self.frame.pack()