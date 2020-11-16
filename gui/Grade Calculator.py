from tkinter import *
import math
import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

class App(Tk):
  def __init__(self):
    Tk.__init__(self)
    #___________FONTS_______________
    self.headerFont = ("Mistral", "28")
    self.paraFont=('Sansita One', '14', 'bold')
    self.otherFont=("Sansita One", '13')
    
    style.use("ggplot")
    
    self.title("Grade Calculator")
    self.addCT()
    self.addExams()
    self.addOutput()
    
  def addCT(self):    
    """ add lab elements """
    Label(self, text = "Class Tests",
          font = self.headerFont).grid(columnspan =3)

#__________SUBJECTS___________________
    Label(self, text = "English", font=self.paraFont).grid(row = 1, column = 1)
    Label(self, text = "Maths", font=self.paraFont).grid(row = 1, column = 3)
    Label(self, text = "Science", font=self.paraFont).grid(row = 1, column = 5)
    Label(self, text = "Social Science", font=self.paraFont).grid(row = 1, column = 7)
    Label(self, text = "Hindi", font=self.paraFont).grid(row = 1, column = 9)
    Label(self, text = "Computer Sc.", font=self.paraFont).grid(row = 1, column = 11)
#_________________CT1______________
    Label(self, text = "Pre Mid Term", font=self.otherFont).grid(row = 2, column = 0)
    self.txtCT1e = Entry(self)
    self.txtCT1e.grid(row = 2, column = 1)
    self.txtCT1e.insert(0, "47")
 	
    Label(self, text = "").grid(row = 2, column = 2)
    self.txtCT1Mat = Entry(self)
    self.txtCT1Mat.grid(row = 2, column = 3)
    self.txtCT1Mat.insert(0, "48")
    
    Label(self, text = "").grid(row = 2, column = 4)
    self.txtCT1sc = Entry(self)
    self.txtCT1sc.grid(row = 2, column = 5)
    self.txtCT1sc.insert(0, "49")

    Label(self, text = "").grid(row = 2, column = 6)
    self.txtCT1s= Entry(self)
    self.txtCT1s.grid(row = 2, column = 7)
    self.txtCT1s.insert(0, "50")

    Label(self, text = "").grid(row = 2, column = 8)
    self.txtCT1h = Entry(self)
    self.txtCT1h.grid(row = 2, column = 9)
    self.txtCT1h.insert(0, "43")

    Label(self, text = "").grid(row = 2, column = 10)
    self.txtCT1it = Entry(self)
    self.txtCT1it.grid(row = 2, column = 11)
    self.txtCT1it.insert(0, "50")
    
#_________________CT2_________________
    Label(self, text = "Mid Term", font=self.otherFont).grid(row = 3, column = 0)
    self.txtCT2e = Entry(self)
    self.txtCT2e.grid(row = 3, column = 1)
    self.txtCT2e.insert(0, "80")

    Label(self, text = "").grid(row = 3, column = 2)
    self.txtCT2Mat = Entry(self)
    self.txtCT2Mat.grid(row = 3, column = 3)
    self.txtCT2Mat.insert(0, "79")

    Label(self, text ="").grid(row = 3, column = 4)
    self.txtCT2sc = Entry(self)
    self.txtCT2sc.grid(row = 3, column = 5)
    self.txtCT2sc.insert(0, "74")
    
    Label(self, text = "").grid(row = 3, column = 6)
    self.txtCT2s = Entry(self)
    self.txtCT2s.grid(row = 3, column = 7)
    self.txtCT2s.insert(0, "77")
    
    Label(self, text = "").grid(row = 3, column = 8)
    self.txtCT2h = Entry(self)
    self.txtCT2h.grid(row = 3, column = 9)
    self.txtCT2h.insert(0, "80")
    
    Label(self, text = "").grid(row = 3, column = 10)
    self.txtCT2it = Entry(self)
    self.txtCT2it.grid(row = 3, column = 11)
    self.txtCT2it.insert(0, "80")

    #_______________CT 3________________
    Label(self, text = "Post Mid Term", font=self.otherFont).grid(row = 4, column = 0)
    self.txtCT3e = Entry(self)
    self.txtCT3e.grid(row = 4, column = 1)
    self.txtCT3e.insert(0, "80")

    Label(self, text = "").grid(row = 4, column = 2)
    self.txtCT3Mat = Entry(self)
    self.txtCT3Mat.grid(row = 4, column = 3)
    self.txtCT3Mat.insert(0, "80")

    Label(self, text ="").grid(row = 4, column = 4)
    self.txtCT3sc = Entry(self)
    self.txtCT3sc.grid(row = 4, column = 5)
    self.txtCT3sc.insert(0, "80")
    
    Label(self, text = "").grid(row = 4, column = 6)
    self.txtCT3s = Entry(self)
    self.txtCT3s.grid(row = 4, column = 7)
    self.txtCT3s.insert(0, "80")
  
    Label(self, text = "").grid(row = 4, column = 8)
    self.txtCT3h = Entry(self)
    self.txtCT3h.grid(row = 4, column = 9)
    self.txtCT3h.insert(0, "80")
    
    Label(self, text = "").grid(row = 4, column = 10)
    self.txtCT3it = Entry(self)
    self.txtCT3it.grid(row = 4, column = 11)
    self.txtCT3it.insert(0, "80")
  
    
  def addExams(self):
    """ add exam elements """
    Label(self, text = "Final Exam",
          font = self.headerFont, ).grid(row = 5, columnspan = 3)

    Label(self, text = "").grid(row = 6, column = 0)
    self.txtFEe = Entry(self)
    self.txtFEe.grid(row = 6, column = 1)
    self.txtFEe.insert(0, "80")

    Label(self, text = "").grid(row = 6, column = 2)
    self.txtFEMat = Entry(self)
    self.txtFEMat.grid(row = 6, column = 3)
    self.txtFEMat.insert(0, "80")

    Label(self, text = "").grid(row = 6, column = 4)
    self.txtFEsc = Entry(self)
    self.txtFEsc.grid(row = 6, column = 5)
    self.txtFEsc.insert(0, "80")

    Label(self, text = "").grid(row = 6, column = 6)
    self.txtFEs = Entry(self)
    self.txtFEs.grid(row = 6, column = 7)
    self.txtFEs.insert(0, "80")

    Label(self, text = "").grid(row = 6, column = 8)
    self.txtFEh = Entry(self)
    self.txtFEh.grid(row = 6, column = 9)
    self.txtFEh.insert(0, "80")

    Label(self, text = "").grid(row = 6, column = 10)
    self.txtFEit = Entry(self)
    self.txtFEit.grid(row = 6, column = 11)
    self.txtFEit.insert(0, "80")

        #_____________SE___________
    Label(self, text = "Subject Enrichment + Notebook",
          font = self.headerFont, anchor='n').grid(row = 8, columnspan = 2)
    
    Label(self, text = "").grid(row = 9, column = 0)
    self.txtSEe = Entry(self)
    self.txtSEe.grid(row = 9, column = 1)
    self.txtSEe.insert(0, "10")

    Label(self, text = "").grid(row = 9, column = 2)
    self.txtSEMat = Entry(self)
    self.txtSEMat.grid(row=9, column = 3)
    self.txtSEMat.insert(0, "10")

    Label(self, text = "").grid(row = 9, column = 4)
    self.txtSEsc = Entry(self)
    self.txtSEsc.grid(row = 9, column = 5)
    self.txtSEsc.insert(0, "10")

    Label(self, text = "").grid(row = 9, column = 6)
    self.txtSEs = Entry(self)
    self.txtSEs.grid(row = 9, column = 7)
    self.txtSEs.insert(0, "10")

    Label(self, text = "").grid(row = 9, column = 8)
    self.txtSEh = Entry(self)
    self.txtSEh.grid(row = 9, column = 9)
    self.txtSEh.insert(0, "10")

    Label(self, text = "").grid(row = 9, column = 10)
    self.txtSEit = Entry(self)
    self.txtSEit.grid(row = 9, column = 11)
    self.txtSEit.insert(0, "10")


  def addOutput(self):
    """ add button and output elements """
    self.btnCalc = Button(self, text = "Calculate", command=self.calculate ,activebackground='Cyan', bd=10, relief=RIDGE)
    self.btnCalc.grid(row = 11, column = 5)
    self.bind('<Return>', self.calculate)
    
    #_________CT_____________  
    Label(self, text = "CT Weightage", font=self.otherFont).grid(row = 12, column = 0)
    self.lblCTe = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTe.grid(row = 12, column = 1, sticky = "we")

    Label(self, text = "").grid(row = 12, column = 2)
    self.lblCTMat = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTMat.grid(row = 12, column = 3, sticky = "we")

    Label(self, text = "").grid(row = 12, column = 4)
    self.lblCTsc = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTsc.grid(row = 12, column = 5, sticky = "we")

    Label(self, text = "").grid(row = 12, column = 6)
    self.lblCTs = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTs.grid(row = 12, column = 7, sticky = "we")

    Label(self, text = "").grid(row = 12, column = 8)
    self.lblCTh = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTh.grid(row = 12, column = 9, sticky = "we")

    Label(self, text = "").grid(row = 12, column = 10)
    self.lblCTit = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblCTit.grid(row = 12, column = 11, sticky = "we")



        #_________Total of Every Subject_____________  
    Label(self, text = "Total", font=self.otherFont).grid(row = 13, column = 0)
    self.lblTe = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTe.grid(row = 13, column = 1, sticky = "we")

    Label(self, text = "").grid(row = 13, column = 2)
    self.lblTMat = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTMat.grid(row = 13, column = 3, sticky = "we")

    Label(self, text = "").grid(row = 13, column = 4)
    self.lblTsc = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTsc.grid(row = 13, column = 5, sticky = "we")

    Label(self, text = "").grid(row = 13, column = 6)
    self.lblTs = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTs.grid(row = 13, column = 7, sticky = "we")

    Label(self, text = "").grid(row = 13, column = 8)
    self.lblTh = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTh.grid(row = 13, column = 9, sticky = "we")

    Label(self, text = "").grid(row = 13, column = 10)
    self.lblTit = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTit.grid(row = 13, column = 11, sticky = "we")
    
    #__________________OVERALLLL_________
    Label(self, text = "Overall Percent",
      font = self.headerFont).grid(row = 14, column = 5)
    self.lblTotal = Label(self, bg = "#fff", anchor = "w", relief = "groove")
    self.lblTotal.grid(row = 15, column =5, sticky = "we")
    
  def calculate(self, event=None):
    """ calculate the grades """
    #_____________LIST__FOR__AVG_______________
    e = [(math.ceil((int(self.txtCT1e.get()))/5)), (math.ceil((int(self.txtCT2e.get()))/8)), (math.ceil((int(self.txtCT3e.get()))/8))]
    Mat = [(math.ceil((int(self.txtCT1Mat.get()))/5)), (math.ceil((int(self.txtCT2Mat.get()))/8)), (math.ceil((int(self.txtCT3Mat.get()))/8))]
    sc= [(math.ceil((int(self.txtCT1sc.get()))/5)), (math.ceil((int(self.txtCT2sc.get()))/8)), (math.ceil((int(self.txtCT3sc.get()))/8))]
    s= [(math.ceil((int(self.txtCT1s.get()))/5)), (math.ceil((int(self.txtCT2s.get()))/8)), (math.ceil((int(self.txtCT3s.get()))/8))]
    h= [(math.ceil((float(self.txtCT1h.get()))/5)), (math.ceil((float(self.txtCT2h.get()))/8)), (math.ceil((float(self.txtCT3h.get()))/8))]
    it=[(math.ceil((int(self.txtCT1it.get()))/5)), (math.ceil((int(self.txtCT2it.get()))/8)), (math.ceil((int(self.txtCT3it.get()))/8))]
    
  #______________AVG_BEST_OUT_OF_TWO_______
    self.lblCTe["text"] = ((heapq.nlargest(2, e))[1] + (heapq.nlargest(2, e))[0])/2
    self.lblCTMat["text"] =((heapq.nlargest(2, Mat))[1] + (heapq.nlargest(2, Mat))[0])/2
    self.lblCTsc["text"]=((heapq.nlargest(2, sc))[1] + (heapq.nlargest(2, sc))[0])/2
    self.lblCTs["text"] =((heapq.nlargest(2, s))[1] + (heapq.nlargest(2, s))[0])/2
    self.lblCTh["text"] = ((heapq.nlargest(2, h))[1] + (heapq.nlargest(2, h))[0])/2
    self.lblCTit["text"] =((heapq.nlargest(2, it))[1] + (heapq.nlargest(2, it))[0])/2

    
    #_________________Subjectwise___TOTAL
    #Eng
    self.lblTe["text"] = (((heapq.nlargest(2, e))[1] + (heapq.nlargest(2, e))[0])/2)+(int(self.txtFEe.get()))+ (int(self.txtSEe.get()))
    e = (((heapq.nlargest(2, e))[1] + (heapq.nlargest(2, e))[0])/2)+(int(self.txtFEe.get()))+ (int(self.txtSEe.get()))
    #Mat
    self.lblTMat["text"] = (((heapq.nlargest(2, Mat))[1] + (heapq.nlargest(2, Mat))[0])/2)+(int(self.txtFEMat.get()))+ (int(self.txtSEMat.get()))
    m = (((heapq.nlargest(2, Mat))[1] + (heapq.nlargest(2, Mat))[0])/2)+(int(self.txtFEMat.get()))+ (int(self.txtSEMat.get()))
    #Science
    self.lblTsc["text"]= (((heapq.nlargest(2, sc))[1] + (heapq.nlargest(2, sc))[0])/2)+(int(self.txtFEsc.get()))+ (int(self.txtSEsc.get()))
    sc = (((heapq.nlargest(2, sc))[1] + (heapq.nlargest(2, sc))[0])/2)+(int(self.txtFEsc.get()))+ (int(self.txtSEsc.get()))
    #SST
    self.lblTs["text"] = (((heapq.nlargest(2, s))[1] + (heapq.nlargest(2, s))[0])/2)+(int(self.txtFEs.get()))+ (int(self.txtSEs.get()))
    s =  (((heapq.nlargest(2, s))[1] + (heapq.nlargest(2, s))[0])/2)+(int(self.txtFEs.get()))+ (int(self.txtSEs.get()))
    #Hindi
    self.lblTh["text"] = (((heapq.nlargest(2, h))[1] + (heapq.nlargest(2, h))[0])/2)+(int(self.txtFEh.get()))+ (int(self.txtSEh.get()))
    h = (((heapq.nlargest(2, h))[1] + (heapq.nlargest(2, h))[0])/2)+(int(self.txtFEh.get()))+ (int(self.txtSEh.get()))
    #FIT
    self.lblTit["text"] = ((((heapq.nlargest(2, it))[1] + (heapq.nlargest(2, it))[0])/2)+(int(self.txtFEit.get()))+ (int(self.txtSEit.get())))
    it = ((((heapq.nlargest(2, it))[1] + (heapq.nlargest(2, it))[0])/2)+(int(self.txtFEit.get()))+ (int(self.txtSEit.get())))

    #________________OveraLLLLL_____________
    total = (e+m+sc+s+h+it)/6
    self.lblTotal["text"] = "%.2f" % total

    #_________PLOTINGGG_________
    means_CT1 = ((int(self.txtCT1e.get()))*2, (int(self.txtCT1Mat.get()))*2, (int(self.txtCT1sc.get()))*2, (int(self.txtCT1s.get()))*2,(int(self.txtCT1h.get()))*2,(int(self.txtCT1it.get()))*2)
    means_CT2 = ((int(self.txtCT2e.get()))*1.25,(int(self.txtCT2Mat.get()))*1.25,(int(self.txtCT2sc.get()))*1.25,(int(self.txtCT2s.get()))*1.25,(int(self.txtCT2h.get()))*1.25,(int(self.txtCT2it.get()))*1.25)
    means_CT3 = ((int(self.txtCT3e.get()))*1.25,(int(self.txtCT3Mat.get()))*1.25,(int(self.txtCT3sc.get()))*1.25,(int(self.txtCT3s.get()))*1.25,(int(self.txtCT3h.get()))*1.25,(int(self.txtCT3it.get()))*1.25)
    means_FE = ((int(self.txtFEe.get()))*1.25,(int(self.txtFEMat.get()))*1.25,(int(self.txtFEsc.get()))*1.25,(int(self.txtFEs.get()))*1.25,(int(self.txtFEh.get()))*1.25,(int(self.txtFEit.get()))*1.25)


    if total == 100:
      Min_val=85
    else:
      Min_val=min(min(means_CT1), min(means_CT2), min(means_CT3), min(means_FE ))-3

    n_groups = 6 
    fig, ax = plt.subplots(num=None, figsize=(11, 8), dpi=80, facecolor='w', edgecolor='b')
    fig.canvas.set_window_title('Graph')
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8
     
    rects1 = plt.bar(index, means_CT1, bar_width,
                     alpha=opacity,
                     color='#1b0193',
                     label='CT 1')
     
    rects2 = plt.bar(index+bar_width , means_CT2, bar_width,
                     alpha=opacity,
                     color='#4823ef',
                     label='CT 2')

    rects3 = plt.bar(index+bar_width+bar_width, means_CT3, bar_width,
                     alpha=opacity,
                     color='#0272e2',
                     label='CT 3')

    rects4 = plt.bar(index+bar_width+bar_width+bar_width , means_FE, bar_width,
                     alpha=opacity,
                     color='#09e4ef',
                     label='Final')
    
    axes = plt.gca()
    axes.set_ylim([Min_val,101])
    plt.xlabel('Test')
    plt.ylabel('Scores')
    plt.title('')
    plt.xticks(index + bar_width, ('English', 'Maths', 'Science', 'Social Science', 'Hindi', 'FIT'))
    plt.legend()
    plt.tight_layout()
    plt.show()
    
def main():
  app = App()
  app.mainloop()
  
if __name__ == "__main__":
  main()
