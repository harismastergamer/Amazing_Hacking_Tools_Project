import tkinter as tk





def WantToLeave():
    WantToLeaveWin = tk.Tk()
    WantToLeaveWin.geometry("200x150")
    wanttoleavelabel = tk.Label(WantToLeaveWin, text="Are You Sure You Want To\nLeave?\nThis May Stop An Update\nAnd Destroy The Installation!")
    wanttoleavelabel.place(x=20, y=20)
    WantToLeaveWin.grab_set()
    yesbutton = tk.Button(WantToLeaveWin, text="Yes",command=quit)
    nobutton = tk.Button(WantToLeaveWin, text="No",command=WantToLeaveWin.destroy)
    yesbutton.place(x=150, y=120)
    nobutton.place(x=10, y=120)
    


UpdateWin = tk.Tk()
UpdateWin.geometry("300x200")
UpdateWin.title("Loading AHT")
UpdateWin.resizable(width=False, height=False)
UpdateWin.protocol("WM_DELETE_WINDOW", WantToLeave)





statuslabel = tk.Label(UpdateWin, text="Loading...", font=("Arial", 15))

statuslabel.place(relx=0.5, rely=0.2, anchor='center')


UpdateWin.mainloop()
