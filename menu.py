#####################<WE ARE GLITCH SQUAD>#########################

#Our application module import for link each file together
import database
import main_function as main

# import module desigen and style text and animetions
from rich import*


#This is main menu        
def main_menu():

    text = str('''
===============================================::::::</>::::::=====================================
  ***              
                         ____            __           __     ____            __    __  ::::       
        ___==___        / __ )__  ______/ /___ ____  / /_   / __ \____  ____/ /___/ /___ _
       [________]      / __  / / / / __  / __ `/ _ \/ __/  / /_/ / __ \/ __  / __  / __ `/
       ] ()  () [     / /_/ / /_/ / /_/ / /_/ /  __/ /_   / ____/ /_/ / /_/ / /_/ / /_/ /
     ___\______/___  /_____/\__,_/\__,_/\__, /\___/\__/  /_/    \____/\__,_/\__,_/\__,_/ 
     +++++++++++++                     /____/                   ©</Glitch Squad>    
                    +++                                                     :::      
===================================================================================================         

    [1] - Mobile Plans
    [2] - View Packages
    [3] - USSD Codes & Hot-lines
    [4] - About Us
    [5] - Exit

==========================================================================
''')
    main.anime(text,0.0009)
 

############## Mobile Plans Menu ################
def mobile_plans():
    print('''[#ff5b5b]
....................................................................
          
        █▄ ▄█ ▄▀▄ ██▄ █ █   ██▀   █▀▄ █   ▄▀▄ █▄ █ ▄▀▀
        █ ▀ █ ▀▄▀ █▄█ █ █▄▄ █▄▄   █▀  █▄▄ █▀█ █ ▀█ ▄██

....................................................................[/#ff5b5b]
          
    [1] - SLT Mobitel
    [2] - Dialog
    [3] - Airtel 
    [4] - Hutch
    [0] - Back to Main Menu
       
[white]...................................................[/white]
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice : "))

            if u_input == 1:
                #user input get 1 :: show mobitel sub menu
                mobitel_sub()
            elif u_input == 2:
                #user input get 2 :: show mobitel sub menu
                dialog_sub()
            elif u_input == 3:
                #user input get 3 :: show mobitel sub menu
                airtel_sub()     
            elif u_input == 4:
                #user input get 4 :: show mobitel sub menu
                hutch_sub()
            elif u_input == 0:
                #close mobile plan menu (while loop is break)
                break
            else:
                #user input the numeric values [this part can be error handling]
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            #user input the char values [this part can be error handling]
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue


##############view packages##################
def viwe_packages():
    print('''[#ff5b5b]
....................................................................
          
         █ █ █ ██▀ █   █   █▀▄ ▄▀▄ ▄▀▀ █▄▀ ▄▀▄ ▄▀  ██▀ ▄▀▀
         ▀▄▀ █ █▄▄ ▀▄▀▄▀   █▀  █▀█ ▀▄▄ █ █ █▀█ ▀▄█ █▄▄ ▄██

....................................................................[/#ff5b5b]
          
    [1] - SLT Mobitel
    [2] - Dialog
    [3] - Airtel 
    [4] - Hutch
    [0] - Back to Main Menu
       
[white]...................................................[/white]
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice : "))
            main.process_bar()

            if u_input == 1:
                price = 5000 #price for pass suggest_packeg function for paramitrs (5000 pass for show all valus)

                standed = database.mobitel['Stanted']
                time_base = database.mobitel['time base']
                unlimited_s_m = database.mobitel['unlimited s_m']
                daily = database.mobitel['Daily Renewal']
                w_l = database.mobitel['W&L']
                unlimited = database.mobitel['Unlimited Plans']

                print('''[#19B2F9]
..................................................................
          
             __   ___                    
            (_ |   |  __ [#28D853]|\/| _ |_ o|_ _ |[/#28D853]
            __)|__ |     [#28D853]|  |(_)|_)||_(-`|[/#28D853]
                                        
..................................................................[/#19B2F9]''')


                print(" ")
                print("[#F8C471]===================::::Stanted::::===================[/#F8C471]")
                main.suggest_packeg(standed,price)
                print('')
                print('')

                print("[#F8C471]==================:::Timebased:::===================[/#F8C471]")
                main.suggest_packeg(time_base,price)
                print('')
                print('')

                print("[#F8C471]==========::::Unlimited Social Media::::============[/#F8C471]")
                main.suggest_packeg(unlimited_s_m,price)
                print('')
                print('')

                print("[#F8C471]===============::::Daily Renewal::::================[/#F8C471]")
                main.suggest_packeg(daily,price)
                print('')
                print('')

                print("[#F8C471]===============::::Work & learn::::=================[/#F8C471]")
                main.suggest_packeg(w_l,price)
                print('')
                print('')

                print("[#F8C471]================::::Unlimited::::===================[/#F8C471]")
                main.suggest_packeg(unlimited,price)



            elif u_input == 2:
                price = 5000
                data = database.dialog["Data_Packages"]

                anytime = data["Anytime"]
                timebase = data["Timebased"]
                work_learn = data["Work & learn"]
                nighttime = data["NightTime"]
                rental_packs = data["Rental Packs"]
                unlimited = data["Unlimited"]
                internet_cards = data["Internet Cards"]
                social_media = data["Social Media"]
                voice_addon = database.dialog["Voice_add-on"]
                combo_packages = database.dialog["Combo_Packages"]

                print('''[bold][#ee161f]
.......................................[/#ee161f]
[#fab31a]             __            
            |  \o _ | _  _ 
            |__/|(_||(_)(_)
                        _/   [/#fab31a]
[#ee161f].......................................[/#ee161f][/bold]''')


                print(" ")
                print("[#F8C471]===================::::Anytime::::===================[/#F8C471]")
                main.suggest_packeg(anytime,price)
                print('')
                print('')

                print("[#F8C471]==================:::Timebased:::===================[/#F8C471]")
                main.suggest_packeg(timebase,price)
                print('')
                print('')

                print("[#F8C471]==============::::Work & learn::::==================[/#F8C471]")
                main.suggest_packeg(work_learn,price)
                print('')
                print('')

                print("[#F8C471]================::::NightTime::::===================[/#F8C471]")
                main.suggest_packeg(nighttime,price)
                print('')
                print('')

                print("[#F8C471]===============::::Rental Packs::::=================[/#F8C471]")
                main.suggest_packeg(rental_packs,price)
                print('')
                print('')

                print("[#F8C471]================::::Unlimited::::===================[/#F8C471]")
                main.suggest_packeg(unlimited,price)
                print('')
                print('')

                print("[#F8C471]==============::::Internet Cards::::================[/#F8C471]")
                main.suggest_packeg(internet_cards,price)
                print('')
                print('')

                print("[#F8C471]===============::::Social Media::::=================[/#F8C471]")
                main.suggest_packeg(social_media,price)
                print('')
                print('')

                print("[#F8C471]==============::::Voice_add-on::::================[/#F8C471]")
                main.suggest_packeg(voice_addon,price)
                print('')
                print('')

                print("[#F8C471]==============::::Combo_Packages::::================[/#F8C471]")
                main.suggest_packeg(combo_packages,price)



            elif u_input == 3:
                price = 5000
                package_freedom= database.airtel["Freedom_Packages"]
                package_topup= database.airtel["4G_Data_Top-up"]
                package_other= database.airtel["Other Packs"]

                print('''[bold][#fe0000]
...........................................[/#fe0000]
   [white]            
             /\ o _|_ _ |  
            /--\|| |_(-`|  
                         [/white]
[#fe0000]...........................................[/#fe0000][/bold]''')
                      
                print(" ")
                print("[#F8C471]===================::::Freedom_Packages::::===================[/#F8C471]")
                main.suggest_packeg(package_freedom,price)
                print('')
                print('')

                print("[#F8C471]==================:::4G_Data_Top-up:::===================[/#F8C471]")
                main.suggest_packeg(package_topup,price)
                print('')
                print('')

                print("[#F8C471]==========::::Other Packs::::============[/#F8C471]")
                main.suggest_packeg(package_other,price)



            elif u_input == 4:
                price = 5000
                data = database.hutch['Data package']
                data1 = database.hutch['Voice & Combo Packages']
                w_l = data1["Work & Learn From Home"]
                non_stop = data1["Non-Stop Social Meadia"]
                any_ney_call = data1["Unlimited Any Net Calls"]


                anytime = data['Anytime']
                l_v_plans = data["Long Validity Plans"]
                unlimited_gamer = data["Ultimate Gamer"]
                unlimited_download = data["Ultimate Downloader"]

                print('''[bold][white]
.........................................[/white]
  [#ff6e3c]             
            |__|   |_ _ |_ 
            |  ||_||_(_ | )
                        [/#ff6e3c]
[white].........................................[/white][/bold]''')


                print(" ")
                print("[#F8C471]===================::::Anytime::::===================[/#F8C471]")
                main.suggest_packeg(anytime,price)
                print('')
                print('')

                print("[#F8C471]==============:::Long Validity Plans:::==============[/#F8C471]")
                main.suggest_packeg(l_v_plans,price)
                print('')
                print('')

                print("[#F8C471]==============::::Ultimate Gamer::::=================[/#F8C471]")
                main.suggest_packeg(unlimited_gamer,price)
                print('')
                print('')

                print("[#F8C471]============::::Ultimate Downloader::::==============[/#F8C471]")
                main.suggest_packeg(unlimited_download,price)
                print('')
                print('')

                print("[#F8C471]============::::Work & Learn From Home::::==========[/#F8C471]")
                main.suggest_packeg(w_l,price)
                print('')
                print('')

                print("[#F8C471]=============:::Non-Stop Social Meadia:::===========[/#F8C471]")
                main.suggest_packeg(non_stop,price)
                print('')
                print('')

                print("[#F8C471]===========::::Unlimited Any Net Calls::::==========[/#F8C471]")
                main.suggest_packeg(any_ney_call,price)


            elif u_input == 0:
                break
            else:
                #user input the numeric values [this part can be error handling]
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            #user input the char values [this part can be error handling]
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue


############## Mobitel Sub Menu #############
def mobitel_sub():
    print('''[#19B2F9]
..................................................................
          
             __   ___                    
            (_ |   |  __ [#28D853]|\/| _ |_ o|_ _ |[/#28D853]
            __)|__ |     [#28D853]|  |(_)|_)||_(-`|[/#28D853]
                                        
..................................................................[/#19B2F9]

        [1] - Daily Renewal
        [2] - Standards
        [3] - Unlimited Social Media
        [4] - Work & Learn
        [5] - Time Based
        [6] - Unlimited
        [0] - Back To Main Menu

[white]..................................................................[/white]
''')
    
    while True:
        try:
            u_input = int(input("Enter the number for your choice :"))

            if u_input == 1:
                package_list= database.mobitel['Daily Renewal']
                price = main.u_input()#get user value
                print("------------------------------------")
                main.suggest_packeg(package_list,price)#pass price in function
                main.back_to_main()

            elif u_input == 2:
                package_list= database.mobitel['Stanted']
                price = main.u_input()
                print("------------------------------------")
                main.suggest_packeg(package_list,price)
                main.back_to_main()

            elif u_input == 3:
                package_list= database.mobitel['unlimited s_m']
                price = main.u_input()
                print("------------------------------------")
                main.suggest_packeg(package_list,price)
                main.back_to_main()   

            elif u_input == 4:
                package_list= database.mobitel['W&L']
                price = main.u_input()
                print("------------------------------------")
                main.suggest_packeg(package_list,price)
                main.back_to_main()

            elif u_input == 5:
                package_list= database.mobitel['time base']
                price = main.u_input()
                print("------------------------------------")
                main.suggest_packeg(package_list,price)
                main.back_to_main()

            elif u_input == 6:
                package_list= database.mobitel['Unlimited Plans']
                price = main.u_input()
                print("------------------------------------")
                main.suggest_packeg(package_list,price)
                main.back_to_main()

            elif u_input == 0:
                mobile_plans()
                break
                
            else:
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue



############## Dialog Sub Menu ##############
def dialog_sub():
    print('''[bold][#ee161f]
.......................................[/#ee161f]
[#fab31a]             __            
            |  \o _ | _  _ 
            |__/|(_||(_)(_)
                        _/   [/#fab31a]
[#ee161f].......................................[/#ee161f][/bold]

        [1] - Data Packages
        [2] - Voice add-on
        [3] - Combo Packages
        [0] - Back To Main Menu
          
[white].......................................[/white]
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice :"))

            if u_input == 1:
                price = main.u_input()
                data = database.dialog["Data_Packages"]

                anytime = data["Anytime"]
                timebase = data["Timebased"]
                work_learn = data["Work & learn"]
                nighttime = data["NightTime"]
                rental_packs = data["Rental Packs"]
                unlimited = data["Unlimited"]
                internet_cards = data["Internet Cards"]
                social_media = data["Social Media"]

                print(" ")
                print("[#F8C471]===================::::Anytime::::===================[/#F8C471]")
                main.suggest_packeg(anytime,price)
                print('')
                print('')

                print("[#F8C471]==================:::Timebased:::===================[/#F8C471]")
                main.suggest_packeg(timebase,price)
                print('')
                print('')

                print("[#F8C471]==============::::Work & learn::::==================[/#F8C471]")
                main.suggest_packeg(work_learn,price)
                print('')
                print('')

                print("[#F8C471]================::::NightTime::::===================[/#F8C471]")
                main.suggest_packeg(nighttime,price)
                print('')
                print('')

                print("[#F8C471]===============::::Rental Packs::::=================[/#F8C471]")
                main.suggest_packeg(rental_packs,price)
                print('')
                print('')

                print("[#F8C471]================::::Unlimited::::===================[/#F8C471]")
                main.suggest_packeg(unlimited,price)
                print('')
                print('')

                print("[#F8C471]==============::::Internet Cards::::================[/#F8C471]")
                main.suggest_packeg(internet_cards,price)
                print('')
                print('')

                print("[#F8C471]===============::::Social Media::::=================[/#F8C471]")
                main.suggest_packeg(social_media,price)
                

            elif u_input == 2:
                price = main.u_input()
                voice_addon = database.dialog["Voice_add-on"]
                main.suggest_packeg(voice_addon, price)

            elif u_input == 3:
                price = main.u_input()
                combo_packages = database.dialog["Combo_Packages"]
                main.suggest_packeg(combo_packages, price)

            elif u_input == 0:
                mobile_plans()
                break
                
            else:
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue



############## Airtel Sub Menu ##############
def airtel_sub():
    print('''[bold][#fe0000]
...........................................[/#fe0000]
   [white]            
             /\ o _|_ _ |  
            /--\|| |_(-`|  
                         [/white]
[#fe0000]...........................................[/#fe0000][/bold]
          
        [1] - Freedom Packages ( Included Freedom - Lite )
        [2] - 4G Data Top-up
        [3] - Other Packs
        [0] - Back To Main Menu

[white]..................................................[/white]
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice :"))

            if u_input == 1:
                package_list= database.airtel["Freedom_Packages"]
                price = main.u_input()
                main.suggest_packeg(package_list,price)

            elif u_input == 2:
                package_list= database.airtel["4G_Data_Top-up"]
                price = main.u_input()
                main.suggest_packeg(package_list,price)

            elif u_input == 3:
                package_list= database.airtel["Other Packs"]
                price = main.u_input()
                main.suggest_packeg(package_list,price) 

            elif u_input == 0:
                mobile_plans()
                break
                
            else:
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue


############# Hutch Sub Menu ###############
def hutch_sub():
    print('''[bold][white]
.........................................[/white]
  [#ff6e3c]             
            |__|   |_ _ |_ 
            |  ||_||_(_ | )
                        [/#ff6e3c]
[white].........................................[/white][/bold]

        [1] - Data Packages
        [2] - Voice & Combo Packages
        [0] - Back to Main Menu
          
[white].........................................[/white]
''')
    while True:
        try:
            u_input = int(input("Enter the number for your choice :"))

            if u_input == 1:
                price = main.u_input()
                data = database.hutch['Data package']

                anytime = data['Anytime']
                l_v_plans = data["Long Validity Plans"]
                unlimited_gamer = data["Ultimate Gamer"]
                unlimited_download = data["Ultimate Downloader"]

                print(" ")
                print("[#F8C471]===================::::Anytime::::===================[/#F8C471]")
                main.suggest_packeg(anytime,price)
                print('')
                print('')

                print("[#F8C471]==============:::Long Validity Plans:::==============[/#F8C471]")
                main.suggest_packeg(l_v_plans,price)
                print('')
                print('')

                print("[#F8C471]==============::::Ultimate Gamer::::=================[/#F8C471]")
                main.suggest_packeg(unlimited_gamer,price)
                print('')
                print('')

                print("[#F8C471]============::::Ultimate Downloader::::==============[/#F8C471]")
                main.suggest_packeg(unlimited_download,price)
                

            elif u_input == 2:
                price = main.u_input()
                data = database.hutch['Voice & Combo Packages']

                w_l = data["Work & Learn From Home"]
                non_stop = data["Non-Stop Social Meadia"]
                any_ney_call = data["Unlimited Any Net Calls"]

                print(" ")
                print("[#F8C471]============::::Work & Learn From Home::::==========[/#F8C471]")
                main.suggest_packeg(w_l,price)
                print('')
                print('')

                print("[#F8C471]=============:::Non-Stop Social Meadia:::===========[/#F8C471]")
                main.suggest_packeg(non_stop,price)
                print('')
                print('')

                print("[#F8C471]===========::::Unlimited Any Net Calls::::==========[/#F8C471]")
                main.suggest_packeg(any_ney_call,price)


            elif u_input == 0:
                mobile_plans()
                break
                
            else:
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue


def ussd_submenu():
    print('''[#ff5b5b]
.................................................................................
          
  █ █ ▄▀▀ ▄▀▀ █▀▄   ▄▀▀ ▄▀▄ █▀▄ ██▀ ▄▀▀        █▄█ ▄▀▄ ▀█▀   █   █ █▄ █ ██▀ ▄▀▀
  ▀▄█ ▄██ ▄██ █▄▀   ▀▄▄ ▀▄▀ █▄▀ █▄▄ ▄██   ▀▀   █ █ ▀▄▀  █    █▄▄ █ █ ▀█ █▄▄ ▄██

.................................................................................[/#ff5b5b]

          [1] - SLT-Mobitel
          [2] - Dialog
          [3] - Airtel
          [4] - Hutch
          [0] - Back to Main Menu

[white]...................................................[/white]
''')
        
    while True:
        try:
            u_input = int(input("Enter the number for your choice :"))

            if u_input == 1:
                mobitel_ussd()
            elif u_input == 2:
                dialog_ussd()
            elif u_input == 3:
                airtel_ussd()     
            elif u_input == 4:
                hutch_ussd()
            elif u_input == 0:
                break
            else:
                print("[red]Invalid input.Please Enter Valid Number.[/red]")
                
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue

########  ABout Us  #######
def about():
    
    print('''[#00ff92] 
                         
        |=================================== < We Are > ======================================|
        |         ___   _     _         _            ___                         _            |
        |        (  _ \(_ ) _( )_      ( )          (  _ \                      ( )           |
        |        | ( (_)| |(_)  _)  ___| |__  ______| (_(_)  _ _ _   _   _ _   _| |           |  
        |        | | __ | || | |  / ___)  _  \______)\__ \ / _  ) ) ( )/ _  )/ _  |           |  
        |        | |(_ )| || | |_( (___| | | |      ( )_) | (_) | (_) | (_| | (_| |           |
        |        (____/(___)_)\__)\____)_) (_)       \____)\__  |\___/ \__ _)\__ _)           | 
        |                                                    | |                              |
        |                                                    (_)                              |
        |================================== < Developers > ===================================|
        |                                                                                     |       
        |                                                                                     | 
        |                                                                                     |      
        |        </> Umesh (TraKa) - The Front-End Magician:[Leader]                          |
        |            - Umesh crafts interfaces and solves design challenges,                  |
        |            making websites and apps shine.                                          |
        |                                                                                     |  
        |                                                                                     |  
        |        </> Sudeera (Sudda) - The Back-End Wizard:                                   |
        |            - Sudeera powers the behind-the-scenes magic, making smooth              |
        |            operations and functionality.                                            |
        |                                                                                     |  
        |                                                                                     |                  
        |        </> Nimuthu (PP) - The Front-End Helper:                                     |    
        |            - Nimuthu brings designs to life and keeps us updated with the           |
        |            latest tech trends, making sure everything runs seamlessly.              |
        |                                                                                     |                  
        |                                                                                     |              
        |                                                                                     |              
        |=====================================================================================|
        |            Together, we are the Glitch Squad, reshaping industry                    |
        |            learning through our unique skills and teamwork.                         |
        |=====================================================================================|
        |               _____ _                 _       _     _               _               |
        |              (_   _) )               ( )     ( )   ( )             ( )              |
        |                | | | |__    _ _  ___ | |/ )   \ \_/ /   _   _   _  | |              |
        |                | | |  _  \/ _  )  _  \   (      \ /   / _ \( ) ( ) | |              |
        |                | | | | | | (_| | ( ) | |\ \     | |  ( (_) ) (_) | (_)              |  
        |                (_) (_) (_)\__ _)_) (_)_) (_)    (_)   \___/ \___/                   |
        |                                                                    (_)              |                                                            
        |=====================================================================================|                                                        

[/#00ff92] ''')
    

    
##########  Exit  ##########
def m_exit():
    text = str('''
          
=============================================================================================
   ▄███▄███▄                                                                     ▄███▄███▄
   █████████   ▀█▀ █▄█ ▄▀▄ █▄ █ █▄▀ ▄▀▀   █▀ ▄▀▄ █▀▄   █ █ ▄▀▀ █ █▄ █ ▄▀    █    █████████
    ▀█████▀     █  █ █ █▀█ █ ▀█ █ █ ▄██   █▀ ▀▄▀ █▀▄   ▀▄█ ▄██ █ █ ▀█ ▀▄█   ▄     ▀█████▀
      ▀█▀                                                                           ▀█▀
=============================================================================================
''')
    
    main.anime(text,0.005)
    

##########  Mobitel Ussd  #########
def mobitel_ussd():
    print('''[#19B2F9]
..................................................................
          
             __   ___                    
            (_ |   |  __ [#28D853]|\/| _ |_ o|_ _ |[/#28D853]
            __)|__ |     [#28D853]|  |(_)|_)||_(-`|[/#28D853]
                                        
..................................................................[/#19B2F9]
                                        
        </> Mobitel PIN Registration Portal
            #171#

        </> Mobitel Self Care Information Portal
            #888# 

        </> Self Care Billing Information Portal (IVR)
            1456 

        </> Self Care Billing Information Portal ( USSD )
            #1456# 

        </> Instant Usage Alert ( SMS )
            4567 

        </> Mobitel Store Locator
            #138# 

        </> Registration Information
            *132# 

        </> Change Language on Customer Support IVR
            1717

        </> Balance ( Prepaid )
            *100# 
            141
          
        </> Balance ( Postpaid )
            # 

        </> Reload card 
            *102*cardNumber#
                SMS PIN to 141

        </> Customer care 
        141 or 1717 or 0712755777
          
        ........................................
          
''')


########## Dialog USSD  #######
def dialog_ussd():
    print('''[bold][#ee161f]
.......................................[/#ee161f]
[#fab31a]             __            
            |  \o _ | _  _ 
            |__/|(_||(_)(_)
                        _/   [/#fab31a]
[#ee161f].......................................[/#ee161f][/bold]

        </> Check Balance
            #456#  

        </> Top Up Card
            #123#PIN#  

        </> Credit Loan/Data Loan/Gift Credit/EZ Cash/Call Me Req
            #356# 

        </> EZ Cash
            #111# 

        </> Mobile Broadband / Data Packege Activation / Data Balance
            #678#   

        </> Roaming
            #103#  

        </> Mobile Insurance/Wi-Fi Calling/Subscribed Services/My Bill and Share Credit/Call Management
            #107# 

        </> IDD / Call Management/News and Information/Entertainment/Rewards and Loyalty
            #107#   

        </> MyDialog Offers
            #107*12*7# 

        </> Sim Owernership
            #132# 

        </> Star Points
            #141#
          
        .............................
''')



########## Airtel USSD  #########
def airtel_ussd():
    print('''[bold][#fe0000]
...........................................[/#fe0000]
   [white]            
             /\ o _|_ _ |  
            /--\|| |_(-`|  
                         [/white]
[#fe0000]...........................................[/#fe0000][/bold]
                

        </> Airtel Customer Care Number
            121     

        </> Airtel Complaint Number
            198
        
        </> Airtel Balance Check
            *123# 

        </> Check for Free 2G Data Balance
            *123*10# or *123*# 

        </> Check for 3G Data Balance
            *123*11# 

        </> Check for Airtel 4G Balance
            *123*11# 

        </> Airtel Night Data Balance
            *123*197# 

        </> Check for  Local SMS Balance
            *123*2# or *555# 

        </> DND Activation/Deactivation
            1909

        </> Airtel Loan Number
            *141*10# or 52141

        </> My Airtel, My Offer
            *121#
                
        </> Airtel Value Added Services
            *121*4#
                
        </> To Check Last 5 Transactions and also Value Added Services.
            *121*7#
                
        </> Check for Airtel to Airtel Mins Balance
            *123*1#
                
        </> Local Airtel to Airtel Night Minutes Balance
            *123*6#
                
        </> Check for Free Local, STD SMS Balance
            *123*7# 
            
        </> Check for Free STD Minutes Balance
            *123*8# 
                       
        </> Airtel Talk time Gift Service [Share or Ask Talk time ]
            *141#
                
        </> Airtel 3g activation USSD code
            SMS 3G to 121
                       
        </> Special 5 Offers
            *222#
                       
        </> Airtel Live Services
            *321#
                
        </> Free Facebook Access [Rs. 1 per day ]
            *325#
                
        </> Twitter Service
            *515#               

        </> Airtel Special Offers and Rewards
            *566#
                
        </> GPRS(Activation/Deactivation)
            *567#

        </> Hello Tunes Menu
            *678#
                
        </> Missed Call Alert
            *888#
                
        </> Local National SMS Packs
            *777#
                
        </> Know Your own Airtel number
            *282#      

        </> Airtel loan code
            *141*10#

        </> Mobile number portability
            SMS PORT to 1909

        </> Start any service
            SMS START to 121 

        </> Stop any service
            SMS STOP to 121

        </> Check 2G/3G balance
            SMS Data USE to 121

        </> Check unbilled amount
            SMS UNB to 121

        </> Outstanding amount
            SMS OT to 121

        </> Current bill plan
            SMS BP to 121

        </> Bill summary
            SMS BILL to 121

        </> Last 3 bill payment details
            SMS PAY to 121

        </> Contests
            543217
        
        .............................
''')



#########  Hutch USSD  ###########
def hutch_ussd():
    print('''[bold][white]
.........................................[/white]
  [#ff6e3c]             
            |__|   |_ _ |_ 
            |  ||_||_(_ | )
                        [/#ff6e3c]
[white].........................................[/white][/bold]

    </> hutch Reload Code
        *355# PIN # 

    </> hutch Check Balance code
        *344# 

    </> hutch Check Balance  ( Postpaid) code
        *444# 

    </> Data Packs ,Call Packs, SMS code
        *123#  

    </> Promotional SMS code
        *123# 

    </>   Sim Owner , internet Settings, VAS code
        *123#

    </> Postpaid Service code
        *444# 

    </> Hutch Offers code
        *101# 

    </> Internet Service code
        *131# 

    </> Hutch Loan Code
        *288# 

    </> Hutch Free Data code
        *400# 

    </> Free Services code
        *101# 

    </> Free SMS code
        *222#
    
    .............................

''')

























