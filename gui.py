from tkinter import *
import custom_button
root= Tk()
#root.iconbitmap('image/calculator.ico') #I have icon error. 
root.title('Calculator')
root.config(bg='white')
root.resizable(0,0)
# ==================== Functions =====================================
def on_key(number):
        screen.insert(END, number)

def calculate():
        ans = eval(screen.get())
        screen.delete(0, END)
        screen.insert(END, ans)

# =====================  Display ======================================

# create entry
screen= Entry(root, font=("Helvetica", 14), justify='right', width=27, bg='#736d6d',fg='white')

# place entry
screen.grid(row=0, column=0, columnspan=4, ipady=15)

# ========================== Keys ======================================

#1st row
button_bar1 = Button(root, text ="(", width=5, height=3, command=lambda:on_key('('))
button_bar1.grid(row=1, column=0)

button_bar2 = Button(root, text =")", width=5, height=3, command=lambda:on_key(')'))
button_bar2.grid(row=1, column=1)

button_module = Button(root, text ="%", width=5, height=3, command=lambda:on_key('%'))
button_module.grid(row=1, column=2)

clear_btn = Button(root, text ="AC", width=5, height=3, command=lambda:screen.delete(0, END))
clear_btn.grid(row=1, column=3)

#2nd row
button_7 = Button(root, text ="7", width=5, height=3, command=lambda:on_key('7'))
button_7.grid(row=2, column=0)

button_8 = Button(root, text ="8", width=5, height=3, command=lambda:on_key('8'))
button_8.grid(row=2, column=1)

button_9 = Button(root, text ="9", width=5, height=3, command=lambda:on_key('9'))
button_9.grid(row=2, column=2)

div_btn=Button(root, text ="÷", width=5, height=3, command=lambda:on_key('/'))
div_btn.grid(row=2, column=3)

#3rd row
button_4 = Button(root, text ="4", width=5, height=3, command=lambda:on_key('4'))
button_4.grid(row=3, column=0)

button_5 = Button(root, text ="5", width=5, height=3, command=lambda:on_key('5'))
button_5.grid(row=3, column=1)

button_6 = Button(root, text ="6", width=5, height=3, command=lambda:on_key('6'))
button_6.grid(row=3, column=2)

mul_btn=Button(root, text ="x", width=5, height=3, command=lambda:on_key('*'))
mul_btn.grid(row=3, column=3)

#4th row
button_1 = Button(root, text ="1", width=5, height=3, command=lambda:on_key('1'))
button_1.grid(row=4, column=0)

button_2 = Button(root, text ="2", width=5, height=3, command=lambda:on_key('2'))
button_2.grid(row=4, column=1)

button_3 = Button(root, text ="3", width=5, height=3, command=lambda:on_key('3'))
button_3.grid(row=4, column=2)

sub_btn=Button(root, text ="-", width=5, height=3, command=lambda:on_key('-'))
sub_btn.grid(row=4, column=3)

#5th row
button_0 = Button(root, text ="0", width=5, height=3, command=lambda:on_key('0'))
button_0.grid(row=5, column=0)

button_float = Button(root, text =".", width=5, height=3, command=lambda:on_key('.'))
button_float.grid(row=5, column=1)

calculate_btn = Button(root, text ="=", width=5, height=3, command=calculate)
calculate_btn.grid(row=5, column=2)

sub_btn=Button(root, text ="+", width=5, height=3, command=lambda:on_key('+'))
sub_btn.grid(row=5, column=3)

root.mainloop()