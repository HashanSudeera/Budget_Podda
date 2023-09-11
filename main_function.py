#####################<WE ARE GLITCH SQUAD>#########################

#This is main function write file in our application

#import python in-build function for using time control and auto typing cli menu(create animations)
import sys
import time

#Interface color and other design (use rich module)
from rich import*
from rich.progress import track


def process_bar():
    '''Process bar function'''
    for _ in track(range(100), description='[green]Processing data'):
        time.sleep(0.01)#process bar time control

def anime(text:str,settime:float):
    '''Test Animetion function'''
    for char in text:
        sys.stdout.write(char)#type text char
        sys.stdout.flush()
        time.sleep(settime)

def continue_y_n():
    '''yes or no quection function'''

    while True:
    
        choice = input("Do you want to continue(y/n) :")

        if choice == 'y' or choice == 'Y':
            return True #return bool values
        elif choice == 'n' or choice == "N":
            return False #return bool values
        else:
            print("[red]Invalid input. Please enter 'y' or 'n' :[/red]")
            continue
    
def suggest_packeg(package:dict,price:int)->str:
    '''This function get parameters (datapackage and user budget price) output filtering data packages'''

    for i in package:
        if i >= 0 and i <= price:#compare the range for user price
            print('')
            plan = package[i]
            anime(plan+'\n',0.001)#typing animetion time
            print('------------------------------------')
        
    if price < 7:
        print(f'We have no packegs under Rs.{price}')

def u_input()-> int:
    '''Get user input return values type intiger'''
    while True:
        try:
            u_input = int(input("Enter your budget price (Rs) :"))
            process_bar()
            return u_input
        
        except ValueError:
            print("[red]Invalid input.Please Enter Valid Number.[/red]")
            continue

def back_to_main():
    '''back to main menu function'''
    while True:
        u_choice = input("[0] Back to Main menu :")

        if u_choice != '0':
            print("[red]Invalid input.Please Enter Valid Number[/red]")
            continue

        if u_choice == '0':
            break

    


