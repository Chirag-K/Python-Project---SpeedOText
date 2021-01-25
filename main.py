import tkinter as tk
from tkinter import *
import random
from time import time


def get_para():
    dict = {1: 'I had never seen a house on fire before, so, one evening when I heard fire engines with loud alarm '
               'bells rushing past my house. I quickly ran out and, a few streets away, joined a large crowd of people.'
               'We could see the fire only from a distance because the police would not allow any one near the building'
               ' on fire.',
            2: 'What a terrible scene I saw that day! Huge flames of fire were coming out of each floor, and black and'
               ' thick smoke spread all around. Four fire engines were engaged and the firemen in their uniform were'
               ' playing the hose on various parts of the building. Then the tall ladders of the fire engine  were'
               ' stretched upwards. Some firemen climbed up with hoses in their hands. The continuous flooding brought'
               ' the fire under control but the building was completely destroyed.',
            3: 'I am now an old coin. I have been in circulation many, many years. I have become dulled and worn  and'
               ' the lettering on my back almost rubbed out. But I can still remember my early youth.'
               ' At that time, I was in Government Treasury.'
               'I was shining silver that time. I was very proud of my smart appearance.',
            4: 'My active life began when I was paid over the counter of a bank. The shopkeepers looked pleased when'
               ' they had me in their hands. I soon found we were a mixed company. But, I soon found a number of rupees'
               ' of other metals of my own rank, but none so new and bright as I was.'}
    ran = random.choice(list(dict.values()))
    ran = ''.join(ran)
    return ran


class Appk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('SpeedOText')
        self.geometry("900x600+350+120")
        self.configure(background='black')
        self.resizable(0, 0)

        self.buttonCycle = False

        self.label = tk.Label(self, text='Typing  Speed  Test', bg='black', fg='yellow', font=('Bold', 35)).place(x=230,
                                                                                                                  y=30)

        self.text_entry = tk.Text(self, height=3, width=76, bg='black', fg='lightblue', bd=4, font=('', 14),
                                  insertwidth=2,
                                  wrap=WORD, padx=4,
                                  pady=4, relief=RIDGE, insertbackground='lightblue', state=DISABLED)
        self.text_entry.place(x=25, y=300)

        self.txt = get_para()
        self.text = tk.Message(self, width=873, bg='black', fg='white', bd=0, font=('', 14), padx=4, text=self.txt,
                               relief=RAISED, pady=4)
        self.text.place(x=10, y=150)

        self.label_timer = Label(self, text='', height=1, width=3, bg='black', fg='brown', font=('Bold', 50))
        self.label_timer.place(x=402, y=415)
        self.count = 0
        self.ready = Button(self, height=2, width=11, text='START', bg='lightblue', font=('Bold', 14),
                            command=lambda: self.updateButton())
        self.ready.place(x=400, y=520)

        self.submit = Button(self, height=2, width=10, text='SUBMIT', bg='lightyellow', command=self.result)
        self.submit.place(x=795, y=400)
        self.accuracy = 0
        self.min = 0


    def run_timer(self):
        self.delta = int(time() - self.old_time)
        time_str = '{:02}:{:02}'.format(*divmod(self.delta, 60))
        self.display.config(text=time_str)
        self.display.after(1000, self.run_timer)

    def updateButton(self):
        if self.buttonCycle:
            self.buttonCycle = False
            self.destroy()
            main()
        elif not self.buttonCycle:
            self.buttonCycle = True
            self.ready.configure(text='RESET')
            self.countdown(3)

    def countdown(self, count=None):
        if count is not None:
            self.count = count
        if self.count == 0:
            self.label_timer.configure(text="GO!")
            self.count -= 1
            self.after(1000, self.countdown)
        elif self.count < 0:
            self.label_timer.destroy()
            self.text_entry.configure(state=NORMAL)
            self.display = tk.Label(self, text='00:00', width=5, height=2, bg='black', fg='brown', font=('Bold', 30))
            self.display.place(x=402, y=415)
            self.old_time = time()
            self.run_timer()
        else:
            self.label_timer.configure(text='%d' % self.count)
            self.count -= 1
            self.after(1000, self.countdown)

    def result(self):
        self.sec = self.delta
        self.display.destroy()
        self.text_entry.config(state=DISABLED)
        _input = self.text_entry.get("1.0", 'end-1c')
        self.user_input = _input.split()
        orignal_input = self.txt.split()
        check = 0
        for i in range(len(self.user_input)):
            if self.user_input[i] == orignal_input[i]:
                check += 1
        self.accuracy = int((check / len(self.user_input)) * 100)

        self.acc_text = "Accuracy : " + str(self.accuracy) + "%"
        self.accuracy_label = Label(self, text=self.acc_text, height=4, width=13, bg='black', fg='brown',
                                    font=('Bold', 16))
        self.accuracy_label.place(x=40, y=390)

        if self.sec > 60:
            while (self.sec > 60) :
                print(self.sec)
                self.sec = self.sec - 60
                self.min = self.min + 1

        self.tyme = "Time : " + str(self.min) + " min " + str(self.sec) + " sec"
        self.tym_label = Label(self, text=self.tyme, height=4, width=15, bg='black', fg='brown',
                                    font=('Bold', 16))
        self.tym_label.place(x=40, y=450)

        if self.delta > 0:
            self.wpm = int((len(self.user_input)/self.delta)*60)
        else:
            self.wpm = 0
        self.wpm = "WPM : " + str(self.wpm)
        self.wpm_label = Label(self, text=self.wpm, height=3, width=15, bg='black', fg='brown',
                                    font=('Bold', 16))
        self.wpm_label.place(x=270, y=400)

def main():
    if __name__ == "__main__":
        app = Appk()
        app.mainloop()


main()
