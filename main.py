#####################<WE ARE GLITCH SQUAD>#########################

#Our application concept is to find the data package as much as you have

#This is main python file in our apllication
#You shoud run first menu.py 
#User for link all menus in Main menu

#Our application module import for link each file together
import menu as menu
import main_function as main

#import rich module for style text(please this module install your Pc before this code run [pip install rich])
from rich import*


while True:

    menu.main_menu()#call main menu function in menu.py
       
    try:
        u_input = int(input("Enter the number for your choice :"))

        if u_input == 1:
            menu.mobile_plans()

        elif u_input == 2:
            menu.viwe_packages()

        elif u_input == 3:
            menu.ussd_submenu() 

        elif u_input == 4:
            menu.about()
            main.back_to_main()

        elif u_input == 5:
            menu.m_exit()
            exit()
        else:
            #user input the numeric values [this part can be error handling]
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            

    except ValueError:
        #user input the char values [this part can be error handling]
        print("[red]Invalid input.Please Enter Valid Number.[/red]")
        





    
