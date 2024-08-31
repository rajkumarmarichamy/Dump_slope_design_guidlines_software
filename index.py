from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

windows = Tk()
# windows.geometry("650x650")
windows.title("SLOPE STABILITY ANALYSIS")


def compute():
    global reseltImageViewer_label
    global deckheight
    global deckwidth
    global unitweight
    global cohesion
    global friction
    global results_1_lable
    global results_2_lable
    global results_1_entry
    global results_2_entry
    global FOSANS
    global DISANS
    global deckhet
    global deckwit
    global unitwet
    global cohe
    global fric
    global goferimage
    global reslutImageViewer_frame
    global photo

    results_1_lable.pack_forget()
    results_1_entry.pack_forget()
    results_2_lable.pack_forget()
    results_2_entry.pack_forget()
    reslutImageViewer_frame.pack_forget()

    deckheight = float(parameter_1_entry.get())
    deckwidth = float(parameter_2_entry.get())
    unitweight = float(parameter_3_entry.get())
    cohesion = float(parameter_4_entry.get())
    friction = float(parameter_5_entry.get())

    FOSANS = abs(round(0*deckheight-0.00036*(deckheight ** 2)+0.01858*deckwidth -
                 0.00015*(deckwidth ** 2)-0.01799*unitweight-0.00059*(unitweight ** 2) + 0.017347*cohesion-0.000055 * (cohesion ** 2) + 0.04025 * friction + -0.000094*(friction ** 2) - 0.12515, 2))

    DISANS = abs(round(0*deckheight+1.011217*(deckheight ** 2)-37.4136*deckwidth -
                 0.256543*(deckwidth ** 2)-70.0069*unitweight+3.357639*(unitweight ** 2) + 13.82222*cohesion-0.04174 * (cohesion ** 2) - 10.1278 * friction + -0.024444*(friction ** 2) + 905.4233, 2))
    # optimal_bench_height =  abs(round((- 1.5 +0.01858*deckwidth - 0.00015*(deckwidth ** 2)-0.01799*unitweight-0.00059*(unitweight ** 2) + 0.017347*cohesion-0.000055 * (cohesion ** 2) + 0.04025 * friction + -0.000094*(friction ** 2) - 0.12515)/16.6667, 2))
    if deckheight < 35:
        deckhet = "30"
        if deckwidth < 37.5:
            deckwit = "30"
        else:
            deckwit = "45"
    else:
        deckhet = "40"
        if deckwidth < 50:
            deckwit = "40"
        else:
            deckwit = "60"

    if unitweight < 16:
        unitwet = "14"
    elif unitweight < 18:
        unitwet = "16"
    else:
        unitwet = "18"

    if cohesion < 60:
        cohe = "40"
    elif cohesion < 80:
        cohe = "60"
    else:
        cohe = "80"

    if friction < 30:
        fric = "25"
    elif friction < 35:
        fric = "30"
    else:
        fric = "35"

    goferimage = "modelphotos/"+deckhet+deckwit+unitwet+cohe+fric+".png"
    results_1_lable = Label(
        frame_output, text="Factor of safety of the slope = ")
    results_1_lable.pack()
    results_1_entry = Label(frame_output, text=FOSANS)
    results_1_entry.pack()

    results_2_lable = Label(
        frame_output, text="Slope displacement in (mm) = ")
    results_2_lable.pack()
    results_2_entry = Label(frame_output, text=DISANS)
    results_2_entry.pack()

    reslutImageViewer_frame = LabelFrame(windows, text="")
    reslutImageViewer_frame.pack()
    photo = ImageTk.PhotoImage(Image.open(
        goferimage). resize((400, 350), Image.Palette.ADAPTIVE))
    reseltImageViewer_label = Label(reslutImageViewer_frame, image=photo)
    reseltImageViewer_label.image_names = photo
    reseltImageViewer_label.pack()


def sorcepage():
    windows.geometry("500x500")
    global paramater_1_lable
    global paramater_2_lable
    global paramater_3_lable
    global paramater_4_lable
    global paramater_5_lable
    global parameter_1_entry
    global parameter_2_entry
    global parameter_3_entry
    global parameter_4_entry
    global parameter_5_entry
    global results_1_lable
    global results_2_lable
    global results_1_entry
    global results_2_entry
    global reseltImageViewer_label
    global reslutImageViewer_frame
    global frame_input
    global frame_input1
    global frame_input2
    global frame_output

    FOSANS = 00
    DISANS = 00
    mainframe.pack_forget()
    footframe.pack_forget()

    frame_input = LabelFrame(
        windows, text="Input Parameters", bd=2)
    frame_input.pack(fill=BOTH, padx=10, pady=10)

    frame_input1 = LabelFrame(
        frame_input, text="", bd=2)
    frame_input1.grid(row=0, column=0, sticky=W, padx=70)

    frame_input2 = LabelFrame(
        frame_input, text="", bd=2)
    frame_input2.grid(row=0, column=1, sticky=E, padx=70)

    frame_output = LabelFrame(
        windows, text="Results", bd=2)
    frame_output.pack(fill=BOTH, padx=10, pady=10)

    paramater_10_lable = Label(
        frame_input1, text="Number of decks")
    paramater_10_lable.pack()
    parameter_10_entry = Entry(
        frame_input1, width=15, borderwidth=2)
    parameter_10_entry.pack()

    paramater_1_lable = Label(
        frame_input1, text="Deck Height (m)")
    paramater_1_lable.pack()
    parameter_1_entry = Entry(
        frame_input1, width=15, borderwidth=2)
    parameter_1_entry.pack()

    paramater_2_lable = Label(
        frame_input1, text="Deck Width (m)")
    paramater_2_lable.pack()
    parameter_2_entry = Entry(
        frame_input1, width=15, borderwidth=2)
    parameter_2_entry.pack()

    paramater_3_lable = Label(
        frame_input2, text="Unit density (KN/m3)")
    paramater_3_lable.pack()
    parameter_3_entry = Entry(
        frame_input2, width=15, borderwidth=2)
    parameter_3_entry.pack()

    paramater_4_lable = Label(
        frame_input2, text="Cohesion (kPa)")
    paramater_4_lable.pack()
    parameter_4_entry = Entry(frame_input2, width=15, borderwidth=2)
    parameter_4_entry.pack()

    paramater_5_lable = Label(
        frame_input2, text="Friction (degree)")
    paramater_5_lable.pack()
    parameter_5_entry = Entry(frame_input2, width=15, borderwidth=2)
    parameter_5_entry.pack()

    results_1_lable = Label(
        frame_output, text="Factor of safety of the slope = ")
    results_1_lable.pack()
    results_1_entry = Label(frame_output, text=FOSANS)
    results_1_entry.pack()

    results_2_lable = Label(
        frame_output, text="Slope displacement in (mm) = ")
    results_2_lable.pack()
    results_2_entry = Label(frame_output, text=DISANS)
    results_2_entry.pack()

    submit_paramater_button = Button(
        windows, text="Submit parameters", command=lambda: compute(), bd=2)
    submit_paramater_button.pack()

    reslutImageViewer_frame = LabelFrame(windows, text="")
    reslutImageViewer_frame.pack()


def login():

    username = username_Lable_entry.get()
    password = password_Lable_entry.get()

    # Validate the login credentials
    if username == "admin" and password == "admin":
        sorcepage()
        # Login successful

    else:
        # Login failed
        messagebox.showerror(
            "Login failed", "Invalid username or password. try again")


mainframe = LabelFrame(windows, text="", bd=2,
                       borderwidth=0, highlightthickness=0)
footframe = LabelFrame(windows, text="", bd=2,
                       borderwidth=0, highlightthickness=0)

mainframe.pack(padx=10, pady=10, fill="both", side=TOP)
footframe.pack(padx=20, pady=20)

new_pic = ImageTk.PhotoImage(Image.open(
    "inviteimage.png").resize((500, 300), Image.Palette.ADAPTIVE))

invitepicture_lable = Label(mainframe, image=new_pic)
invitepicture_lable.pack()


username_Lable = Label(footframe, text="Username :")
username_Lable_entry = Entry(footframe, width=15, borderwidth=2)
password_Lable = Label(footframe, text="password :")
password_Lable_entry = Entry(footframe, width=15, borderwidth=2)

username_Lable.grid(row=0, column=0, padx=50)
username_Lable_entry.grid(row=0, column=1)
password_Lable.grid(row=1, column=0, padx=50)
password_Lable_entry.grid(row=1, column=1)

copyright_lable = Label(
    windows, text="Copyright @ 2024, UCE(A) OU, All rights reserved")
copyright_lable.pack(side=BOTTOM)

login_button = Button(
    footframe, text="Submit", command=lambda: login(), bd=2)
login_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

windows.mainloop()
