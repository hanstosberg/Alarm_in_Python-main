from tkinter import *
import time
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
        self.lbl = Label(self.root, text=f'Текущее время: {str(time.strftime("%H:%M:%S", time.localtime()))[:5]}',
                         bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=80, height=2)
        self.hour = Label(self.root, text='Введите час',
                          fg='#000000', bd=2, font='Verdana', width=15, height=1)

        self.hour = Label(self.root, text='Введите час',
                          fg='#000000', bd=2, font='Verdana', width=15, height=1)
        self.minutes = Label(self.root, text='Введите минуту',
                             fg='#000000', bd=2, font='Verdana', width=15, height=1)
        self.text_hour = Entry(self.root, bg='#CECECE', font='Cambria', justify='center', width=5)
        self.text_minutes = Entry(self.root, bg='#CECECE', font='Cambria', justify='center', width=5)

        self.btn = Button(self.root, text=" Установить будильник ", width=35, height=2, bg='#6EA6C1',
                          fg='#000000', font=('Verdana', 13, 'bold'))
        self.miusik = Label(self.root, text=f'Выберете мелодию:',
                            bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=20, height=2)
        self.variable = StringVar(self.root)

        self.shr = OptionMenu(self.root, self.variable, 'Мелодия 1', 'Мелодия 2', 'Мелодия 3', 'Мелодия 4', 'Мелодия 5')
        self.lbl.pack()
        self.hour.place(x=45, y=100)
        self.minutes.place(x=45, y=140)
        self.text_hour.place(x=260, y=100)
        self.text_minutes.place(x=260, y=140)
        self.miusik.place(x=10, y=190)
        self.btn.place(x=0, y=270)
        self.shr.place(x=280, y=205)
        self.canvas.pack()
        self.root.mainloop()

alarm_clock = AlarmClock()