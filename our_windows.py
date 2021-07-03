from tkinter import *
import sqlite3


class AbstractWindow:
    def __init__(self, title):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry("800x600+300+200")

    def mainloop(self):
        self.window.mainloop()


class AuthorWindow(AbstractWindow):
    def __init__(self):
        super().__init__('Добро пожаловать!')
        self.access = False
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
        if self.e_login.get() == 'admin':
            self.vhod()
        else:
            self.wrong()

    def vhod(self):
        self.access = True
        self.window.destroy()

    def wrong(self):
        self.l_label.config(text="Неправильно!")


class MainWindow(AbstractWindow):
    def __init__(self, connect, cursor):
        super().__init__('Автосервис')
        self.connect = connect
        self.cursor = cursor
        self.menu = Menu(self.window)
        self.clients = Menu(self.menu)
        self.clients.add_command(label='Показать', command=self.show_clients)
        self.clients.add_command(label='Добавить', command=self.add_client)
        self.menu.add_cascade(label='Клиенты', menu=self.clients)
        self.window.config(menu=self.menu)
        self.frame = Frame(self.window)
        self.frame.pack()

    def show_clients(self):
        self.frame.destroy()
        self.frame = Frame(self.window)
        self.cursor.execute('SELECT * FROM Client')
        clients = self.cursor.fetchall()
        for i, cl in enumerate(clients):
            for j in range(len(cl)):
                l = Label(self.frame, text=cl[j])
                l.grid(column=j, row=i)
        self.frame.pack()

    def add_client(self):
        adding_window = WindowForAddingClient(self.cursor)
        adding_window.mainloop()
        self.connect.commit()


class WindowForAddingClient(AbstractWindow):
    def __init__(self, cursor):
        super().__init__('добавьте клиента')
        self.cursor = cursor
        self.l_surname = Label(self.window, text="Фамилия", font=("Comic Sans MS", 23))
        self.l_surname.pack()
        self.e_surname = Entry(self.window, font=("Comic Sans MS", 23))
        self.e_surname.pack()
        self.l_name = Label(self.window, text="Имя", font=("Comic Sans MS", 23))
        self.l_name.pack()
        self.e_name = Entry(self.window, font=("Comic Sans MS", 23))
        self.e_name.pack()
        self.l_phone = Label(self.window, text="Телефон", font=("Comic Sans MS", 23))
        self.l_phone.pack()
        self.e_phone = Entry(self.window, font=("Comic Sans MS", 23))
        self.e_phone.pack()
        self.b_button = Button(self.window, text='Добавить', font=("Comic Sans MS", 23), command=self.add_client_click)
        self.b_button.pack()

    def add_client_click(self):
        surname = self.e_surname.get()
        name = self.e_name.get()
        phone = self.e_phone.get()
        self.cursor.execute(f'INSERT INTO Client VALUES(null, \'{surname}\', \'{name}\', \'{phone}\')')
        self.window.destroy()
