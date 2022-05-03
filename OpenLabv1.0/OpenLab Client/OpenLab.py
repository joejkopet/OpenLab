from cProfile import label
from contextlib import nullcontext
from pickle import FALSE
from ttkbootstrap import Menu
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import socket
import subprocess
import webview
from pathlib import Path
from tkPDFViewer import tkPDFViewer as pdf
from ttkbootstrap.style import Bootstyle, Colors

#Global Variables 
global OpenLabServerIP
with open(r'config\openlabserver.cfg') as o:
    OpenLabServerIP = o.read()
global OpenLabClassName
OpenLabClassName = 'classnamehere'

LP1_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP1_2_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP2_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP2_2_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP2_3_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP2_4_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP3_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP4_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP6_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP7_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"
LP8_1_Friendly = "$FriendlyNameThatStudentsWillSeeInTheLabSubMenu"

def main_menu():
    global root
    root = ttk.Window(themename="superhero",title="OpenLab - Main Menu")
    root.geometry("1000x250")
    root.resizable(width=False, height=False)
    root.iconbitmap(r'images\openlabicon.ico')
    global LP
    LP='LP0_0'
    versionnumber = ttk.Label(root, text='v1.0 BETA')
    versionnumber.place(relx=1.0, rely=1.0, anchor='se')
    global router_image
    router_image = ttk.PhotoImage(file=r'images\router.png')
    global switch_image
    switch_image = ttk.PhotoImage(file=r'images\switch.png')
    global firewall_image
    firewall_image = ttk.PhotoImage(file=r'images\firewall.png')
    routerlabel = ttk.Label(root, text="Routers")
    routerlabel.place(x=150, y=25, anchor="center")

    switchlabel = ttk.Label(root, text="Switches")
    switchlabel.place(x=500, y=25, anchor="center")

    switchlabel = ttk.Label(root, text="Firewalls")
    switchlabel.place(x=812.50, y=25, anchor="center")


    r1 = ttk.Button(root, text="R1", bootstyle="info-outline", command=open_putty_r1, image=router_image, compound=ttk.BOTTOM)
    r1.place(x=50, y=100, anchor='center')

    r2 = ttk.Button(root, text="R2", bootstyle="info-outline", command=open_putty_r2, image=router_image, compound=ttk.BOTTOM)
    r2.place(x=150, y=100, anchor='center')

    r3 = ttk.Button(root, text="R3", bootstyle="info-outline", command=open_putty_r3, image=router_image, compound=ttk.BOTTOM)
    r3.place(x=250, y=100, anchor='center')

    s1 = ttk.Button(root, text="S1", bootstyle="info-outline", command=open_putty_s1, image=switch_image, compound=ttk.BOTTOM)
    s1.place(x=400, y=100, anchor='center')

    s2 = ttk.Button(root, text="S2", bootstyle="info-outline", command=open_putty_s2, image=switch_image, compound=ttk.BOTTOM)
    s2.place(x=500, y=100, anchor='center')

    s3 = ttk.Button(root, text="S3", bootstyle="info-outline", command=open_putty_s3, image=switch_image, compound=ttk.BOTTOM)
    s3.place(x=600, y=100, anchor='center')

    asa1 = ttk.Button(root, text="ASA Firewall #1", bootstyle="info-outline", command=open_putty_asa1, image=firewall_image, compound=ttk.BOTTOM)
    asa1.place(x=750, y=100, anchor='center')

    asa2 = ttk.Button(root, text="ASA Firewall #2", bootstyle="info-outline", command=open_putty_asa2, image=firewall_image, compound=ttk.BOTTOM)
    asa2.place(x=875, y=100, anchor='center')

    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(
        menubar,
        tearoff=0
    )



    LP1_sub_menu = Menu(file_menu, tearoff=0)
    LP1_sub_menu.add_command(label=LP1_1_Friendly, command=LP1_1)
    LP1_sub_menu.add_command(label=LP1_2_Friendly, command=LP1_2)

    LP2_sub_menu = Menu(file_menu, tearoff=0)
    LP2_sub_menu.add_command(label=LP2_1_Friendly, command=LP2_1)
    LP2_sub_menu.add_command(label=LP2_2_Friendly, command=LP2_2)
    LP2_sub_menu.add_command(label=LP2_3_Friendly, command=LP2_3)
    LP2_sub_menu.add_command(label=LP2_4_Friendly, command=LP2_4)

    LP3_sub_menu = Menu(file_menu, tearoff=0)
    LP3_sub_menu.add_command(label=LP3_1_Friendly, command=LP3_1)

    LP4_sub_menu = Menu(file_menu, tearoff=0)
    LP4_sub_menu.add_command(label=LP4_1_Friendly, command=LP4_1)


    LP5_sub_menu = Menu(file_menu, tearoff=0)
    LP5_sub_menu.add_command(label='No Labs Available')

    LP6_sub_menu = Menu(file_menu, tearoff=0)
    LP6_sub_menu.add_command(label=LP6_1_Friendly, command=LP6_1)

    LP7_sub_menu = Menu(file_menu, tearoff=0)
    LP7_sub_menu.add_command(label=LP7_1_Friendly, command=LP7_1)

    LP8_sub_menu = Menu(file_menu, tearoff=0)
    LP8_sub_menu.add_command(label=LP8_1_Friendly, command=LP8_1)

    file_menu.add_cascade(
        label="Learning Plan 1",
        menu=LP1_sub_menu
    )

    file_menu.add_cascade(
        label="Learning Plan 2",
        menu=LP2_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 3",
        menu=LP3_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 4",
        menu=LP4_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 5",
        menu=LP5_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 6",
        menu=LP6_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 7",
        menu=LP7_sub_menu
    )
    file_menu.add_cascade(
        label="Learning Plan 8",
        menu=LP8_sub_menu
    )


    file_menu.add_separator()
    file_menu.add_command(
        label='Exit',
        command=root.destroy
    )


    menubar.add_cascade(
        label="Labs",
        menu=file_menu,
        underline=0
    )

    help_menu = Menu(
        menubar,
        tearoff=0
    )

    root.mainloop()


def open_putty_s1():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\s1.cfg') as s:
        S1IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+S1IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_s2():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\s2.cfg') as s:
        S2IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+S2IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_s3():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\s3.cfg') as s:
        S3IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+S3IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_r1():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\r1.cfg') as s:
        R1IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+R1IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_r2():
    with open(r'config\student.cfg') as f:
        print(student+'-')
    with open(r'config\r2.cfg') as s:
        R2IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+R2IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_r3():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\r3.cfg') as s:
        R3IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+R3IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_asa1():
    with open(r'config\student.cfg') as f:
        print(student+'-')
    with open(r'config\asa1.cfg') as s:
        ASA1IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+ASA1IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def open_putty_asa2():
    with open(r'config\student.cfg') as f:
        student = f.read()
    with open(r'config\asa2.cfg') as s:
        ASA2IPAddress = s.read()
    cmd_args = student+'_'+LP+'@'+ASA2IPAddress
    subprocess.Popen([r"bin/putty.exe", cmd_args])
def grade_lab():
    with open(r'config\student.cfg') as f:
        student = f.read()
        student = student + "_"
        print (student)
    webview.create_window('Grade Results for '+FriendlyName, 'http://'+OpenLabServerIP+'/'+OpenLabClassName+"/"+student+LP,on_top=True)
    webview.start()
def LP_Sub_Menu_Template():
    WindowName = LP+"Window"
    WindowName = ttk.Toplevel(root)
    WindowName.title("OpenLab - "+FriendlyName)
    WindowName.geometry("1000x800")
    WindowName.resizable(width=True, height=True)
    WindowName.iconbitmap(r'images\openlabicon.ico')
    versionnumber = ttk.Label(WindowName, text='v1.0 BETA')
    versionnumber.place(relx=1.0, rely=1.0, anchor='se')
    menubar = Menu(WindowName)
    WindowName.config(menu=menubar)

    routerlabel = ttk.Label(WindowName, text="Routers")
    routerlabel.place(x=150, y=25, anchor="center")

    switchlabel = ttk.Label(WindowName, text="Switches")
    switchlabel.place(x=500, y=25, anchor="center")

    switchlabel = ttk.Label(WindowName, text="Firewalls")
    switchlabel.place(x=812.50, y=25, anchor="center")


    r1 = ttk.Button(WindowName, text="R1", bootstyle="info-outline", command=open_putty_r1, image=router_image, compound=ttk.BOTTOM)
    r1.place(x=50, y=100, anchor='center')


    r2 = ttk.Button(WindowName, text="R2", bootstyle="info-outline", command=open_putty_r2, image=router_image, compound=ttk.BOTTOM)
    r2.place(x=150, y=100, anchor='center')

    r3 = ttk.Button(WindowName, text="R3", bootstyle="info-outline", command=open_putty_r3, image=router_image, compound=ttk.BOTTOM)
    r3.place(x=250, y=100, anchor='center')

    s1 = ttk.Button(WindowName, text="S1", bootstyle="info-outline", command=open_putty_s1, image=switch_image, compound=ttk.BOTTOM)
    s1.place(x=400, y=100, anchor='center')

    s2 = ttk.Button(WindowName, text="S2", bootstyle="info-outline", command=open_putty_s2, image=switch_image, compound=ttk.BOTTOM)
    s2.place(x=500, y=100, anchor='center')

    checkresults = ttk.Button(WindowName, text="Check Results", bootstyle="info-outline", command=grade_lab, compound=ttk.BOTTOM)
    checkresults.place(x=500, y=175, anchor='center')

    s3 = ttk.Button(WindowName, text="S3", bootstyle="info-outline", command=open_putty_s3, image=switch_image, compound=ttk.BOTTOM)
    s3.place(x=600, y=100, anchor='center')

    asa1 = ttk.Button(WindowName, text="ASA Firewall #1", bootstyle="info-outline", command=open_putty_asa1, image=firewall_image, compound=ttk.BOTTOM)
    asa1.place(x=750, y=100, anchor='center')

    asa2 = ttk.Button(WindowName, text="ASA Firewall #2", bootstyle="info-outline", command=open_putty_asa2, image=firewall_image, compound=ttk.BOTTOM)
    asa2.place(x=875, y=100, anchor='center')
    PDFv1 = LP+"v1"
    global v1
    v1 = PDFv1
    PDFv2 = LP+"v2"
    global v2
    v2 = PDFv2
    v1 = pdf.ShowPdf()
    v1.img_object_li.clear()
    v2 = v1.pdf_view(WindowName,
                    pdf_location=r"labs/"+LP+'.pdf',
                    width=200, height=50, load="after")
    v2.place(x=25,y=200)
    versionnumber = ttk.Label(WindowName, text='v1.0 BETA')
    versionnumber.place(relx=1.0, rely=1.0, anchor='se')
def LP1_1():
    global LP
    LP='LP1_1'
    global FriendlyName
    FriendlyName = LP1_1_Friendly
    LP_Sub_Menu_Template()
def LP1_2():
    global LP
    LP='LP1_2'
    global FriendlyName
    FriendlyName = LP1_2_Friendly
    LP_Sub_Menu_Template()
def LP2_1():
    global LP
    LP='LP2_1'
    global FriendlyName
    FriendlyName = LP2_1_Friendly
    LP_Sub_Menu_Template()
def LP2_2():
    global LP
    LP='LP2_2'
    global FriendlyName
    FriendlyName = LP2_2_Friendly
    LP_Sub_Menu_Template()
def LP2_3():
    global LP
    LP='LP2_3'
    global FriendlyName
    FriendlyName = LP2_3_Friendly
    LP_Sub_Menu_Template()
def LP2_4():
    global LP
    LP='LP2_4'
    global FriendlyName
    FriendlyName = LP2_4_Friendly
    LP_Sub_Menu_Template()
def LP3_1():
    global LP
    LP='LP3_1'
    global FriendlyName
    FriendlyName = LP3_1_Friendly
    LP_Sub_Menu_Template()
def LP4_1():
    global LP
    LP='LP4_1'
    global FriendlyName
    FriendlyName = LP4_1_Friendly
    LP_Sub_Menu_Template()
def LP2_1():
    global LP
    LP='LP2_1'
    global FriendlyName
    FriendlyName = LP2_1_Friendly
    LP_Sub_Menu_Template()
def LP6_1():
    global LP
    LP='LP6_1'
    global FriendlyName
    FriendlyName = LP6_1_Friendly
    LP_Sub_Menu_Template()
def LP7_1():
    global LP
    LP='LP7_1'
    global FriendlyName
    FriendlyName = LP7_1_Friendly
    LP_Sub_Menu_Template()
def LP8_1():
    global LP
    LP='LP8_1'
    global FriendlyName
    FriendlyName = LP8_1_Friendly
    LP_Sub_Menu_Template()
main_menu()

#Credit
#Router Image: https://commons.wikimedia.org/wiki/File:Router_symbol-Blue.svg; Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
#Switch Image: https://commons.wikimedia.org/wiki/File:Switch_symbol-Blue.svg; Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
#Firewall Image: https://commons.wikimedia.org/wiki/File:Firewall_Symbol_-_blue.svg; Michel Bakni, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons
#Icon: <a href="https://www.flaticon.com/free-icons/server" title="server icons">Server icons created by RaftelDesign - Flaticon</a>
