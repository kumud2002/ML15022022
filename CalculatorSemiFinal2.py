import tkinter as tkr
from lib2to3.pgen2.literals import evalString


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
    
    exp()
def exp():
    a=en1.get()
    b=en2.get() 
    if rb1.get()=='+':
            exp=a+b
    elif rb1.get()=='-':
            exp=a-b
    elif rb1.get()=='%':
            exp=a%b
    elif rb1.get()=='/':
        exp=a/b
    else:
            exp=a*b
    tkr.Label(app,text=exp,font=(80)).pack()
##    exp=eval(a,rb1.get(),b)
    print('Calculation: ',exp)
    ##print('+'/'-'/'%'/'*')
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

##def final():
##    print(final)
##    final=en1en2
        

######## RESULT BUTTON




tkr.Label(app,text='**RESULT**',font=(100)).pack()




app.mainloop()
