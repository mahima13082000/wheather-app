from tkinter import *
import requests
import json
import win32com.client


window = Tk()
window.title("WHETHER APP")
#window.minsize(width=400,height=500)
#window.maxsize(width=400,height=500)
l1 = Label(window,text= "WHETHER APP",bg="blue",fg="white",width=40)
l1.place(x=560,y=250)
# l1.grid(row=0,column=5)
# l1.pack()
img= PhotoImage(file="C:/Users/mishr/OneDrive/Documents/my documents/logo5.png")
l2= Label(window,image=img)
l2.pack()


v = StringVar()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(f"PLEASE ENTER YOUR LOCATION AND ENTER SUBBMIT BUTTON WHEN APP IS OPEN")
def action():

    city  = v.get()
    url =  "http://api.weatherapi.com/v1/current.json?key=ea48052d07b04c1cbe952029230107&q="+ city
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(f"HERE IS DETAILS ABOUT YOUR LOCATION")

    df = requests.get(url)
    data = json.loads(df.content)
    l3.config(text=""+str(data['current']['temp_c']),bg="white",fg="blue")
    l4.config(text=""+str(data['location']['name']),bg="white",fg="blue")
    l5.config(text="ENTER YOUR LOCATION:->",bg="white",fg="blue")
    l6.config(text="YOUR LOCATION IS:->",bg="white",fg="blue") 
    l7.config(text="TEMPERATURE IN CALCICUS:->",bg="white",fg="blue")
    l8.config(text=""+str(data['location']['region']),bg="white",fg="blue")
    l9.config(text="TEMPERATURE IN FAHERNEHITE IS:->",bg="white",fg="blue")
    l11.config(text="REGION IS :->",bg="white",fg="blue")
    l10.config(text=""+str(data['current']['temp_f']),bg="white",fg="blue")
    l12.config(text=""+str(data['location']['country']),bg="white",fg="blue")
    l13.config(text="Country is:->",bg="white",fg="blue")
  

e1 = Entry(window,width=20,font=("arial",20),textvariable=v)
e1.place(x=560,y=300)


b1 = Button(window,text="SUBMIT",bg="white",fg="blue",command=action)
b1.place(x=560,y=350)
l3 = Label(window,text= "GET TEMPERATURE IN CALCIUS",bg="white",fg="blue",width=30)
l3.place(x=560,y=400)

l4 = Label(window,text="GET LOCATION",bg="white",fg="blue",width=30)
l4.place(x=560,y=450)

l5 = Label(window,text="ENTER YOUR LOCATION:->",bg="white",fg="blue",width=30)
l5.place(x=250,y=300)

l6 = Label(window,text=" YOUR LOCATION IS:->",bg="white",fg="blue",width=30)
l6.place(x=250,y=450)

l7 = Label(window,text=" TEMPERATURE IN CALCICUS IS:->",bg="white",fg="blue",width=30)
l7.place(x=250,y=400)



l11 = Label(window,text=" REGION  IS:->",bg="white",fg="blue",width=30)
l11.place(x=250,y=560)


l9 = Label(window,text=" TEMPERATURE IN FAHERNEHITE IS:->",bg="white",fg="blue",width=30)
l9.place(x=260,y=500)

l8 = Label(window,text= " GET REGION ",bg="white",fg="blue",width=20)
l8.place(x=600,y=550)

l10= Label(window,text=" GET TEMPERATURE IN FAHERNEHITE IS ",bg="white",fg="blue",width=30)
l10.place(x=580,y=500)

l12= Label(window,text=" GET COUNTRY ",bg="white",fg="blue",width=20)
l12.place(x=590,y=600)

l13 = Label(window,text=" COUNTRY IS:->",bg="white",fg="blue",width=30)
l13.place(x=250,y=600)



# l1.place(x=500,y=200)
# window.minsize(width=100,height=200)
# window.maxsize(width=600,height=800)
window.mainloop()
