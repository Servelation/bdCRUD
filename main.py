import sqlite3
from tkinter import *
from our_windows import *


con = sqlite3.connect(r'C:\Program Files\SQLiteStudio\Autoservice')
cursor = con.cursor()
authorise_window = AuthorWindow()
authorise_window.mainloop()

main_window = MainWindow(cursor)
main_window.mainloop()

# cursor = con.cursor()
# cursor.execute('SELECT * FROM Client')
# for client in cursor.fetchall():
#     print(client)