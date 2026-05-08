import tkinter as tk

root = tk.Tk()
root.title("My Banking App")
root.geometry("1000x500")

mainLabel = tk.Label(root,text="Welcome To Banking APP",foreground="Blue",font=("Helvetica", 24, "bold"))
mainLabel.pack()

sublabel = tk.Label(root,text="Bank registration form")
sublabel.pack()

frame = tk.Frame(root)
frame.pack()


namelable = tk.Label(frame,text="Name of bank :")
namelable.grid(column=0,row=0)
nameEntry = tk.Entry(frame)
nameEntry.grid(column=1,row=0)

contactlable = tk.Label(frame,text="contact :")
contactlable.grid(column=0,row=1)
contactEntry = tk.Entry(frame)
contactEntry.grid(column=1,row=1)

addresslable = tk.Label(frame,text="address :")
addresslable.grid(column=0,row=2)
addressText = tk.Text(frame)
addressText.grid(column=1,row=2)




root.mainloop()