from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

windows = Tk()
windows.geometry("650x650")
windows.title("TARP Guidlines")
windows.configure(background="white")


def cal(D, Y, C, F, MD, BS, SM, VB):
    global DMM
    global FOS
    global ROD
    DMM = abs(round(3.5*MD-30.6*Y+0.04*D-0.25*C-2.77*F+0.72*BS -
                    16.32, 2))
    FOS = abs(round(0.0028*C-0.0054*MD-0.0150*F -
                    0.0502*BS-0.0003*D-0.0179*Y+2.45, 2))
    ROD = abs(round(0.0822*SM+0.0946*VB-0.97851))
    results_1_lable = Label(
        frame_results, text="Slope displacement in (mm)")
    results_1_lable.grid(row=3, column=0, sticky=NSEW)
    results_1_entry = Label(frame_results, text=DMM)
    results_1_entry.grid(row=4, column=0)

    results_2_lable = Label(
        frame_results, text="Factor of safety of the slope")
    results_2_lable.grid(row=5, column=0, sticky=NSEW)
    results_2_entry = Label(frame_results, text=FOS)
    results_2_entry.grid(row=6, column=0)

    results_3_lable = Label(
        frame_results, text="Rate of displacement (mm/day)")
    results_3_lable.grid(row=1, column=0, sticky=NSEW)
    results_3_entry = Label(frame_results, text=ROD)
    results_3_entry.grid(row=2, column=0)


def compute():
    # global results_1_lable
    # global results_1_entry
    # global results_2_lable
    # global results_2_entry
    global density
    global cohesion
    global friction
    global youngs
    global mdepth
    global bslopeangle
    global soilmoisture
    global vibration

    density = float(parameter_1_entry.get())
    youngs = float(parameter_2_entry.get())
    cohesion = float(parameter_4_entry.get())
    friction = float(parameter_5_entry.get())
    mdepth = float(parameter_6_entry.get())
    bslopeangle = float(parameter_8_entry.get())
    soilmoisture = float(parameter_9_entry.get())
    vibration = float(parameter_10_entry.get())

    results_1_lable.grid_forget()
    results_1_entry.grid_forget()
    results_2_lable.grid_forget()
    results_2_entry.grid_forget()
    results_3_lable.grid_forget()
    results_3_entry.grid_forget()

    cal(density, youngs, cohesion, friction, mdepth,
        bslopeangle, soilmoisture, vibration)


def sorcepage():
    global paramater_1_lable
    global paramater_2_lable
    global paramater_3_lable
    global paramater_4_lable
    global paramater_5_lable
    global paramater_6_lable
    global paramater_8_lable
    global parameter_1_entry
    global parameter_2_entry
    global parameter_3_entry
    global parameter_4_entry
    global parameter_5_entry
    global parameter_6_entry
    global parameter_8_entry
    global parameter_9_entry
    global parameter_10_entry
    global frame_body
    global frame_results
    global frame_body_Stiffness
    global frame_body_Strength
    global frame_body_Geomentry
    global frame_body_otherparameters
    global results_1_lable
    global results_2_lable
    global results_3_lable
    global results_1_entry
    global results_2_entry
    global results_3_entry
    global frame_foot
    global foot_label
    global foot_label2
    headframe.pack_forget()
    mainframe.pack_forget()
    footframe.pack_forget()
    copyright_frame.pack_forget()
    frame_head = LabelFrame(windows, text="", bd=2)
    frame_head.pack(padx=20, pady=20, fill="both", side=TOP)
    head_lable = Label(
        frame_head, text="Advanced Real-time slope monitoring system using Internet of Things")
    head_lable.pack()
    frame_body = LabelFrame(windows, text="Bench slope parameters",
                            bd=2)
    frame_body.pack(padx=20, pady=20, fill="both", side=TOP)
    frame_results = LabelFrame(windows, text="Results", bd=2)
    frame_results.pack(padx=20, pady=20, side=TOP)
    frame_body_Stiffness = LabelFrame(frame_body, text="Stiffness",
                                      bd=2)
    frame_body_Stiffness.grid(row=0, column=1, sticky=W, padx=10,
                              pady=10)

    frame_body_Strength = LabelFrame(frame_body, text="Strength",
                                     bd=2)
    frame_body_Strength.grid(row=0, column=2, sticky=N, padx=10, pady=10)
    frame_body_Geomentry = LabelFrame(frame_body, text="Geomentry", bd=2)
    frame_body_Geomentry.grid(row=0, column=3, sticky=N, padx=10, pady=10)
    frame_body_otherparameters = LabelFrame(
        frame_body, text="Other parameters", bd=2)
    frame_body_otherparameters.grid(
        row=0, column=4, sticky=NE, padx=10, pady=10)

    paramater_1_lable = Label(
        frame_body_Stiffness, text="Input density in kg/m3")
    paramater_1_lable.pack()
    parameter_1_entry = Entry(
        frame_body_Stiffness, width=15, borderwidth=2)
    parameter_1_entry.pack()

    paramater_2_lable = Label(
        frame_body_Stiffness, text="Input Young's modulus in GPa")
    paramater_2_lable.pack()
    parameter_2_entry = Entry(
        frame_body_Stiffness, width=15, borderwidth=2)
    parameter_2_entry.pack()

    paramater_3_lable = Label(
        frame_body_Stiffness, text="Input Poisson ratio")
    paramater_3_lable.pack()
    parameter_3_entry = Entry(
        frame_body_Stiffness, width=15, borderwidth=2)
    parameter_3_entry.pack()

    paramater_4_lable = Label(
        frame_body_Strength, text="Input Cohesion in KPa")
    paramater_4_lable.pack()
    parameter_4_entry = Entry(frame_body_Strength, width=15, borderwidth=2)
    parameter_4_entry.pack()

    paramater_5_lable = Label(
        frame_body_Strength, text="Input Friction angle in degree")
    paramater_5_lable.pack()
    parameter_5_entry = Entry(frame_body_Strength, width=15, borderwidth=2)
    parameter_5_entry.pack()

    paramater_6_lable = Label(
        frame_body_Geomentry, text="Input mine depth in meter")
    paramater_6_lable.pack()
    parameter_6_entry = Entry(
        frame_body_Geomentry, width=15, borderwidth=2)
    parameter_6_entry.pack()

    paramater_8_lable = Label(
        frame_body_Geomentry, text="Input Bench slope angle in degree")
    paramater_8_lable.pack()
    parameter_8_entry = Entry(
        frame_body_Geomentry, width=15, borderwidth=2)
    parameter_8_entry.pack()

    paramater_9_lable = Label(
        frame_body_otherparameters, text="Input Soil moisture in percentage")
    paramater_9_lable.pack()
    parameter_9_entry = Entry(
        frame_body_otherparameters, width=15, borderwidth=2)
    parameter_9_entry.pack()

    paramater_10_lable = Label(
        frame_body_otherparameters, text="Input Vibration in Hertz")
    paramater_10_lable.pack()
    parameter_10_entry = Entry(
        frame_body_otherparameters, width=15, borderwidth=2)
    parameter_10_entry.pack()

    results_1_lable = Label(
        frame_results, text="Slope displacement in (mm)")
    results_1_lable.grid(row=3, column=0, sticky=NSEW)
    results_1_entry = Label(frame_results, text='00')
    results_1_entry.grid(row=4, column=0)

    results_2_lable = Label(
        frame_results, text="Factor of safety of the slope")
    results_2_lable.grid(row=5, column=0, sticky=NSEW)
    results_2_entry = Label(frame_results, text='00')
    results_2_entry.grid(row=6, column=0)

    results_3_lable = Label(
        frame_results, text="Rate of displcement (mm/day)")
    results_3_lable.grid(row=1, column=0, sticky=NSEW)
    results_3_entry = Label(frame_results, text='00')
    results_3_entry.grid(row=2, column=0)

    submit_paramater_button = Button(
        frame_body, text="Submit parameters", command=lambda: compute(), bd=2)
    submit_paramater_button.grid(
        row=1, column=2, columnspan=2, padx=10, pady=10)

    frame_foot = LabelFrame(windows, text="", bd=0)
    frame_foot.pack(padx=20, pady=20, fill="both", side=TOP)
    foot_label = Label(
        frame_foot, text="Created by").pack()
    foot_label2 = Label(
        frame_foot, text="Sathish Kumar Mittapally & Ram Chandra Karra").pack()


def login():
    windows.geometry("850x650")
    global mainframe
    global foot_label

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


headframe = LabelFrame(windows, text="", bd=2)
headframe.configure(bg="white", fg="white")
mainframe = LabelFrame(windows, text="", bd=2)
mainframe.configure(bg="white", fg="white")
footframe = LabelFrame(windows, text="login", bd=2)
copyright_frame = LabelFrame(windows, text="", bd=2)
copyright_frame.configure(bg="white", fg="white")
headframe.pack(padx=20, pady=20, fill="both", side=TOP)
mainframe.pack(padx=10, pady=10, fill="both", side=TOP)
footframe.pack(padx=20, pady=20)
copyright_frame.pack(padx=20, pady=10, fill="both")

# inviteimg = ImageTk.PhotoImage(Image.open("modelphotos/01302514.png"))
inviteimg = Image.open(
    "modelphotos/01302514.png").resize((300, 225), Image.ADAPTIVE)
new_pic = ImageTk.PhotoImage(inviteimg)
heading_Lable = Label(
    headframe, text="Advanced slope monitoring system using Internet of Things", font=("Arial", 12, "bold"))
heading_Lable.pack()

invitepicture_lable = Label(mainframe, image=new_pic)
invitepicture_lable.pack()

username_Lable = Label(footframe, text="Username")
username_Lable_entry = Entry(footframe, width=15, borderwidth=2)
password_Lable = Label(footframe, text="password")
password_Lable_entry = Entry(footframe, width=15, borderwidth=2)

username_Lable.grid(row=0, column=0, padx=50)
username_Lable_entry.grid(row=0, column=1)
password_Lable.grid(row=1, column=0, padx=50)
password_Lable_entry.grid(row=1, column=1)

copyright_lable = Label(
    copyright_frame, text="Copyright @ 2024, NITK Surathkal, All rights reserved")
copyright_lable.pack()

login_button = Button(
    footframe, text="Submit", command=lambda: login(), bd=2)
login_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

windows.mainloop()
