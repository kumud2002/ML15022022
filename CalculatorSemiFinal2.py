import tkinter as tkr

app=tkr.Tk(__name__)
app.title('CALCULATOR')
app.geometry('600x800')

######## ADDING LABLES

tkr.Label(app,text='NUMBER 1').place(x=50,y=20)
tkr.Label(app,text='NUMBER 2').place(x=50,y=50)

######## FUNCTIONS

def show():
    print('NUMBER 1: ',en1.get())
    print('NUMBER 2: ',en2.get())
    print('radiobutton values:',rb1.get())    
    cal()
def cal(): 
    c=str(en1.get())
    d=str(en2.get())
    exp=eval(c+rb1.get()+d)
    print('Calculation: ',exp)
    tkr.Label(app,text=exp,font=(80)).pack()


######## ENTRY BOXES

en1=tkr.IntVar(app)
en2=tkr.IntVar(app)
tkr.Entry(app,textvariable=en1,font=(30),width=15).pack()
tkr.Entry(app,textvariable=en2,font=(30),width=15).pack()

######## RADIO BUTTON

rb1 =tkr.Variable(app,'0')
rb_values = {'+':'+','-':'-','%':'%','/':'/','*':'*'}
for k,v in rb_values.items():
    tkr.Radiobutton(app,text=k,variable=rb1,value=v).pack()
    
######## BUTTON

tkr.Button(app,text='CALCULATE',command=show).pack()

######## CALCULATION



######## RESULT BUTTON


tkr.Label(app,text='**RESULT**',font=(100)).pack()
app.mainloop()
