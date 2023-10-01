from tkinter import *

class AlarmClock:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("430x450")
        self.root.resizable(width=False, height=False)
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.cn = Canvas(self.root, bg='white', height=30, width=30)
        self.canvas = Canvas(self.root, bg='white', height=self.screen_height, width=self.screen_width)
        self.root.title('Будильник')

        self.hour = Label(self.root, text='Введите час',
                          fg='#000000', bd=2, font='Verdana', width=15, height=1)
        self.minutes = Label(self.root, text='Введите минуту',
                             fg='#000000', bd=2, font='Verdana', width=15, height=1)
        self.text_hour = Entry(self.root, bg='#CECECE', font='Cambria', justify='center', width=5)
        self.text_minutes = Entry(self.root, bg='#CECECE', font='Cambria', justify='center', width=5)
        self.hour.place(x=45, y=100)
        self.minutes.place(x=45, y=140)
        self.text_hour.place(x=260, y=100)
        self.text_minutes.place(x=260, y=140)

        self.canvas.pack()
        self.root.mainloop()

alarm_clock = AlarmClock()