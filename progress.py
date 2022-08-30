
from tkinter import *
from datetime import datetime
from tkinter.ttk import Progressbar, Style
from threading import Thread
from time import sleep




#Progress Bar Length
PLEN = 250
BACKGROUND ='#3299a8'
#microsecond constants
MICROSECONDS = 1000000.0
MICROMINUTES = MICROSECONDS * 60
MICROHOURS = MICROMINUTES * 60
MICRODAY  = MICROHOURS * 24 
#Month calculated in function 
now = datetime.now()
if((now.year % 400 == 0) or  
     (now.year % 100 != 0) and  
     (now.year % 4 == 0)):   
     LEAPYEAR = 1
else:
    LEAPYEAR =0 
MICROYEAR = MICRODAY * (365+LEAPYEAR)

bits =[]
for i in range(32):
    bits.append("\u25A0")


     
            
app = Tk()
app_style = Style()
app_style.theme_use('alt')
app_style.configure("mine.Horizontal.TProgressbar", troughcolor =BACKGROUND, 
                        background='lightblue', thickness=5)
app.config(background='#3299a8')
app.title('Progress Bar')
app.geometry("1000x500")
canvas = Canvas(app)


def month_days(d,year):
    match d:
        case 1:
            return 31
        case 2:
            #check for leap year
            if (year %400 or (year%100!=0 and year%4==0)):
                return 29
            return 28
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 30
        case 12:
            return 31

def  Create_time_labels():
    labels = [
    Label(app,text="Second",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Minute",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Hour",background=BACKGROUND, anchor='e',width=6,justify='right'),
    Label(app,text="Day",background=BACKGROUND, anchor='e',width=6,justify='right'),
    Label(app,text="Month",background=BACKGROUND, anchor='e', width=6,justify='right'),
    Label(app,text="Year",background=BACKGROUND, anchor='e', width=6,justify='right')
    ]
    for i in range(6):
        labels[i].grid(row=i+1,column=0)
    return labels
    
def Create_time_count_labels():
    column= 1
    labels =[]
    for i in range(6):
        labels.append(Label(app,text=i,background=BACKGROUND,relief='ridge',anchor='w', width=13,justify='right'))
        labels[i].grid(row=i+1,column=column)       
    return labels

def Create_progress_bars():
    column= 2
    pbars =[]
    for i in range(6):
        pbars.append(Progressbar(app, orient=HORIZONTAL,
                style="mine.Horizontal.TProgressbar",
                length=PLEN, mode="determinate"))
        pbars[i].grid(row=i+1,column=column)       
    return pbars

def Create_percent_labels():
    column= 3
    labels =[]
    for i in range(6):
        labels.append(Label(app,text=i,background=BACKGROUND))
        labels[i].grid(row=i+1,column=column)       
    return labels   

def Seconds():
    row = 0
    now = datetime.now()
    time_display.config(text=now)
    s_micro = now.second * MICROSECONDS + now.microsecond
    m_micro = now.minute * MICROMINUTES + s_micro
    h_micro = now.hour * MICROHOURS + m_micro
    d_micro = now.day * MICRODAY + h_micro
    

    t_percent =   (now.microsecond /MICROSECONDS) 
    label_time_count[row].config(text='%10.8f' %( now.second +t_percent))
    t_percent *= 100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
# Minutes():
    row +=1
    t_percent =   (s_micro/MICROMINUTES) 
    label_time_count[row].config(text='{:10.8f}'.format( now.minute +t_percent))
    t_percent *=100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    

# Hours():
    row +=1
    t_percent =   (m_micro /MICROHOURS) 
    label_time_count[row].config(text='%10.8f' %( now.hour +t_percent%1))
    t_percent *=100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
# Days():
    row +=1
    t_percent =   (h_micro /MICRODAY) 
    label_time_count[row].config(text='%10.8f' %( now.day + t_percent%1))
    t_percent *=100
    pbars[row]['value'] = t_percent
    
    label_percents[row].config(text="{:.0f}%".format(t_percent))


# months():
    row +=1
    days_in_month = month_days(now.month,now.year)
    mircomonth = MICRODAY  * days_in_month
    t_percent =   (d_micro /mircomonth) 
    label_time_count[row].config(text='%10.8f' %( now.month+t_percent),justify=RIGHT)
    t_percent *= 100
    pbars[row]['value'] = t_percent 
    label_percents[row].config(text="{:.0f}%".format(t_percent))


#Years():
    row+=1
    y_micro = MICRODAY * now.timetuple().tm_yday + h_micro

    t_percent =   (y_micro /MICROYEAR) 
    label_time_count[row].config(text='%12.8f' %( now.year+t_percent))
    t_percent *= 100
    pbars[row]['value'] = t_percent
    label_percents[row].config(text="{:.0f}%".format(t_percent))
    
    canvas.after(10,Seconds)
   
def bitadd():
    label_bit_add.config(text=bits)
    index = 0
    while index < len(bits):  
        if bits[index] == "\u25A0":
            bits[index] ="\u25A1"
            break 
        elif bits[index] == "\u25A1" and index != len(bits)-1:
            bits[index] = "\u25A0"
            index+=1  
        else:
            for i in range(len(bits)):
                bits[i]="\u25A0"
            break  
    canvas.after(1000,bitadd)

label_bit_add = Label(app,background=BACKGROUND)
label_bit_add.grid(row=8,columnspan=4)
label_first_column = Create_time_labels()
label_time_count = Create_time_count_labels()
pbars = Create_progress_bars()
label_percents = Create_percent_labels()
time_display = Label(app, text = 'TIME',background=BACKGROUND)

time_display.grid(row=0,columnspan=4)
b = Thread(target=bitadd)
b.start()
new_thread = Thread(target=Seconds)
new_thread.start()




#app.overrideredirect(True)
app.mainloop()


