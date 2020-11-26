from tkinter import *
from tkinter import messagebox
import dbConnection as mydb
mycon = mydb.returnConnection()
mycur = mycon.cursor()

def saveRecord(ent1,ent2,ent3,ent4,addf):
	global mycon,mycur
	try:
		query="insert into emp values({0},'{1}','{2}',{3})".format(ent1.get(),ent2.get(),ent3.get(),ent4.get())
		mycur.execute(query)
		mycon.commit()
		messagebox.showinfo("...:::Insert","Record Added Successfully")
		addf.lift(mywin)  # to reduce problem of minimize after messagebox
	except:
		messagebox.showinfo("...:::Insert","## Error ##")
		addf.lift(mywin)
def resetFields(eno,en,dp,sl,ent1):
	eno.set('')
	en.set('')
	dp.set('')
	sl.set('')
	ent1.focus_set()
	
	
	
def addEmployee():
	eno=StringVar()
	en=StringVar()
	dp=StringVar()
	sl=StringVar()
	addForm = Toplevel(mywin)
	addForm.title("...:::New Employee Registration")
	addForm.geometry("380x350+400+220")
	addForm.resizable(False,False)
	lb1=Label(addForm,text="NEW EMPLOYEE FORM",bg='black',fg='white',font=('verdana',12,'bold'),width=30)
	lb1.grid(row=0,column=0, columnspan=2)
	
	lbeno = Label(addForm,text="Employee Number",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbeno.grid(row=1,column=0,pady=10,sticky=W,padx=4)
	
	enteno = Entry(addForm,textvariable=eno,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	enteno.grid(row=1,column=1,pady=10,sticky=W)
	
	lbname = Label(addForm,text="Employee Name",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbname.grid(row=2,column=0,pady=10,padx=4,sticky=W)
	
	entname = Entry(addForm,textvariable=en,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entname.grid(row=2,column=1,pady=10,sticky=W)
	
	lbdept = Label(addForm,text="Employee Department",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbdept.grid(row=3,column=0,pady=10,sticky=W,padx=4)
	
	entdept = Entry(addForm,textvariable=dp,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entdept.grid(row=3,column=1,pady=10,sticky=W)
	
	lbsalary = Label(addForm,text="Employee Salary",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbsalary.grid(row=4,column=0,pady=10,sticky=W,padx=4)
	
	entsalary = Entry(addForm,textvariable=sl,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entsalary.grid(row=4,column=1,pady=10,sticky=W)
	addForm.lift()
	Button(addForm,text="Save",command=lambda:saveRecord(enteno,entname,entdept,entsalary,addForm),width=10,bg='brown',fg='white',font=('verdana',10,'bold')).grid(row=5,column=0)
	Button(addForm,text="Clear",command=lambda:resetFields(eno,en,dp,sl,enteno),bg='brown',fg='white',font=('verdana',10,'bold'),width=10).grid(row=5,column=1)
	Button(addForm,text="Close Me!",command=addForm.destroy,width=20,bg='black',fg='white',font=('verdana',10,'bold')).grid(row=6,column=0,columnspan=2,pady=5)
def findRecord(eno,en,dp,sl,edf):
	global mycon,mycur
	e = eno.get()
	query="select * from emp where empno={0}".format(e)
	mycur.execute(query)
	mydata = mycur.fetchone()
	if mycur.rowcount>0:
		en.set(mydata[1])
		dp.set(mydata[2])
		sl.set(mydata[3])
	else:
		messagebox.showinfo('Not Found','No Matching Employee Number')
		edf.lift(mywin)
def updateRecord(eno,en,dp,sl,edf):
	global mycon,mycur
	query="update emp set dept='{0}',salary={1} where empno={2}".format(dp.get(),sl.get(),eno.get())
	mycur.execute(query)
	mycon.commit()
	messagebox.showinfo('Update','Record Updated successfully!')
	edf.lift(mywin)
def editEmployee():
	eno=StringVar()
	en=StringVar()
	dp=StringVar()
	sl=StringVar()
	editForm = Toplevel(mywin)
	editForm.title("...:::Edit Employee Form")
	editForm.geometry("450x350+400+220")
	editForm.resizable(False,False)
	lb1=Label(editForm,text="EDIT EMPLOYEE FORM",bg='black',fg='white',font=('verdana',12,'bold'),width=30)
	lb1.grid(row=0,column=0, columnspan=2)
	
	lbeno = Label(editForm,text="Employee Number",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbeno.grid(row=1,column=0,pady=10,sticky=W,padx=4)
	Button(editForm,text="Find",command=lambda:findRecord(eno,en,dp,sl,editForm)).grid(row=1,column=2)
	enteno = Entry(editForm,textvariable=eno,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	enteno.grid(row=1,column=1,pady=10,sticky=W)
	
	lbname = Label(editForm,text="Employee Name",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbname.grid(row=2,column=0,pady=10,padx=4,sticky=W)
	
	entname = Entry(editForm,textvariable=en,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entname.grid(row=2,column=1,pady=10,sticky=W)
	
	lbdept = Label(editForm,text="Employee Department",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbdept.grid(row=3,column=0,pady=10,sticky=W,padx=4)
	
	entdept = Entry(editForm,textvariable=dp,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entdept.grid(row=3,column=1,pady=10,sticky=W)
	
	lbsalary = Label(editForm,text="Employee Salary",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbsalary.grid(row=4,column=0,pady=10,sticky=W,padx=4)
	
	entsalary = Entry(editForm,textvariable=sl,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entsalary.grid(row=4,column=1,pady=10,sticky=W)
	editForm.lift()
	Button(editForm,text="Update",command=lambda:updateRecord(enteno,entname,entdept,entsalary,editForm),width=10,bg='brown',fg='white',font=('verdana',10,'bold')).grid(row=5,column=0)
	Button(editForm,text="Clear",command=lambda:resetFields(eno,en,dp,sl,enteno),bg='brown',fg='white',font=('verdana',10,'bold'),width=10).grid(row=5,column=1)
	Button(editForm,text="Close Me!",command=editForm.destroy,width=20,bg='black',fg='white',font=('verdana',10,'bold')).grid(row=6,column=0,columnspan=2,pady=5)
def deleteRecord(eno,en,dp,sl,ldf):
	global mycon,mycur
	response = messagebox.askquestion('Delete?','Are You Sure to Delete ?')
	ldf.lift(mywin)
	if response=='yes':
		query="delete from emp where empno={0}".format(eno.get())
		mycur.execute(query)
		mycon.commit()
		messagebox.showinfo('Deleted','Record Deleted Successfully!')
		ldf.lift(mywin)
		

def deleteEmployee():
	eno=StringVar()
	en=StringVar()
	dp=StringVar()
	sl=StringVar()
	delForm = Toplevel(mywin)
	delForm.title("...:::Delete Employee Form")
	delForm.geometry("450x350+400+220")
	delForm.resizable(False,False)
	lb1=Label(delForm,text="DELETE EMPLOYEE FORM",bg='black',fg='white',font=('verdana',12,'bold'),width=30)
	lb1.grid(row=0,column=0, columnspan=2)
	
	lbeno = Label(delForm,text="Employee Number",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbeno.grid(row=1,column=0,pady=10,sticky=W,padx=4)
	Button(delForm,text="Find",command=lambda:findRecord(eno,en,dp,sl,delForm)).grid(row=1,column=2)
	enteno = Entry(delForm,textvariable=eno,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	enteno.grid(row=1,column=1,pady=10,sticky=W)
	
	lbname = Label(delForm,text="Employee Name",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbname.grid(row=2,column=0,pady=10,padx=4,sticky=W)
	
	entname = Entry(delForm,textvariable=en,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entname.grid(row=2,column=1,pady=10,sticky=W)
	
	lbdept = Label(delForm,text="Employee Department",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbdept.grid(row=3,column=0,pady=10,sticky=W,padx=4)
	
	entdept = Entry(delForm,textvariable=dp,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entdept.grid(row=3,column=1,pady=10,sticky=W)
	
	lbsalary = Label(delForm,text="Employee Salary",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbsalary.grid(row=4,column=0,pady=10,sticky=W,padx=4)
	
	entsalary = Entry(delForm,textvariable=sl,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entsalary.grid(row=4,column=1,pady=10,sticky=W)
	delForm.lift()
	Button(delForm,text="Update",command=lambda:deleteRecord(enteno,entname,entdept,entsalary,delForm),width=10,bg='brown',fg='white',font=('verdana',10,'bold')).grid(row=5,column=0)
	Button(delForm,text="Clear",command=lambda:resetFields(eno,en,dp,sl,enteno),bg='brown',fg='white',font=('verdana',10,'bold'),width=10).grid(row=5,column=1)
	Button(delForm,text="Close Me!",command=delForm.destroy,width=20,bg='black',fg='white',font=('verdana',10,'bold')).grid(row=6,column=0,columnspan=2,pady=5)

def searchEmployee():
	eno=StringVar()
	en=StringVar()
	dp=StringVar()
	sl=StringVar()
	searchForm = Toplevel(mywin)
	searchForm.title("...:::Search Employee Form")
	searchForm.geometry("450x350+400+220")
	searchForm.resizable(False,False)
	lb1=Label(searchForm,text="SEARCH EMPLOYEE FORM",bg='black',fg='white',font=('verdana',12,'bold'),width=30)
	lb1.grid(row=0,column=0, columnspan=2)
	
	lbeno = Label(searchForm,text="Employee Number",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbeno.grid(row=1,column=0,pady=10,sticky=W,padx=4)
	Button(searchForm,text="Find",command=lambda:findRecord(eno,en,dp,sl,searchForm)).grid(row=1,column=2)
	enteno = Entry(searchForm,textvariable=eno,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	enteno.grid(row=1,column=1,pady=10,sticky=W)
	
	lbname = Label(searchForm,text="Employee Name",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbname.grid(row=2,column=0,pady=10,padx=4,sticky=W)
	
	entname = Entry(searchForm,textvariable=en,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entname.grid(row=2,column=1,pady=10,sticky=W)
	
	lbdept = Label(searchForm,text="Employee Department",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbdept.grid(row=3,column=0,pady=10,sticky=W,padx=4)
	
	entdept = Entry(searchForm,textvariable=dp,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entdept.grid(row=3,column=1,pady=10,sticky=W)
	
	lbsalary = Label(searchForm,text="Employee Salary",bg='black',fg='yellow',font=('verdana',10,'bold'))
	lbsalary.grid(row=4,column=0,pady=10,sticky=W,padx=4)
	
	entsalary = Entry(searchForm,textvariable=sl,width=20,bg='yellow',fg='red',font=('verdana',10,'bold'))
	entsalary.grid(row=4,column=1,pady=10,sticky=W)
	searchForm.lift()
	Button(searchForm,text="Clear",command=lambda:resetFields(eno,en,dp,sl,enteno),bg='brown',fg='white',font=('verdana',10,'bold'),width=10).grid(row=5,column=1)
	Button(searchForm,text="Close Me!",command=searchForm.destroy,width=20,bg='black',fg='white',font=('verdana',10,'bold')).grid(row=6,column=0,columnspan=2,pady=5)


def showAll():
	global mycon,mycur
	allForm = Toplevel(mywin)
	allForm.title("...:::Employee Database")
	allForm.geometry("500x500+400+200")
	query="select * from emp"
	mycur.execute(query)
	ta = Text(allForm,height=30,width=80)
	ta.grid(row=0,column=0)
	records = mycur.fetchall()
	heading="%10s"%"EMPNO"+"%20s"%"NAME"+"%20s"%"DEPARTMENT"+"%10s"%"SALARY"+'\n'
	
	ta.insert(END,heading)
	
	ta.insert(END,"="*70)
	ta.insert(END,'\n')
	for row in records:
		rec = "%10s"%str(row[0])+"%20s"%row[1]+"%20s"%row[2]+"%10s"%str(row[3])+'\n'
		ta.insert(END,rec)
	ta.config(state=DISABLED)
def aboutUS():
        aboutmessage=''' Author : Vinod Kumar Verma
E-Mail : vinodexclusively@gmail.com
URL    : www.python4csip.com'''
                
        messagebox.showinfo('...::::About US',aboutmessage)
        

#Main Interface

mywin = Tk()
mywin.title("Employee Management System")
mywin.geometry("480x450+400+200")
mywin.resizable(False,False)
# mywin.iconbitmap("logo.ico")
mywin.config(bg='black')
Button(mywin,text="Add New Employee",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=addEmployee).pack(pady=10)
Button(mywin,text="Edit Employee",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=editEmployee).pack(pady=10)
Button(mywin,text="Delete Employee",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=deleteEmployee).pack(pady=10)
Button(mywin,text="Search Employee",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=searchEmployee).pack(pady=10)
Button(mywin,text="Show All Employee",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=showAll).pack(pady=10)
Button(mywin,text="About Us",bg='yellow',fg='blue' ,font=('arial',15,'bold'),width=30,command=aboutUS).pack(pady=10)
Button(mywin,text="Exit",bg='yellow',fg='blue',command=mywin.quit,font=('arial',15,'bold'),width=30).pack(pady=10)


mywin.mainloop()
