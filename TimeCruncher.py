from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Time Calkulator")
root.iconbitmap(
    'C:/Users/aceas/Programering/Tkinter-youtube/beginner/logo-black.ico')
root.geometry("400x400")


'''                  LABELS                    '''
labelEmty0 = Label(root, text="          ", font=('arial', 4))
labelEmty0.grid(row=0, column=0)
labelEmty1 = Label(root, text="          ", font=('arial', 10))
labelEmty1.grid(row=2, column=0)
topLabel = Label(root, text="Time Kontrolør", font=('arial', 20, 'bold'))
topLabel.grid(row=1, column=1, columnspan=3)
labeltimer = Label(root, text="Timer", font=('arial', 10))
labeltimer.grid(row=2, column=1, pady=5, padx=5)
labelminutter = Label(root, text="Minutter", font=('arial', 10))
labelminutter.grid(row=2, column=2, pady=5, padx=5)
eksisterende = Label(root, text="Totale Timer", font=('arial', 10))
eksisterende.grid(row=2, column=3, pady=5, padx=5)
totalMinutt = Label(root, text="Minutt", font=('arial', 10))
totalMinutt.grid(row=2, column=4, pady=5, padx=5)

'''                  ENTRYS                    '''
timer = Entry(width=10)
timer.grid(row=3, column=1, pady=5, padx=5)
timer.insert(0, 0)
minutt = Entry(width=10)
minutt.grid(row=3, column=2, pady=5, padx=5)
minutt.insert(0, 0)
exist = Entry(width=10)
exist.grid(row=3, column=3, pady=5, padx=5)
exist.insert(0, 0)
totleMin = Entry(width=10)
totleMin.grid(row=3, column=4, pady=5, padx=5)
totleMin.insert(0, 0)


def CalcTime():
    t_imer = timer.get()
    m_minut = minutt.get()
    e_xist = exist.get()
    m_minut1 = totleMin.get()
    timer.delete(0, END)
    minutt.delete(0, END)
    exist.delete(0, END)
    totleMin.delete(0, END)
    timer.insert(0, 0)
    minutt.insert(0, 0)

    total = int(t_imer) + int(e_xist)
    m_minut = int(m_minut)
    m_minut1 = int(m_minut1)
    m_minut1 += m_minut
    if (m_minut1 >= 60):
        total += 1
        m_minut1 -= 60
        totleMin.insert(0, m_minut1)
    else:
        totleMin.insert(0, m_minut1)
    exist.insert(0, total)


def clear():
    timer.delete(0, END)
    minutt.delete(0, END)
    exist.delete(0, END)
    totleMin.delete(0, END)

    timer.insert(0, 0)
    minutt.insert(0, 0)
    exist.insert(0, 0)
    totleMin.insert(0, 0)


Button(root, text="Calculate", command=CalcTime).grid(row=4, column=1)

Button(root, text="Clear", command=clear).grid(row=4, column=2)


root.mainloop()
