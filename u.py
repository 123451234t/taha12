from tkinter import*
win=Tk()
win.geometry("600x400")
win.config(bg="aqua")
import bak
db=bak
# =============================funcshen=====================

def select():

































################widget#################
lbl_name=Label(win,text="نام:")
lbl_name.place(x=20,y=20)
ent_name=Entry(win)
ent_name.place(x=100,y=20)
lbl_lname=Label(win,text="نام خانوادگی:")
lbl_lname.place(x=20,y=50)
ent_lname=Entry(win)
ent_lname.place(x=100,y=50)
lbl_cname=Label(win,text=":رمز ورود")
lbl_cname.place(x=480,y=20)
ent_cname=Entry(win)
ent_cname.place(x=300,y=20)
lbl_cname=Label(win,text=":نام دوره")
lbl_cname.place(x=480,y=50)
ent_cname=Entry(win)
ent_cname.place(x=300,y=50)

lst_name=Listbox(win,width=50)
lst_name.place(x=20,y=90)

btn_see=Button(win,text="مشاهده همه",width=15,command=select)
btn_see.place(x=450,y=90)

btn_insert=Button(win,text="اضافه کردن",width=15,command=insert)
btn_insert.place(x=450,y=120)

btn_delete_ent=Button(win,text="خالی کردن ورودیها",width=15,command=delete_ent)
btn_delete_ent.place(x=450,y=150)

btn_delete=Button(win,text="حذف کردن",width=15,command=delete)
btn_delete.place(x=450,y=180)

btn_exit=Button(win,text="خروج",width=15,command=exit1)
btn_exit.place(x=450,y=210)

btn_open=Button(win,text="ورود به سامانه",width=15,command=open2)
btn_open.place(x=450,y=240)

lbl_name=Label(win,text="☝👌رمز ورود")
lbl_name.pack(side=BOTTOM)

ent_name=Entry(win,show="*",width=50)
ent_name.pack(side=BOTTOM)



win.mainloop()