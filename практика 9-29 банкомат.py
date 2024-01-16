from tkinter import *
from tkinter import messagebox
window = Tk()
window.attributes('-fullscreen', True)
window.title('интерфейс банкомата НеобманБАНК')


#Важные переменные
adminlogin = 'ADMIN'
pin_code = '0000'
balance = '0'

def false_pin():                                                          #СООБЩЕНИЕ "НЕВЕРНЫЙ ПИН"
    global n
    if n > 0:
        messagebox.showinfo('Внимание!','ПИН-код не верный')
        pin.delete(0,END)
    else:
        vvbut.destroy()
        pin.destroy()
        vvpin.destroy()
        nachalo()
        n = n+3

def nachalo():                                                                           #НАЧАЛЬНОЕ ОКНО
    lbl1 = Label(window, text='НеобманБАНК', font=('Arial Bold', 40))
    lbl1.place(x=40)
    lbl2 = Label(window, text='Приём платежей', font=('Arial Bold', 40))
    lbl2.place(x=1080)
    lbl3 = Label(window, text='Номер терминала \n 00001', font=('Arial Bold', 20))
    lbl3.place(x=40, y=750)
    lbl4 = Label(window, text='Телефон тех. поддержки \n не задан', font=('Arial Bold', 20))
    lbl4.place(x=650, y=750)
    lbl5 = Label(window, text='Адрес терминала \n не задан', font=('Arial Bold', 20))
    lbl5.place(x=1250, y=750)
    global nachbutt
    nachbutt = Button(window, text='Начать --->', font=('Arial Bold', 40), command= pincode)
    nachbutt.place(relx=0.5, rely=0.5,anchor=CENTER)
    admbut = Button(window, text='Для администратора', font=('Arial Bold', 10), command= admin_menu)
    admbut.place(x=745, y=820)

def admin_menu():
    nachbutt.destroy()

def pincode():                                                                         #ВВОД ПИН-КОДА
    def press_key(event):
        if event.char =='\r':   #\r - char клавиши энтер узнается через repr() в консоли
            dialogwindow()

    window.bind('<Key>', press_key)
    
    def validate(new_value):
        return new_value == '' or new_value.isnumeric()
    
    vcmd = (window.register(validate), '%P')

    nachbutt.destroy()
    global vvpin
    vvpin = Label(window, text='Введите PIN-код', font=('Arial Bold', 40))
    vvpin.place(x=570, y=250)
    global pin
    pin= Entry(window, validate='key', validatecommand=vcmd, show='*', justify='center',font=('Arial Bold', 40))
    pin.place(relx=0.5, rely=0.5,anchor=CENTER)
    global vvbut
    vvbut = Button(window, text='Ввод \n (ENTER)', font=('Arial Bold', 16), command=dialogwindow)
    vvbut.place(x=1070, y=400)

n = 3

def dialogwindow():                                                              #ДИАЛОГОВОЕ ОКНО БАЛАНС ВВОД ВЫВОД
    p = pin.get()
    global n
    
    if p == pin_code:
        vvbut.destroy()
        pin.destroy()
        vvpin.destroy()
        operbut1 = Button(window, text='Узнать баланс карты', font=('Arial Bold', 40))
        operbut2 = Button(window, text='Ввод средств', font=('Arial Bold', 40))
        operbut3 = Button(window, text='Вывод средств', font=('Arial Bold', 40))
        operbut1.place(x=500, y=270)
        operbut2.place(relx=0.5, rely=0.5,anchor=CENTER)
        operbut3.place(x=560, y=490)
    else:
        n = n-1
        false_pin()




nachalo()

window.mainloop()
