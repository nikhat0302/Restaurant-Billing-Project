from tkinter import*
from PIL import ImageTk
import mysql.connector
import math
import random
import datetime
from tkinter import messagebox

conn=mysql.connector.connect(host="localhost",user="root",password="password123",database="mydb")
mycursor=conn.cursor()

class Restaurant:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x777+0+0")
        self.root.title("CookBook Billing System")
        self.root.resizable(0,0)
        
        #---------------photos-----------------
        self.logo_icon1=ImageTk.PhotoImage(file="chef.jpg")
        self.logo_icon2=PhotoImage(file="fork.png")

        #------------------------frame-----------------
        frame =Frame(self.root)
        frame.place(x=0,y=0,relwidth=1)

        Label(frame,text="CookBook Restaurant",image=self.logo_icon2,compound=LEFT,font="mistral 55 bold",bg="lightgoldenrod",bd=5,relief=GROOVE).grid(row=0,column=1,ipadx=500)

        #-------------------frame1-------------------
        frame1=LabelFrame(self.root,text="Customer Details",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame1.place(x=0,y=102,relwidth=1)

        cus_name=StringVar()
        cus_num=StringVar()
        cus_bill=IntVar()
        

        Label(frame1,text="Customer Name",font="arial 15 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=10)
        Entry(frame1,textvariable=cus_name,font="arial 15").grid(row=0,column=1,pady=3,padx=10)
        Label(frame1,text="      Contact Number",font="arial 15 bold",bg="lightgoldenrod").grid(row=0,column=2,ipady=10)
        Entry(frame1,textvariable=cus_num,font="arial 15").grid(row=0,column=3,pady=3,padx=10)
        Label(frame1,text="       Bill Number",font="arial 15 bold",bg="lightgoldenrod").grid(row=0,column=4,ipady=10)
        Entry(frame1,textvariable=cus_bill).grid(row=0,column=5,pady=3,padx=10)
        Label(frame1,text="\tcookbook@ac.in",font="arial 15 bold",bg="lightgoldenrod").grid(row=0,column=7)

        def search_bill():
            sql=str(cus_bill.get())+str(".txt")
            f=open(sql,"r")
            txtar.delete(1.0,END)
            txtar.insert(END,f.read())

        Button(frame1,text="Search",font="arial 13 bold",bg="lightgoldenrod",command=search_bill).grid(row=0,column=6,padx=25)

        #------------------------frame2-------------------
        frame2=LabelFrame(self.root,text="Starter",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame2.place(x=0,y=177,width=300)

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()

        Label(frame2,text="Spring Roll",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=10)
        Entry(frame2,textvariable=var1,font="arial 14",width=8).grid(row=0,column=1,pady=3)
        Label(frame2,text="Paneer Chilly",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=0,ipady=10)
        Entry(frame2,textvariable=var2,font="arial 14",width=8).grid(row=1,column=1,padx=5,pady=3)
        Label(frame2,text="Hakka Noodles",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=0,ipady=10)
        Entry(frame2,textvariable=var3,font="arial 14",width=8).grid(row=2,column=1,padx=5,pady=3)
        Label(frame2,text="Garlic Bread",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=0,ipady=10)
        Entry(frame2,textvariable=var4,font="arial 14",width=8).grid(row=3,column=1,padx=5,pady=3)
        Label(frame2,text="Fruit Salad",font="arial 14 bold",bg="lightgoldenrod").grid(row=4,column=0,ipady=10)
        Entry(frame2,textvariable=var5,font="arial 14",width=8).grid(row=4,column=1,padx=5,pady=3)
        Label(frame2,text="Italian Chaap",font="arial 14 bold",bg="lightgoldenrod").grid(row=5,column=0,ipady=10)
        Entry(frame2,textvariable=var6,font="arial 14",width=8).grid(row=5,column=1,padx=5,pady=3)
        Label(frame2,text="Chilly Potato",font="arial 14 bold",bg="lightgoldenrod").grid(row=6,column=0,ipady=10)
        Entry(frame2,textvariable=var7,font="arial 14",width=8).grid(row=6,column=1,padx=5,pady=3)
        Label(frame2,text="Veg Chowmin",font="arial 14 bold",bg="lightgoldenrod").grid(row=7,column=0,ipady=10)
        Entry(frame2,textvariable=var8,font="arial 14",width=8).grid(row=7,column=1,padx=5,pady=3)

        #------------------------frame3-------------------
        frame3=LabelFrame(self.root,text="Meals",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame3.place(x=305,y=177,width=300)

        
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()

        Label(frame3,text="Veg Biryani",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=10)
        Entry(frame3,textvariable=var9,font="arial 14",width=8).grid(row=0,column=1,pady=3)
        Label(frame3,text="Murgh Tufani",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=0,ipady=10)
        Entry(frame3,textvariable=var10,font="arial 14",width=8).grid(row=1,column=1,padx=5,pady=3)
        Label(frame3,text="Egg Masala",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=0,ipady=10)
        Entry(frame3,textvariable=var11,font="arial 14",width=8).grid(row=2,column=1,padx=5,pady=3)
        Label(frame3,text="Fried Rice",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=0,ipady=10)
        Entry(frame3,textvariable=var12,font="arial 14",width=8).grid(row=3,column=1,padx=5,pady=3)
        Label(frame3,text="Dal Makhani",font="arial 14 bold",bg="lightgoldenrod").grid(row=4,column=0,ipady=10)
        Entry(frame3,textvariable=var13,font="arial 14",width=8).grid(row=4,column=1,padx=5,pady=3)
        Label(frame3,text="Sambhar Rice",font="arial 14 bold",bg="lightgoldenrod").grid(row=5,column=0,ipady=10)
        Entry(frame3,textvariable=var14,font="arial 14",width=8).grid(row=5,column=1,padx=5,pady=3)
        Label(frame3,text="Rajma Chawal",font="arial 14 bold",bg="lightgoldenrod").grid(row=6,column=0,ipady=10)
        Entry(frame3,textvariable=var15,font="arial 14",width=8).grid(row=6,column=1,padx=5,pady=3)
        Label(frame3,text="Stuffed Kulcha",font="arial 14 bold",bg="lightgoldenrod").grid(row=7,column=0,ipady=10)
        Entry(frame3,textvariable=var16,font="arial 14",width=8).grid(row=7,column=1,padx=5,pady=3)

        #------------------------frame4-------------------
        frame4=LabelFrame(self.root,text="Cold Drinks",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame4.place(x=895,y=177,width=250)

        var17=IntVar()
        var18=IntVar()
        var19=IntVar()
        var20=IntVar()
        var21=IntVar()
        var22=IntVar()
        var23=IntVar()
        var24=IntVar()

        Label(frame4,text="Frooti",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=10)
        Entry(frame4,textvariable=var17,font="arial 14",width=8).grid(row=0,column=1,pady=3)
        Label(frame4,text="Pepsi",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=0,ipady=10)
        Entry(frame4,textvariable=var18,font="arial 14",width=8).grid(row=1,column=1,padx=5,pady=3)
        Label(frame4,text="Maaza",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=0,ipady=10)
        Entry(frame4,textvariable=var19,font="arial 14",width=8).grid(row=2,column=1,padx=5,pady=3)
        Label(frame4,text="Limca",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=0,ipady=10)
        Entry(frame4,textvariable=var20,font="arial 14",width=8).grid(row=3,column=1,padx=5,pady=3)
        Label(frame4,text="Slice",font="arial 14 bold",bg="lightgoldenrod").grid(row=4,column=0,ipady=10)
        Entry(frame4,textvariable=var21,font="arial 14",width=8).grid(row=4,column=1,padx=5,pady=3)
        Label(frame4,text="Mirinda",font="arial 14 bold",bg="lightgoldenrod").grid(row=5,column=0,ipady=10)
        Entry(frame4,textvariable=var22,font="arial 14",width=8).grid(row=5,column=1,padx=5,pady=3)
        Label(frame4,text="Sprit",font="arial 14 bold",bg="lightgoldenrod").grid(row=6,column=0,ipady=10)
        Entry(frame4,textvariable=var23,font="arial 14",width=8).grid(row=6,column=1,padx=5,pady=3)
        Label(frame4,text="Juice",font="arial 14 bold",bg="lightgoldenrod").grid(row=7,column=0,ipady=10)
        Entry(frame4,textvariable=var24,font="arial 14",width=8).grid(row=7,column=1,padx=5,pady=3)

        #------------------------frame5-------------------
        frame5=LabelFrame(self.root,text="Desserts",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame5.place(x=610,y=177,width=280)

        var25=IntVar()
        var26=IntVar()
        var27=IntVar()
        var28=IntVar()
        var29=IntVar()
        var30=IntVar()
        var31=IntVar()
        var32=IntVar()

        Label(frame5,text="Battenburg",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=10)
        Entry(frame5,textvariable=var25,font="arial 14",width=8).grid(row=0,column=1,pady=3)
        Label(frame5,text="Fairy Bun",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=0,ipady=10)
        Entry(frame5,textvariable=var26,font="arial 14",width=8).grid(row=1,column=1,padx=5,pady=3)
        Label(frame5,text="Ice cream",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=0,ipady=10)
        Entry(frame5,textvariable=var27,font="arial 14",width=8).grid(row=2,column=1,padx=5,pady=3)
        Label(frame5,text="Fab Choco",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=0,ipady=10)
        Entry(frame5,textvariable=var28,font="arial 14",width=8).grid(row=3,column=1,padx=5,pady=3)
        Label(frame5,text="Doughnot",font="arial 14 bold",bg="lightgoldenrod").grid(row=4,column=0,ipady=10)
        Entry(frame5,textvariable=var29,font="arial 14",width=8).grid(row=4,column=1,padx=5,pady=3)
        Label(frame5,text="Chess Pie",font="arial 14 bold",bg="lightgoldenrod").grid(row=5,column=0,ipady=10)
        Entry(frame5,textvariable=var30,font="arial 14",width=8).grid(row=5,column=1,padx=5,pady=3)
        Label(frame5,text="Peach Crisp",font="arial 14 bold",bg="lightgoldenrod").grid(row=6,column=0,ipady=10)
        Entry(frame5,textvariable=var31,font="arial 14",width=8).grid(row=6,column=1,padx=5,pady=3)
        Label(frame5,text="Cherry Tart",font="arial 14 bold",bg="lightgoldenrod").grid(row=7,column=0,ipady=10)
        Entry(frame5,textvariable=var32,font="arial 14",width=8).grid(row=7,column=1,padx=5,pady=3)

        #------------------------frame7-------------------
        frame7=LabelFrame(self.root,text="Billing Menu",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame7.place(x=0,y=587)

        txt1=DoubleVar()
        txt2=DoubleVar()
        txt3=DoubleVar()
        txt4=DoubleVar()
        txt5=DoubleVar()
        txt6=DoubleVar()
        txt7=DoubleVar()
        txt8=DoubleVar()

        Label(frame7,text="Total Starter Price",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=0,ipady=5)
        Label(frame7,textvariable=txt1,font="arial 14",width=8).grid(row=0,column=1)
        Label(frame7,text="Total Meal Price",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=0,ipady=5)
        Label(frame7,textvariable=txt2,font="arial 14",width=8).grid(row=1,column=1)
        Label(frame7,text="Total Desserts Price",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=0,ipady=5)
        Label(frame7,textvariable=txt3,font="arial 14",width=8).grid(row=2,column=1)
        Label(frame7,text="Total Cold Drink Price",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=0,ipady=5)
        Label(frame7,textvariable=txt4,font="arial 14",width=8).grid(row=3,column=1)

        Label(frame7,bg="lightgoldenrod").grid(row=0,column=2,padx=5)

        Label(frame7,text="Starter Tax",font="arial 14 bold",bg="lightgoldenrod").grid(row=0,column=3,ipady=5)
        Label(frame7,textvariable=txt5,font="arial 14",width=8).grid(row=0,column=4,padx=5)
        Label(frame7,text="Meal Tax",font="arial 14 bold",bg="lightgoldenrod").grid(row=1,column=3,ipady=5)
        Label(frame7,textvariable=txt6,font="arial 14",width=8).grid(row=1,column=4)
        Label(frame7,text="Desserts Tax",font="arial 14 bold",bg="lightgoldenrod").grid(row=2,column=3,ipady=5)
        Label(frame7,textvariable=txt7,font="arial 14",width=8).grid(row=2,column=4)
        Label(frame7,text="Cold Drink Tax",font="arial 14 bold",bg="lightgoldenrod").grid(row=3,column=3,ipady=5)
        Label(frame7,textvariable=txt8,font="arial 14",width=8).grid(row=3,column=4)

        #------------------------frame8-------------------
        frame8=LabelFrame(self.root,text="Buttons",font="arial 10 bold",bd=5,relief= GROOVE,bg="lightgoldenrod")
        frame8.place(x=575,y=587)

        #-----------------------total function--------------------
        def func(name,bill_no,num):
            txtar.delete(1.0,END)
            txtar.insert(END,"\t\t      Bill Area\n")
            txtar.insert(END,"\t\tCookBook Restaurant\n\t\tHappy To Serve You!\n\n")
            txtar.insert(END,"Contact Us : 2345667531")
            txtar.insert(END,"\nBill No. : ")
            txtar.insert(END,bill_no)
            txtar.insert(END,"\nCustomer Name : ")
            txtar.insert(END,name)
            txtar.insert(END,"\nContact No. : ")
            txtar.insert(END,num)
            txtar.insert(END,"\n\n*********************************************\n")
            txtar.insert(END,"Product\t\t     Quantity\t\tPrice")
            txtar.insert(END,"\n*********************************************\n")

        frame6=Frame(self.root)
        frame6.place(x=1150,y=177)
        txtar=Text(frame6,width=45,height=37)
        txtar.grid(row=0,column=0)

        num=""
        bill_no=""       
        name=""
        func(name,bill_no,num)

        def total_button():
            starter=var1.get()*50+var2.get()*80+var3.get()*120+var4.get()*40+var5.get()*50+var6.get()*50+var7.get()*80+var8.get()*100
            txt1.set(starter)
            txt5.set(starter*0.05)

            meal=var9.get()*200+var10.get()*150+var11.get()*80+var12.get()*120+var13.get()*90+var14.get()*50+var15.get()*80+var16.get()*40
            txt2.set(meal)
            txt6.set(meal*0.1)
            
            dessert=var25.get()*50+var26.get()*60+var27.get()*50+var28.get()*70+var29.get()*50+var30.get()*60+var31.get()*50+var32.get()*60
            txt3.set(dessert)
            txt7.set(dessert*0.05)

            drink=var17.get()*20+var18.get()*20+var19.get()*20+var20.get()*20+var21.get()*20+var22.get()*20+var23.get()*20+var24.get()*15
            txt4.set(drink)
            txt8.set(drink*0.02)

        #----------------------bill generation---------------------
        
        def gen_bill():
            total_button()
            name=cus_name.get()
            bill_no=random.randint(1000,9999)
            num=cus_num.get()
            func(name,bill_no,num)
            
            if (len(name)<=0):
                messagebox.showerror("Error","Enter the Customer Details")
                clear_data()
            #elif (len(num)!=10):
                #messagebox.showerror("Error","Enter 10 digit Contact Number")
                clear_data()
            elif (txt1.get()<=0 and txt2.get()<=0 and txt3.get()<=0 and txt4.get()<=0):
                messagebox.showerror("Error","Select at least One Item")

            #----------------------starter pack-----------------
            starter=[50,80,120,40,50,50,100,200]
            if var1.get()>0:
                price=("Spring Roll\t\t\t"+str(var1.get())+"\t\t"+str(starter[0]*var1.get())+"\n")
                txtar.insert(END,price)
            if var2.get()>0:
                price=("Paneer Chilli\t\t\t"+str(var2.get())+"\t\t"+str(starter[1]*var2.get())+"\n")
                txtar.insert(END,price)
            if var3.get()>0:
                price=("Paneer Chilli\t\t\t"+str(var3.get())+"\t\t"+str(starter[2]*var3.get())+"\n")
                txtar.insert(END,price)
            if var4.get()>0:
                price=("Hakka Noodlesi\t\t\t"+str(var4.get())+"\t\t"+str(starter[3]*var4.get())+"\n")
                txtar.insert(END,price)
            if var5.get()>0:
                price=("Garlic Bread\t\t\t"+str(var5.get())+"\t\t"+str(starter[4]*var5.get())+"\n")
                txtar.insert(END,price)
            if var6.get()>0:
                price=("Fruit Salad\t\t\t"+str(var6.get())+"\t\t"+str(starter[5]*var6.get())+"\n")
                txtar.insert(END,price)
            if var7.get()>0:
                price=("Chilly Potato\t\t\t"+str(var7.get())+"\t\t"+str(starter[6]*var7.get())+"\n")
                txtar.insert(END,price)
            if var8.get()>0:
                price=("Veg Chowmin\t\t\t"+str(var8.get())+"\t\t"+str(starter[7]*var8.get())+"\n")
                txtar.insert(END,price)

            #---------------------meals---------------------
            meal=[200,150,80,120,90,50,80,40]
            meal_item=["Veg Biryani","Murgh Tufani","Egg Masala","Fried Rice","Dal Makhani","Sambhar Rice","Rajma Chawal","Stuffed Kulcha"]
            if var9.get()>0:
                price=(meal_item[0]+"\t\t\t"+str(var9.get())+"\t\t"+str(meal[0]*var9.get())+"\n")
                txtar.insert(END,price)
            if var10.get()>0:
                price=(meal_item[1]+"\t\t\t"+str(var10.get())+"\t\t"+str(meal[1]*var10.get())+"\n")
                txtar.insert(END,price)
            if var11.get()>0:
                price=(meal_item[2]+"\t\t\t"+str(var11.get())+"\t\t"+str(meal[2]*var11.get())+"\n")
                txtar.insert(END,price)
            if var12.get()>0:
                price=(meal_item[3]+"\t\t\t"+str(var12.get())+"\t\t"+str(meal[3]*var12.get())+"\n")
                txtar.insert(END,price)
            if var13.get()>0:
                price=(meal_item[4]+"\t\t\t"+str(var13.get())+"\t\t"+str(meal[4]*var13.get())+"\n")
                txtar.insert(END,price)
            if var14.get()>0:
                price=(meal_item[5]+"\t\t\t"+str(var14.get())+"\t\t"+str(meal[5]*var14.get())+"\n")
                txtar.insert(END,price)
            if var15.get()>0:
                price=(meal_item[6]+"\t\t\t"+str(var15.get())+"\t\t"+str(meal[6]*var15.get())+"\n")
                txtar.insert(END,price)
            if var16.get()>0:
                price=(meal_item[7]+"\t\t\t"+str(var16.get())+"\t\t"+str(meal[7]*var16.get())+"\n")
                txtar.insert(END,price)

            #---------------------desserts---------------------
            dessert=[50,60,50,70,50,60,50,60]
            dessert_item=["Battenburg","Fairy Bun","Ice cream","Fab Choco","Doughnot","Chess Pie","Peach Crisp","Cherry Tart"]
            if var25.get()>0:
                price=(dessert_item[0]+"\t\t\t"+str(var25.get())+"\t\t"+str(dessert[0]*var25.get())+"\n")
                txtar.insert(END,price)
            if var26.get()>0:
                price=(dessert_item[1]+"\t\t\t"+str(var26.get())+"\t\t"+str(dessert[1]*var26.get())+"\n")
                txtar.insert(END,price)
            if var27.get()>0:
                price=(dessert_item[2]+"\t\t\t"+str(var27.get())+"\t\t"+str(dessert[2]*var27.get())+"\n")
                txtar.insert(END,price)
            if var28.get()>0:
                price=(dessert_item[3]+"\t\t\t"+str(var28.get())+"\t\t"+str(dessert[3]*var28.get())+"\n")
                txtar.insert(END,price)
            if var29.get()>0:
                price=(dessert_item[4]+"\t\t\t"+str(var29.get())+"\t\t"+str(dessert[4]*var29.get())+"\n")
                txtar.insert(END,price)
            if var30.get()>0:
                price=(dessert_item[5]+"\t\t\t"+str(var30.get())+"\t\t"+str(dessert[5]*var30.get())+"\n")
                txtar.insert(END,price)
            if var31.get()>0:
                price=(dessert_item[6]+"\t\t\t"+str(var31.get())+"\t\t"+str(dessert[6]*var31.get())+"\n")
                txtar.insert(END,price)
            if var32.get()>0:
                price=(dessert_item[7]+"\t\t\t"+str(var32.get())+"\t\t"+str(dessert[7]*var32.get())+"\n")
                txtar.insert(END,price)

            #---------------------cold drinks---------------------
            drink=[20,20,20,20,20,20,20,15]
            drink_item=["Frooti","Pepsi","Maaza","Limca","Slice","Mirinda","Sprit","Juice"]
            if var17.get()>0:
                price=(drink_item[0]+"\t\t\t"+str(var17.get())+"\t\t"+str(drink[0]*var17.get())+"\n")
                txtar.insert(END,price)
            if var18.get()>0:
                price=(drink_item[1]+"\t\t\t"+str(var18.get())+"\t\t"+str(drink[1]*var18.get())+"\n")
                txtar.insert(END,price)
            if var19.get()>0:
                price=(drink_item[2]+"\t\t\t"+str(var19.get())+"\t\t"+str(drink[2]*var19.get())+"\n")
                txtar.insert(END,price)
            if var20.get()>0:
                price=(drink_item[3]+"\t\t\t"+str(var20.get())+"\t\t"+str(drink[3]*var20.get())+"\n")
                txtar.insert(END,price)
            if var21.get()>0:
                price=(drink_item[4]+"\t\t\t"+str(var21.get())+"\t\t"+str(drink[4]*var21.get())+"\n")
                txtar.insert(END,price)
            if var22.get()>0:
                price=(drink_item[5]+"\t\t\t"+str(var22.get())+"\t\t"+str(drink[5]*var22.get())+"\n")
                txtar.insert(END,price)
            if var23.get()>0:
                price=(drink_item[6]+"\t\t\t"+str(var23.get())+"\t\t"+str(drink[6]*var23.get())+"\n")
                txtar.insert(END,price)
            if var24.get()>0:
                price=(drink_item[7]+"\t\t\t"+str(var24.get())+"\t\t"+str(drink[7]*var24.get())+"\n")
                txtar.insert(END,price)
            
            txtar.insert(END,"*********************************************")
            txtar.insert(END,"Total Product Price :\t")
            txtar.insert(END,txt1.get()+txt2.get()+txt3.get()+txt4.get())
            txtar.insert(END,"\nTotal Tax :\t\t")
            txtar.insert(END,txt5.get()+txt6.get()+txt7.get()+txt8.get())
            txtar.insert(END,"\nTotal Amount :\t\t")
            txtar.insert(END,txt1.get()+txt2.get()+txt3.get()+txt4.get()+txt5.get()+txt6.get()+txt7.get()+txt8.get())
            date=datetime.datetime.now()
            txtar.insert(END,"\n\n")
            txtar.insert(END,date)

            
            sql="insert into cookbook_bills (bill_no,description) values(%s,%s)"
            val=(bill_no,txtar.get(1.0,END))
            mycursor.execute(sql,val)
            conn.commit()

        #---------------clear---------------
        def clear_data():
            txtar.delete(1.0,END)
            name=""
            num=""
            bill_no=""
            func(name,num,bill_no)

            cus_name.set("")
            cus_num.set("")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)
            var21.set(0)
            var22.set(0)
            var23.set(0)
            var24.set(0)
            var25.set(0)
            var26.set(0)
            var27.set(0)
            var28.set(0)
            var29.set(0)
            var30.set(0)
            var31.set(0)
            var32.set(0)

            txt1.set(0.00)
            txt2.set(0.00)
            txt3.set(0.00)
            txt4.set(0.00)
            txt5.set(0.00)
            txt6.set(0.00)
            txt7.set(0.00)
            txt8.set(0.00)

        Button(frame8,text="Total",font="arial 20 bold",command=total_button).grid(row=0,column=0,pady=50,ipadx=5,padx=10)
        btn=Button(frame8,text="Generate Bill",font="arial 20 bold",command=gen_bill).grid(row=0,column=1,pady=50,ipadx=5,padx=5)
        Button(frame8,text="Clear",font="arial 20 bold",command=clear_data).grid(row=0,column=2,pady=50,ipadx=5,padx=5)
        Button(frame8,text="Exit",font="arial 20 bold",command=quit).grid(row=0,column=3,pady=50,ipadx=5,padx=10)

if __name__ == "__main__":
    root=Tk()
    obj=Restaurant(root)
    root.mainloop()
