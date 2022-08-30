import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import DISABLED
from tkinter import messagebox
import numpy as np
import numpy_financial as npf
import os
import sys

root=Tk()
root.title("Coursework 1 - Maryam Gadiali")
root.attributes('-topmost', True)
root.lift()
root.attributes('-topmost', False)
root.configure(bg="#dcfcfc")

w=380
h=300

ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()

x=(ws/2)-(w/2) 
y=(hs/2)-(h/2)-50
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

global count
count=0

def ProfitabilitySelections(num, loopButton, error):
    global RatioSelectionButton
    global ResetWindowButton
    global GrossProfitVar
    global SalesVar
    global SalesVar2
    global SalesVar3
    global count
    global top
    if num == 1:
        RatioSelectionButton.config(state='disabled', text="Successfully Selected")
    if count==0:
        top=Toplevel()
        count+=1
        root.attributes('-topmost', False)
        top.attributes('-topmost', True)
        top.attributes('-topmost', False)
        top.configure(bg="#dcfcfc")
        top.lift()
    else:
        loopButton.destroy()
        error.destroy()
        
    def reset():
        
        os.execl(sys.executable, sys.executable, *sys.argv)
    restartButton=Button(top, text='Return to Tab 1', command=reset)
    restartButton.pack()
    
    frame=LabelFrame(top, text='Input', padx=5, pady=5, bg="#dcfcfc") 
    frame.pack(side=LEFT)
    resultFrame=LabelFrame(top, text='Output', padx=5, pady=5, bg="#FCFCDC")
    resultFrame.pack(side=RIGHT)
   
####################################Gross Margin Formula########################################################################################
    if GrossMargin.get()==1:
        myLabel=Label(frame, text="Gross margin variables:").pack() 
        firstEquationLabel=Label(frame, text="Enter the Gross Profit").pack()
        e1= Entry(frame, width=50, bg="white", borderwidth=20)
        e1.pack()
        secondEquationLabel=Label(frame, text="Enter the Sales Value").pack()
        e2= Entry(frame, width=50, bg="white", borderwidth=20)
        e2.pack()
        def secondClick1(num):
            if num==1:
                SalesVar.config(state='disabled', text="Gross Profit Values Entered")
                def GrossProfitCalculation(num):
                    if num==1:
                        GrossProfitCalculationButton.destroy()
                    GrossProfit=float(e1.get())/float(e2.get())
                    GrossProfit=GrossProfit*100
                    GrossProfitAnswerLabel=Label(resultFrame,text="Gross Profit : " + str("{:.2f}".format(GrossProfit))+"%")
                    GrossProfitAnswerLabel.pack()

                try:
                    float(e1.get())
                    float(e2.get())
                    if ((float(e1.get())) != 0) and ((float(e2.get()))!= 0):
                        GrossProfitCalculationButton=Button(resultFrame, text="Display Gross Profit Result", command=lambda:GrossProfitCalculation(1))
                        GrossProfitCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        SalesVar=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick1(1)) #step4
        SalesVar.pack()
       
####################################Operating Margin Formula#######################################################################################################

    if OperatingMargin.get()==1:
        myLabel=Label(frame, text="Operating margin variables:").pack()
        firstEquationLabel2=Label(frame, text="Enter the Operating Profit").pack()
        e3= Entry(frame, width=50, bg="white", borderwidth=20)
        e3.pack()
        secondEquationLabel=Label(frame, text="Enter the Sales Value").pack()
        e4= Entry(frame, width=50, bg="white", borderwidth=20)
        e4.pack()
        def secondClick2(num):
            if num==1:
                SalesVar2.config(state='disabled', text="Operating Profit Values Entered")
                def OperatingProfitCalculation(num):
                    if num==1:
                        OperatingProfitCalculationButton.config(state='disabled', text="Calculated Operating Profit")
                        OperatingProfitCalculationButton.destroy()
                    OperatingProfit=float(e3.get())/float(e4.get())
                    OperatingProfit=OperatingProfit*100
                    OperatingProfitAnswerLabel=Label(resultFrame,text="Operating Profit : "+ str("{:.2f}".format(OperatingProfit))+"%")
                    OperatingProfitAnswerLabel.pack()

                try:
                    float(e3.get())
                    float(e4.get())
                    if ((float(e3.get())) != 0) and ((float(e4.get()))!= 0):
                        OperatingProfitCalculationButton=Button(resultFrame, text="Display Operating Profit Result", command=lambda:OperatingProfitCalculation(1))
                        OperatingProfitCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        SalesVar2=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick2(1)) 
        SalesVar2.pack()
      


########################################### Net Profit Formula ######################################################################################################
    if NetProfitMargin.get()==1:
        myLabel=Label(frame, text="Net margin variables:").pack() #step 1 works
        firstEquationLabel3=Label(frame, text="Enter the Net Profit").pack()
        e5= Entry(frame, width=50, bg="white", borderwidth=20)
        e5.pack()
        secondEquationLabel2=Label(frame, text="Enter the Sales Value").pack()
        e6= Entry(frame, width=50, bg="white", borderwidth=20)
        e6.pack()
        def secondClick3(num):
            if num==1:
                SalesVar3.config(state='disabled', text="Net Profit Values Entered")
                def NetProfitCalculation(num):
                    if num==1:
                        NetProfitCalculationButton.destroy()
                    NetProfit=float(e5.get())/float(e6.get())
                    NetProfit=NetProfit*100
                    NetProfitAnswerLabel=Label(resultFrame,text="Net Profit : "+ str("{:.2f}".format(NetProfit))+"%")
                    NetProfitAnswerLabel.pack()

                try:
                    float(e5.get())
                    float(e6.get())
                    if ((float(e5.get())) != 0) and ((float(e6.get()))!= 0):
                        NetProfitCalculationButton=Button(resultFrame, text="Display Net Profit Result", command=lambda:NetProfitCalculation(1))
                        NetProfitCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:ProfitabilitySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        SalesVar3=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick3(1)) 
        SalesVar3.pack()
       
#################################################################################################################################     

def LiquiditySelections(num, loopButton, error):
    global count
    global top
    if num == 1:
        RatioSelectionButton.config(state='disabled', text="Successfully Selected")
    if count==0:
        top=Toplevel()
        count+=1
        root.attributes('-topmost', False)
        top.attributes('-topmost', True)
        top.attributes('-topmost', False)
        top.configure(bg="#dcfcfc")
        top.lift()
    else:
        loopButton.destroy()
        error.destroy()
        
    def reset():
        os.execl(sys.executable, sys.executable, *sys.argv)
    
    restartButton=Button(top, text='Return to Tab 1', command=reset)
    restartButton.pack()
    
    frame=LabelFrame(top, text='Input', padx=5, pady=5, bg="#dcfcfc") 
    frame.pack(side=LEFT)
    resultFrame=LabelFrame(top, text='Output', padx=5, pady=5, bg="#FCFCDC") 
    resultFrame.pack(side=RIGHT)

################################Current Ratio ###########################################################################################################################
    if CurrentRatio.get()==1:
        myLabel=Label(frame, text="Current Ratio Variables:").pack() 
        firstEquationLabel4=Label(frame, text="Enter the Current Assets").pack()
        e1= Entry(frame, width=50, bg="white", borderwidth=20)
        e1.pack()
        secondEquationLabel3=Label(frame, text="Enter the Current Liabilities").pack()
        e2= Entry(frame, width=50, bg="white", borderwidth=20)
        e2.pack()
        def secondClick1(num):
            if num==1:
                finaliseVar.config(state='disabled', text="Current Ratio Values Entered")
                def CurrentRatioCalculation(num):
                    if num==1:
                        CurrentRatioCalculationButton.destroy()
                    CurrentRatio=float(e1.get())/float(e2.get())
                    CurrentRatioAnswerLabel=Label(resultFrame,text="Current Ratio = " + str("{:.2f}".format(CurrentRatio)))
                    CurrentRatioAnswerLabel.pack()

                try:
                    float(e1.get())
                    float(e2.get())
                    if ((float(e1.get())) != 0) and ((float(e2.get()))!= 0):
                        CurrentRatioCalculationButton=Button(resultFrame, text="Display the Current Ratio", command=lambda:CurrentRatioCalculation(1))
                        CurrentRatioCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick1(1)) 
        finaliseVar.pack()
       
########################################Quick Ratio ########################################################################################################

    if QuickRatio.get()==1:
        myLabel=Label(frame, text="Quick Ratio variables:").pack()
        firstEquationLabel5=Label(frame, text="Enter the Current Assets").pack()
        e3= Entry(frame, width=50, bg="white", borderwidth=20)
        e3.pack()
        secondEquationLabel5=Label(frame, text="Enter the Current Liabilities").pack()
        e4= Entry(frame, width=50, bg="white", borderwidth=20)
        e4.pack()
        thirdEquationLabel5=Label(frame, text="Enter the Inventory Value").pack()
        e4b= Entry(frame, width=50, bg="white", borderwidth=20)
        e4b.pack()
        def secondClick2(num):
            if num==1:
                finaliseVar2.config(state='disabled', text="Quick Ratio Values Entered")
                def QuickRatioCalculation(num):
                    if num==1:
                        QuickRatioCalculationButton.config(state='disabled', text="Calculated Quick Ratio")
                        QuickRatioCalculationButton.destroy()
                    QuickRatio=(float(e3.get())-float(e4b.get()))/(float(e4.get()))
                    QuickRatioAnswerLabel=Label(resultFrame,text="Quick Ratio : "+ str("{:.2f}".format(QuickRatio)))
                    QuickRatioAnswerLabel.pack()

                try:
                    float(e3.get())
                    float(e4.get())
                    float(e4b.get())
                    if ((float(e3.get())) != 0) and ((float(e4.get()))!= 0) and ((float(e4b.get()))!= 0):
                        QuickRatioCalculationButton=Button(resultFrame, text="Display Quick Ratio Result", command=lambda:QuickRatioCalculation(1))
                        QuickRatioCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar2=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick2(1)) 
        finaliseVar2.pack()
        

#################################### Cash Ratio ##############################################################################################################################
    if CashRatio.get()==1:
        myLabel=Label(frame, text="Cash Ratio variables:").pack()
        firstEquationLabel6=Label(frame, text="Enter the Cash Value").pack()
        e5= Entry(frame, width=50, bg="white", borderwidth=20)
        e5.pack()
        secondEquationLabel6=Label(frame, text="Enter the Current Liabilities").pack()
        e6= Entry(frame, width=50, bg="white", borderwidth=20)
        e6.pack()
        def secondClick3(num):
            if num==1:
                finaliseVar3.config(state='disabled', text="Cash Ratio Values Entered")
                def CashRatioCalculation(num):
                    if num==1:
                        CashRatioCalculationButton.destroy()
                    CashRatio=float(e5.get())/float(e6.get())
                    CashRatioAnswerLabel=Label(resultFrame,text="Cash Ratio : "+ str("{:.2f}".format(CashRatio)))
                    CashRatioAnswerLabel.pack()

                try:
                    float(e5.get())
                    float(e6.get())
                    if ((float(e5.get())) != 0) and ((float(e6.get()))!= 0):
                        CashRatioCalculationButton=Button(resultFrame, text="Display Cash Ratio Result", command=lambda:CashRatioCalculation(1))
                        CashRatioCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:LiquiditySelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar3=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick3(1)) 
        finaliseVar3.pack()
       


###################################################################################################################################################

def LeverageSelections(num, loopButton, error):
    global top
    global count
    if num == 1:
        RatioSelectionButton.config(state='disabled', text="Successfully Selected")
    if count==0:
        top=Toplevel()
        count+=1
        root.attributes('-topmost', False)
        top.attributes('-topmost', True)
        top.attributes('-topmost', False)
        top.configure(bg="#dcfcfc")
        top.lift()
    else:
        loopButton.destroy()
        error.destroy()
        
    def reset():
        os.execl(sys.executable, sys.executable, *sys.argv)
    restartButton=Button(top, text='Return to Tab 1', command=reset)
    restartButton.pack()
    
    frame=LabelFrame(top, text='Input', padx=5, pady=5, bg="#dcfcfc") #padding inside of the frame
    frame.pack(side=LEFT)
    resultFrame=LabelFrame(top, text='Output', padx=5, pady=5, bg="#FCFCDC") #padding inside of the frame
    resultFrame.pack(side=RIGHT)
   


############################### Debt to Equity #######################################################################################################################################
    if DebtToEquityRatio.get()==1:
        myLabel=Label(frame, text="Debt-To-Equity Variables:").pack()
        firstEquationLabel7=Label(frame, text="Enter the Total Debt Value").pack()
        e1= Entry(frame, width=50, bg="white", borderwidth=20)
        e1.pack()
        secondEquationLabel7=Label(frame, text="Enter the Total Equity Value").pack()
        e2= Entry(frame, width=50, bg="white", borderwidth=20)
        e2.pack()
        def secondClick1(num):
            if num==1:
                finaliseVar.config(state='disabled', text="Debt-To-Equity Values Entered")
                def DebtToEquityCalculation(num):
                    if num==1:
                        DebtToEquityCalculationButton.destroy()
                    DebtToEquity=float(e1.get())/float(e2.get())
                    DebtToEquityAnswerLabel=Label(resultFrame,text="Debt-To-Equity Ratio = " + str("{:.2f}".format(DebtToEquity)))
                    DebtToEquityAnswerLabel.pack()

                try:
                    float(e1.get())
                    float(e2.get())
                    if ((float(e1.get())) != 0) and ((float(e2.get()))!= 0):
                        DebtToEquityCalculationButton=Button(resultFrame, text="Display the Debt-To-Equity", command=lambda:DebtToEquityCalculation(1))
                        DebtToEquityCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:LeverageSelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:LeverageSelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick1(1)) #step4
        finaliseVar.pack()
        



############################### Debt to Capital ############################################################################################################################

    if DebtToCapitalRatio.get()==1:
        myLabel=Label(frame, text="Debt-To-Capital variables:").pack()
        firstEquationLabel8=Label(frame, text="Enter the Total Debt Value").pack()
        e3= Entry(frame, width=50, bg="white", borderwidth=20)
        e3.pack()
        secondEquationLabel8=Label(frame, text="Enter the Total Equity Value").pack()
        e4= Entry(frame, width=50, bg="white", borderwidth=20)
        e4.pack()
        def secondClick2(num):
            if num==1:
                finaliseVar2.config(state='disabled', text="Debt-To-Capital Values Entered")
                def DebtToCapitalCalculation(num):
                    if num==1:
                        DebtToCapitalCalculationButton.config(state='disabled', text="Calculated Debt-To-Capital")
                        DebtToCapitalCalculationButton.destroy()
                    DebtToCapital=float(e3.get())/(float(e4.get())+float(e3.get()))
                    DebtToCapitalAnswerLabel=Label(resultFrame,text="Debt-To-Capital Ratio: "+ str("{:.2f}".format(DebtToCapital)))
                    DebtToCapitalAnswerLabel.pack()

                try:
                    float(e3.get())
                    float(e4.get())
                    if ((float(e3.get())) != 0) and ((float(e4.get()))!= 0):
                        DebtToCapitalCalculationButton=Button(resultFrame, text="Display Debt-To-Capital Result", command=lambda:DebtToCapitalCalculation(1))
                        DebtToCapitalCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:LeverageSelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:LeverageSelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar2=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick2(1)) 
        finaliseVar2.pack()
       


#############################################################################################################################################################

def OperatingSelections(num, loopButton, error):
    global count
    global top
    if num == 1:
        RatioSelectionButton.config(state='disabled', text="Successfully Selected")
    if count==0:
        top=Toplevel()
        count+=1
        root.attributes('-topmost', False)
        top.attributes('-topmost', True)
        top.attributes('-topmost', False)
        top.configure(bg="#dcfcfc")
        top.lift()
    else:
        loopButton.destroy()
        error.destroy()
        
    def reset():
        os.execl(sys.executable, sys.executable, *sys.argv)
    restartButton=Button(top, text='Return to Tab 1', command=reset)
    restartButton.pack()
    
    frame=LabelFrame(top, text='Input', padx=5, pady=5, bg="#dcfcfc")
    frame.pack(side=LEFT)
    resultFrame=LabelFrame(top, text='Output', padx=5, pady=5, bg="#FCFCDC")
    resultFrame.pack(side=RIGHT)
  


########################## Return on equity #######################################################################################################################################

    if ReturnOnEquityRatio.get()==1:
        myLabel=Label(frame, text="Return-On-Equity Variables:").pack()
        firstEquationLabel9=Label(frame, text="Enter the Net Income Value").pack()
        e1= Entry(frame, width=50, bg="white", borderwidth=20)
        e1.pack()
        secondEquationLabel9=Label(frame, text="Enter the Book Value of Equity").pack()
        e2= Entry(frame, width=50, bg="white", borderwidth=20)
        e2.pack()
        def secondClick1(num):
            if num==1:
                finaliseVar.config(state='disabled', text="Return-On-Equity Values Entered")
                def ReturnOnEquityCalculation(num):
                    if num==1:
                        ReturnOnEquityCalculationButton.destroy()
                    ReturnOnEquity=float(e1.get())/float(e2.get())
                    ReturnOnEquityAnswerLabel=Label(resultFrame,text="Return-On-Equity Ratio = " + str("{:.2f}".format(ReturnOnEquity)))
                    ReturnOnEquityAnswerLabel.pack()

                try:
                    float(e1.get())
                    float(e2.get())
                    if ((float(e1.get())) != 0) and ((float(e2.get()))!= 0):
                        ReturnOnEquityCalculationButton=Button(resultFrame, text="Display the Return-On-Equity", command=lambda:ReturnOnEquityCalculation(1))
                        ReturnOnEquityCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:OperatingSelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:OperatingSelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick1(1)) 
        finaliseVar.pack()
        



############################Return on Assets ###############################################################################################################################

    if ReturnOnAssetsRatio.get()==1:
        myLabel=Label(frame, text="Return-On-Assets variables:").pack()
        firstEquationLabel10=Label(frame, text="Enter the Net Income").pack()
        e3= Entry(frame, width=50, bg="white", borderwidth=20)
        e3.pack()
        secondEquationLabel10=Label(frame, text="Enter the Total Assets Value").pack()
        e4= Entry(frame, width=50, bg="white", borderwidth=20)
        e4.pack()
        def secondClick2(num):
            if num==1:
                finaliseVar2.config(state='disabled', text="Return-On-Assets Values Entered")
                def ReturnOnAssetsCalculation(num):
                    if num==1:
                        ReturnOnAssetsCalculationButton.config(state='disabled', text="Calculated Return-On-Assets")
                        ReturnOnAssetsCalculationButton.destroy()
                    ReturnOnAssets=float(e3.get())/float(e4.get())
                    ReturnOnAssetsAnswerLabel=Label(resultFrame,text="Return-On-Assets Ratio : "+ str("{:.2f}".format(ReturnOnAssets)))
                    ReturnOnAssetsAnswerLabel.pack()

                try:
                    float(e3.get())
                    float(e4.get())
                    if ((float(e3.get())) != 0) and ((float(e4.get()))!= 0):
                        ReturnOnAssetsCalculationButton=Button(resultFrame, text="Display Return-On-Assets Result", command=lambda:ReturnOnAssetsCalculation(1))
                        ReturnOnAssetsCalculationButton.pack()
                    else:
                        def popup():
                            response = messagebox.showerror('ValueError', 'Enter a valid number!')
                            frame.destroy()
                            resultFrame.destroy()
                            restartButton.destroy()
                            top.lift()
                        ResetWindowButton=Button(top, text="Reset Window", command=lambda:OperatingSelections(1, ResetWindowButton, error))
                        ResetWindowButton.pack()
                        error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                        error.pack()
                        error.after(5, popup)
                        
                    
                except ValueError:
                    def popup():
                        response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal!')
                        frame.destroy()
                        resultFrame.destroy()
                        restartButton.destroy()
                        top.lift()
                    ResetWindowButton=Button(top, text="Reset Window", command=lambda:OperatingSelections(1, ResetWindowButton, error))
                    ResetWindowButton.pack()
                    error=Label(top, text='CLICK HERE TO RESET THE WINDOW!')
                    error.pack()
                    error.after(5, popup)
        finaliseVar2=Button(frame, text="Click here when both numbers have been entered", command=lambda: secondClick2(1)) 
        finaliseVar2.pack()
        

def optionTypeResponses(num):
    global RatioTypesButtonSelection
    global RatioSelectionButton
    if num == 1:
        RatioTypesButtonSelection.config(state='disabled', text="Successfully Selected")
    if selectedOption.get()=="Profitability":
        RatioCalcLabel=Label(root, text="Select which ratio(s) you want to calculate").grid(row=3, column=1)
        global GrossMargin
        global OperatingMargin
        global NetProfitMargin
        GrossMargin=IntVar() 
        OperatingMargin=IntVar()
        NetProfitMargin=IntVar()
        FirstOption=Checkbutton(root, text="Gross Margin", variable=GrossMargin)
        FirstOption.grid(row=4, column=1)
        SecondOption=Checkbutton(root, text="Operating Margin", variable=OperatingMargin)
        SecondOption.grid(row=5, column=1)
        ThirdOption=Checkbutton(root, text="Net Profit Margin", variable=NetProfitMargin)
        ThirdOption.grid(row=6, column=1)
        RatioSelectionButton=Button(root, text="Show selection", command=lambda:ProfitabilitySelections(1, None, None))
        RatioSelectionButton.grid(row=7, column=1)
    if selectedOption.get()=="Liquidity":
        RatioCalcLabel=Label(root, text="Select which ratio(s) you want to calculate").grid(row=3, column=1)
        global CurrentRatio
        global QuickRatio
        global CashRatio
        CurrentRatio=IntVar() #initialises variable
        QuickRatio=IntVar()
        CashRatio=IntVar()
        FirstOption=Checkbutton(root, text="Current Ratio", variable=CurrentRatio)
        FirstOption.grid(row=4, column=1)
        SecondOption=Checkbutton(root, text="Quick Ratio", variable=QuickRatio)
        SecondOption.grid(row=5, column=1)
        ThirdOption=Checkbutton(root, text="Cash Ratio", variable=CashRatio)
        ThirdOption.grid(row=6, column=1)
        RatioSelectionButton=Button(root, text="Show selection", command=lambda:LiquiditySelections(1, None, None))
        RatioSelectionButton.grid(row=7, column=1)
    if selectedOption.get()=="Leverage":
        RatioCalcLabel=Label(root, text="Select which ratio(s) you want to calculate").grid(row=3, column=1)
        global DebtToEquityRatio
        global DebtToCapitalRatio
        DebtToEquityRatio=IntVar() #initialises variable
        DebtToCapitalRatio=IntVar()
        FirstOption=Checkbutton(root, text="DebtToEquity Ratio", variable=DebtToEquityRatio)
        FirstOption.grid(row=4, column=1)
        SecondOption=Checkbutton(root, text="DebtToCapital Ratio", variable=DebtToCapitalRatio)
        SecondOption.grid(row=5, column=1)
        RatioSelectionButton=Button(root, text="Show selection", command=lambda:LeverageSelections(1, None, None))
        RatioSelectionButton.grid(row=6, column=1)
    if selectedOption.get()=="Operating":
        RatioCalcLabel=Label(root, text="Select which ratio(s) you want to calculate").grid(row=3, column=1)
        global ReturnOnEquityRatio
        global ReturnOnAssetsRatio
        ReturnOnEquityRatio=IntVar() #initialises variable
        ReturnOnAssetsRatio=IntVar()
        FirstOption=Checkbutton(root, text="ReturnOnEquity Ratio", variable=ReturnOnEquityRatio)
        FirstOption.grid(row=4, column=1)
        SecondOption=Checkbutton(root, text="ReturnOnAssets Ratio", variable=ReturnOnAssetsRatio)
        SecondOption.grid(row=5, column=1)
        RatioSelectionButton=Button(root, text="Show selection", command=lambda:OperatingSelections(1, None, None))
        RatioSelectionButton.grid(row=6, column=1)
    
    
        
def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)
    
restartButton=Button(root, text='Reset Tab 1', command=reset)
restartButton.grid(pady=(80,0),row=0, column=1) 


def Tab2():
    for widgets in root.winfo_children():
      widgets.destroy()
    w=635
    h=650
    x=(ws/2)-(w/2)
    y=(hs/2)-(h/2)-50
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    def resetTab2():
        for widgets in root.winfo_children():
            widgets.destroy()
        Tab2()
    ResetWindowButton1=Button(root, text="Reset Tab 2", command=resetTab2)
    ResetWindowButton1.grid(row =0, column=0, columnspan=2)

   
    frame=LabelFrame(root, bg="#FCDCFC", text='Input', padx=5, pady=5) #padding inside of the frame
    frame.grid()
      
    def Tab3():
        for widgets in root.winfo_children():
            widgets.destroy()
        w=440
        h=650
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)-50
        root.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
        nextTab=Button(root, text='>>', state=DISABLED)
        nextTab.grid(row=0, column=2, sticky='e')
        lastTab=Button(root, text='<<', command=Tab2)
        lastTab.grid(row=0, column=0, sticky='w',)
        def resetTab3():
            for widgets in root.winfo_children():
                widgets.destroy()
            Tab3()
        ResetWindowButton=Button(root, text="Reset Tab 3", command=resetTab3)
        ResetWindowButton.grid(row =0, column=0)
        frame=LabelFrame(root, bg="#FCDCFC", text='Input', padx=5, pady=5) #padding inside of the frame
        frame.grid()
        myLabel=Label(frame, text="Enter the Initial Investement Value: ")
        myLabel.grid(row=1, column=0)

        IIV= Entry(frame, width=20, bg="white", borderwidth=20)
        IIV.grid(row=1, column=1)

        myLabel2=Label(frame, text="Enter the Discount Rate: ")
        myLabel2.grid(row=2, column=0) 
        DR= Entry(frame, width=20, bg="white", borderwidth=20)
        DR.grid(row=2, column=1)


        def TableFrame():
            try:
                global initialInvestment
                global discountRate
                initialInvestment=float(IIV.get())
                discountRate=float(DR.get())
    
                frame.destroy()
                w=605
                h=650
                x=(ws/2)-(w/2)
                y=(hs/2)-(h/2)-50
                root.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
                frameCover=Label(root, text='Step 1 Done', padx=5, pady=5) #padding inside of the frame
                frameCover.grid()
                
                tableFrame=LabelFrame(root, bg="#FCDCFC", text='Table Input', padx=5, pady=5) #padding inside of the frame
                tableFrame.grid()
                j=Label(tableFrame, text='Enter the information in the following grid').grid(row=0) 

                yearLabel=Label(tableFrame, text="Year")
                yearLabel.grid(row=1, column=0)
                cashOutflowLabel=Label(tableFrame, text="Cash Outflows (£)")
                cashOutflowLabel.grid(row=1, column=1)
                cashInflowLabel=Label(tableFrame, text="Cash Inflows (£)")
                cashInflowLabel.grid(row=1, column=2)

                

                year1Label=Label(tableFrame, text="1")
                year1Label.grid(row=2, column=0)
                year2Label=Label(tableFrame, text="2")
                year2Label.grid(row=3, column=0)
                year3Label=Label(tableFrame, text="3")
                year3Label.grid(row=4, column=0)
                year4Label=Label(tableFrame, text="4")
                year4Label.grid(row=5, column=0)
                year5Label=Label(tableFrame, text="5")
                year5Label.grid(row=6, column=0)

                global cashOutflow1
                global cashOutflow2
                global cashOutflow3
                global cashOutflow4
                global cashOutflow5

                global cashInflow1
                global cashInflow2
                global cashInflow3
                global cashInflow4
                global cashInflow5

                cashOutflow1=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashOutflow1.grid(row=2, column =1)
                cashOutflow2=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashOutflow2.grid(row=3, column =1)
                cashOutflow3=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashOutflow3.grid(row=4, column =1)
                cashOutflow4=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashOutflow4.grid(row=5, column =1)
                cashOutflow5=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashOutflow5.grid(row=6, column =1)

                cashInflow1=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashInflow1.grid(row=2, column =2)
                cashInflow2=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashInflow2.grid(row=3, column =2)
                cashInflow3=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashInflow3.grid(row=4, column =2)
                cashInflow4=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashInflow4.grid(row=5, column =2)
                cashInflow5=Entry(tableFrame, width=20, bg='white', borderwidth=20)
                cashInflow5.grid(row=6, column =2)

                def OptionList():
                    try:
                        acashOutflow1=float(cashOutflow1.get())
                        acashOutflow2=float(cashOutflow2.get())
                        acashOutflow3=float(cashOutflow3.get())
                        acashOutflow4=float(cashOutflow4.get())
                        acashOutflow5=float(cashOutflow5.get())
                        acashInflow1=float(cashInflow1.get())
                        acashInflow2=float(cashInflow2.get())
                        acashInflow3=float(cashInflow3.get())
                        acashInflow4=float(cashInflow4.get())
                        acashInflow5=float(cashInflow5.get())
                        acashNetFlow1=acashInflow1-acashOutflow1
                        acashNetFlow2=acashInflow2-acashOutflow2
                        acashNetFlow3=acashInflow3-acashOutflow3
                        acashNetFlow4=acashInflow4-acashOutflow4
                        acashNetFlow5=acashInflow5-acashOutflow5
                    
                        tableFrame.destroy()
                        w=295
                        h=650
                        x=(ws/2)-(w/2)
                        y=(hs/2)-(h/2)-50
                        root.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
                        tableFrameCover=Label(root, text='Step 2 Done', padx=5, pady=5) #padding inside of the frame
                        tableFrameCover.grid()
                        optionFrame=LabelFrame(root, bg="#FCDCFC", text='Option Selection', padx=5, pady=5) #padding inside of the frame
                        optionFrame.grid()
                        NPV=IntVar()
                        IRR=IntVar()
                        PP=IntVar()
                        FirstOption=Checkbutton(optionFrame, text="Net Present Value", variable=NPV)
                        FirstOption.grid()
                        SecondOption=Checkbutton(optionFrame, text="Internal Rate of Return", variable=IRR)
                        SecondOption.grid()
                        ThirdOption=Checkbutton(optionFrame, text="Payback Period", variable=PP)
                        ThirdOption.grid()
                    except ValueError:
                        response = messagebox.showerror('No or Wrong Values Entered', 'Only Enter Numbers or Decimals!\nThe Page Will Now Reset')
                        for widgets in root.winfo_children():
                            widgets.destroy()
                        Tab3()
                    def investmentCalculations(): 
                        investmentChoice.config(state='disabled', text="Formulas Chosen")
                        w=220
                        h=650
                        x=(ws/2)-(w/2)
                        y=(hs/2)-(h/2)-50
                        root.geometry('%dx%d+%d+%d' % (w, h, x, y)) 
                        if (NPV.get()!=1) and (IRR.get()!=1) and (PP.get()!=1):
                            response = messagebox.showerror('No Selection Made', 'Pick At Least One Choice\nThe Page Will Now Reset')
                            for widgets in root.winfo_children():
                                widgets.destroy()
                            Tab3()
                            
                        if NPV.get()==1:
                            rate,cashflows=(discountRate/100), [-initialInvestment,acashNetFlow1,acashNetFlow2,acashNetFlow3,acashNetFlow4,acashNetFlow5]
                            NPVresult=npf.npv(rate, cashflows).round(2)
                            NPVlabel=Label(optionFrame, text="NPV: £"+ str("{:.2f}".format(NPVresult))).grid()
                            
                        if IRR.get()==1:
                            IRRresult= round(npf.irr([-initialInvestment,acashNetFlow1,acashNetFlow2,acashNetFlow3,acashNetFlow4,acashNetFlow5]),2)
                            IRRresult=(IRRresult*100)
                            IRRlabel=Label(optionFrame, text="IRR: "+str("{:.2f}".format(IRRresult))+"%").grid()
                        if PP.get()==1:
                            cashFlowList=[acashNetFlow1,acashNetFlow2,acashNetFlow3,acashNetFlow4,acashNetFlow5]
                            cumulative=-initialInvestment
                            years=0
                            for item in cashFlowList:
                                cumulative+=item
                                years+=1
                                if cumulative==0:
                                    result=Label(optionFrame, text=str(years)+" Years").grid()
                                    break
                                if cumulative>0:
                                    years-=1
                                    cumulative-=item
                                    remainder=-cumulative
                                    fractionOf=remainder/item
                                    days=round(fractionOf*365)
                                    result=Label(optionFrame,text="Payback Period: "+str(years)+" Years, "+str(days)+" Days").grid()
                                    break
                                
                         
                    investmentChoice=Button(optionFrame, text = "Confirm which formulas you want to calculate", command=investmentCalculations)
                    investmentChoice.grid()
                optionFrameOpener=Button(tableFrame, text="Click when you have filled out all the details", command=OptionList)
                optionFrameOpener.grid()
            except ValueError:
                response = messagebox.showerror('No or Wrong Values Entered', 'Only Enter Numbers or Decimals!\nThe Page Will Now Reset')
                for widgets in root.winfo_children():
                    widgets.destroy()
                Tab3()
                
        tableFrameOpener=Button(frame, text="Click when you have entered both details in", command=TableFrame)
        tableFrameOpener.grid()
        
    nextTab=Button(root, text='>>', command=Tab3)
    nextTab.grid(row=0, column=0, sticky='e')
    lastTab=Button(root, text='<<', command=reset)
    lastTab.grid(row=0, column=0, sticky='w')
    space=Label(frame, text=' ').grid(row=2, column=0)
    myLabel=Label(frame, text="Enter your choice of amount\n(Present Value Formula - Enter the Future Amount)\n(Future Value Formula - Enter the Amount Invested)")
    myLabel.grid(row=3, column=0) 
    e1= Entry(frame, width=50, bg="white", borderwidth=20)
    e1.grid(row=3, column=1)

    myLabel2=Label(frame, text="Enter the Annual Interest Rate")
    myLabel2.grid(row=4, column=0) 
    e2= Entry(frame, width=50, bg="white", borderwidth=20)
    e2.grid(row=4, column=1)

    myLabel3=Label(frame, text="Enter the number of years")
    myLabel3.grid(row=5, column=0) 
    e3= Entry(frame, width=50, bg="white", borderwidth=20)
    e3.grid(row=5, column=1)

    def twoEquations():
        completeButton.config(state='disabled', text="All Values Entered")
        try:
            float(e1.get())
            float(e2.get())
            float(e3.get())
            amount=float(e1.get())
            interestRate=(float(e2.get()))/(100)
            period=float(e3.get())
            choiceFrame=LabelFrame(root, text='Option Choice', padx=5, pady=5) #padding inside of the frame
            choiceFrame.grid()
            def oneOptionSelection(num):
                if num==1:
                    twoformulaSelection.config(state='disabled', text="Pick an equation to calculate")
                options=[("Present Value", "Present Value"), ("Future Value", "Future Value")]
                formulas = StringVar()
                formulas.set(None)

                option1=Radiobutton(choiceFrame, text="Present Value", variable=formulas, value="Present Value")
                option1.pack()
                option2=Radiobutton(choiceFrame, text="Future Value", variable=formulas, value="Future Value")
                option2.pack()
                def clicked(formula):
                    optionChoice.config(state='disabled', text="Formula chosen")
                    resultFrame=LabelFrame(root, text='Output', padx=5, pady=5) #padding inside of the frame
                    resultFrame.grid()
                    if formula=="None":
                        response = messagebox.showerror('No Selection', 'Choose an option')
                        choiceFrame.destroy()
                        twoEquations()
                    if formula=="Present Value":
                        presentValue=(amount)/((1+(interestRate))**(period))
                        presentValueResult=Label(resultFrame, text="Present Value = £" + str("{:.2f}".format(presentValue)))
                        presentValueResult.grid()

                    if formula == "Future Value":
                        futureValue=(amount)*((1+(interestRate))**(period))
                        futureValueResult=Label(resultFrame, text="Future Value = £" + str("{:.2f}".format(futureValue)))
                        futureValueResult.grid()
                        
                optionChoice=Button(choiceFrame, text='Confirm Formula Choice', command=lambda:clicked(formulas.get()))
                optionChoice.pack()
                
                    
                
            twoformulaSelection=Button(choiceFrame, text="Open Formula Selection", command = lambda:oneOptionSelection(1)) #creates a button, where 'show' function is called
            twoformulaSelection.pack()
            
        except ValueError:
            response = messagebox.showerror('ValueError', 'Enter a Number or a Decimal! \nThis page will reset.')
            Tab2()
    
    completeButton=Button(frame, text='Click here when you have entered all three values', command=twoEquations)
    completeButton.grid(row=6, column=1)

nextTab=Button(root, text='>>', command=Tab2)
nextTab.grid(row=0, column=2, pady=(80,0), sticky='e')
lastTab=Button(root, text='<<', state=DISABLED)
lastTab.grid(row=0, column=0, pady=(80,0),sticky='w')

optionTypes=["Profitability", #Shows the 4 types of ratios available
         "Liquidity",
         "Leverage",
         "Operating"] 

selectedOption=StringVar() #initialises variable
selectedOption.set(optionTypes[0]) #Sets the initial value of choice to be the first item in list

dropMenuList=OptionMenu(root, selectedOption, *optionTypes) #sets up a drop menu in main window
dropMenuList.grid(row=1, column=1) 
RatioTypesButtonSelection=Button(root, text="Confirm selection to choose the ratios you wish to calculate", width=45, command = lambda:optionTypeResponses(1)) #creates a button, where 'show' function is called
RatioTypesButtonSelection.grid(row=2, column=1)
root.mainloop()
