from tkinter import *
import datetime
import os
from tkinter.filedialog import asksaveasfilename, askopenfilename, askopenfile
from tkinter import messagebox

# testing function to see if the initial_diameter store the e1 textbox (answer: it does store the input)
from tkinter.filedialog import asksaveasfile

#Converting Horizontal speed into Rotational speed
def calculating():
    # inital_diameter = int(e1.get())
    # inital_speed = int(e2.get())
    # Check for any invalid input such as string or character. Return as error window for user
    try:
        Diameter = float(e1.get())  # Diameter
        Ini_speed = float(e2.get())  # Initial Speed

    except ValueError:
        messagebox.showinfo("ERROR", "Please Enter a number")

    # Testing   Formula (requires actual formula later on...)
    # Formula : Diameter / 1.589  * Initial Speed = Vs
    #           Output Speed = Vd/(Vs/Vd)
    Vs = ((Diameter) / 1.589) * Ini_speed
    FinalSpeed = Ini_speed / (Vs / Ini_speed)

    # allow the output to refresh for different inputs
    e3.configure(state='normal')
    e3.delete(0, END)  # get new number every time
    e3.insert(0, round(FinalSpeed, 4))
    e3.configure(state='disabled')

# This function allow user to clear the inputs/outputs
def clear():
    e0.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.configure(state='normal')
    e3.delete(0, END)
    e3.configure(state='disabled')


def storefile():  # store converted speed into txt, uncommented commented lines to store data as CSV file
    # file_exists = os.path.isfile('cylinder_data_file.csv')
    current = datetime.datetime.now()
    header = "Part Number, Diameter(in), InitialSpeed(mm/s), FinalSpeed(mm/s), Date, Time "
    with open('cylinder_data_file.txt', mode='a',
              newline='') as cylinder_file:  # 'a' prevent overwritten the past input
        # fieldnames = ['Part number', 'Diameter(in)', 'Initial Speed(mm/s)', 'Output Speed(mm/s)', 'Date', 'Time']
        # cylinder_writer = csv.DictWriter(cylinder_file, delimiter=',', fieldnames=fieldnames)
        # cylinder_file.write(header +"\n")
        # e3.configure(state='normal')
        cylinder_file.seek(0, 2)  # will seek the next line of csv file and extract the inputs/outputs
        if cylinder_file.tell() == 0:  # if first file line --> write header
            cylinder_file.write(header + "\n")
        # cylinder_writer.writerow(
        # {'Part number': e0.get(), 'Diameter(mm)': e1.get(), 'Initial Speed(mm/s)': e2.get(), 'Output Speed(mm/s)'
        #: e3.get(), 'Date': current.strftime("%Y/%m/%d"), 'Time': current.strftime("%I:%M:%S %p")})
        cylinder_file.write(e0.get() + ",")
        cylinder_file.write(e1.get() + ",")
        cylinder_file.write(e2.get() + ",")
        cylinder_file.write(e3.get() + ",")
        cylinder_file.write(current.strftime("%Y/%m/%d") + ",")
        cylinder_file.write(current.strftime("%I:%M:%S %p") + "\n")
        e3.configure(state='disabled')


def event_on_closing():  # Events happen when close the GUI, Erase data if not save.
    if messagebox.askyesno("Quit", "Do you want to save before Exit? All contents will be erase "):  # yes option
        os.startfile('cylinder_data_file.txt', 'open')

    else:
        cylinder_file = 'cylinder_data_file.txt'
        file = open(cylinder_file, "w+")  # clear all the content of main file
        file.close()  # close the file
        master.destroy()

#SET UP the GUI
master = Tk()

master.title('EPRI_HYPER_CALCULATOR')

master.resizable(0, 0)  # does not allow calculator window resizable

Label(master, text="Part Number", font=("Helvetica", 16)).grid(row=0, column=0)  # where the part coming from
Label(master, text="Diameter(in)", font=("Helvetica", 16)).grid(row=1, column=0)
Label(master, text="Speed(mm/s)", font=("Helvetica", 16)).grid(row=3, column=0)
Label(master, text="Final Speed(mm/s)", font=("Helvetica", 16)).grid(row=4, column=0)

# store the entry of each label into variable
e0 = Entry(master, font=("Helvetica", 16))  # to record the cylindrical number
e1 = Entry(master, font=("Helvetica", 16))
e2 = Entry(master, font=("Helvetica", 16))
e3 = Entry(master, font=("Helvetica", 16))
e3.configure(state='disabled')  # Disable user input when the program starts
# e4 = Text(master, height=20, width=80) # to be edited, add a history table

# apparently increase the font size increase the text box size
# organize each entry into rows and columns

e0.grid(row=0, column=1)
e1.grid(row=1, column=1, )
e2.grid(row=3, column=1, )
e3.grid(row=4, column=1, )

# Setup the button to show the result
Button(master, text='clear', command=clear, width=15, height=1, font=("Helvetica", 16)).grid(row=5, column=0, sticky=W,
                                                                                             pady=4)
Button(master, text='Calculate', command=calculating, width=15, height=1, font=("Helvetica", 16)).grid(row=5, column=1,
                                                                                                       pady=4, sticky=W)
Button(master, text='Save Data', command=storefile, width=15, height=1, font=("Helvetica", 16)).grid(row=6, column=0,
                                                                                                     sticky=W, pady=4,
                                                                                                     columnspan=2)
master.protocol("WM_DELETE_WINDOW", event_on_closing)
mainloop()