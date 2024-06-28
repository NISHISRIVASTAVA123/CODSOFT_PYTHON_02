import tkinter as tk
def button_click(number):
    current_text=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,current_text+str(number))
def button_clear():
    entry.delete(0,tk.END)
def button_operator(operator):
    current = entry.get()
    if current and current[-1] not in '+-*/':
        entry.insert(tk.END, operator)
    elif current and current[-1] in '+-*/':
        entry.delete(len(current) - 1, tk.END)
        entry.insert(tk.END, operator)
def button_equal():
    expression=entry.get()
    result=eval(expression)
    entry.delete(0,tk.END)
    entry.insert(0,str(result))
root=tk.Tk()
root.title("Simple Calculator")
root.geometry('500x460')
root.resizable(False,False)
root.configure(background="pink")

entry=tk.Entry(root,text='',bg='black',fg='white')
entry.grid(row=0,column=0,columnspan=5,pady=40,padx=25)
entry.config(font=("Helvetica",30,'bold'))

button9=tk.Button(root,text='9',bg='white',fg='black',width=5,height=2,command=lambda:button_click(9))
button9.grid(row=1,column=0,padx=5, pady=5, sticky='nsew')
button9.config(font=('Helvetica',14))


button8=tk.Button(root,text='8',bg='white',fg='black',width=5,height=2,command=lambda:button_click(8))
button8.grid(row=1,column=1,padx=5, pady=5, sticky='nsew')
button8.config(font=('Helvetica',14))


button7=tk.Button(root,text='7',bg='white',fg='black',width=5,height=2,command=lambda:button_click(7))
button7.grid(row=1,column=2,padx=5, pady=5, sticky='nsew')
button7.config(font=('Helvetica',14))


button_add=tk.Button(root,text='+',bg='white',fg='black',width=5,height=2,command=lambda:button_operator('+'))
button_add.grid(row=1,column=3,padx=5, pady=5, sticky='nsew')
button_add.config(font=('Helvetica',14))


button6=tk.Button(root,text='6',bg='white',fg='black',width=5,height=2,command=lambda:button_click(6))
button6.grid(row=2,column=0,padx=5, pady=5, sticky='nsew')
button6.config(font=('Helvetica',14))


button5=tk.Button(root,text='5',bg='white',fg='black',width=5,height=2,command=lambda:button_click(5))
button5.grid(row=2,column=1,padx=5, pady=5, sticky='nsew')
button5.config(font=('Helvetica',14))


button4=tk.Button(root,text='4',bg='white',fg='black',width=5,height=2,command=lambda:button_click(4))
button4.grid(row=2,column=2,padx=5, pady=5, sticky='nsew')
button4.config(font=('Helvetica',14))


button_subtract=tk.Button(root,text='-',bg='white',fg='black',width=5,height=2,command=lambda:button_operator('-'))
button_subtract.grid(row=2,column=3,padx=5, pady=5, sticky='nsew')
button_subtract.config(font=('Helvetica',14))


button3=tk.Button(root,text='3',bg='white',fg='black',width=5,height=2,command=lambda:button_click(3))
button3.grid(row=3,column=0,padx=5, pady=5, sticky='nsew')
button3.config(font=('Helvetica',14))


button2=tk.Button(root,text='2',bg='white',fg='black',width=5,height=2,command=lambda:button_click(2))
button2.grid(row=3,column=1,padx=5, pady=5, sticky='nsew')
button2.config(font=('Helvetica',14))


button1=tk.Button(root,text='1',bg='white',fg='black',width=5,height=2,command=lambda:button_click(1))
button1.grid(row=3,column=2,padx=5, pady=5, sticky='nsew')
button1.config(font=('Helvetica',14))


button_multiply=tk.Button(root,text='*',bg='white',fg='black',width=5,height=2,command=lambda:button_operator('*'))
button_multiply.grid(row=3,column=3,padx=5, pady=5, sticky='nsew')
button_multiply.config(font=('Helvetica',14))


button_clr=tk.Button(root,text='AC',bg='white',fg='black',width=5,height=2,command=lambda:button_clear())
button_clr.grid(row=4,column=0,padx=5, pady=5, sticky='nsew')
button_clr.config(font=('Helvetica',14))


button0=tk.Button(root,text='0',bg='white',fg='black',width=5,height=2,command=lambda:button_click(0))
button0.grid(row=4,column=1,padx=5, pady=5, sticky='nsew')
button0.config(font=('Helvetica',14))


button_result=tk.Button(root,text='=',bg='white',fg='black',width=5,height=2,command=lambda:button_equal())
button_result.grid(row=4,column=2,padx=5, pady=5, sticky='nsew')
button_result.config(font=('Helvetica',14))


button_divide=tk.Button(root,text='/',bg='white',fg='black',width=5,height=2,command=lambda:button_operator('/'))
button_divide.grid(row=4,column=3,padx=5, pady=5, sticky='nsew')
button_divide.config(font=('Helvetica',14))


root.mainloop()












