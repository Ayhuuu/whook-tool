import requests
import json
import time
import os
import sys
from colorama import *
from pystyle import *
import threading

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

                                                                     
                                                                                
                                    
            )               )       
 (  (    ( /(            ( /(  (    
 )\))(   )\())  (    (   )\()) )\   
((_)()\ ((_)\   )\   )\ ((_)\ ((_)  
_(()((_)| |(_) ((_) ((_)| |(_)|__ \ 
\ V  V /| ' \ / _ \/ _ \| / /   /_/ 
 \_/\_/ |_||_|\___/\___/|_\_\  (_)  
                                    
                                                                                
                                                                                                                                                                                                                                                                                         
        > Press Enter                                         

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


init()

intro = f"""{Fore.RED}

            )               )       
 (  (    ( /(            ( /(  (    
 )\))(   )\())  (    (   )\()) )\   
((_)()\ ((_)\   )\   )\ ((_)\ ((_)  
_(()((_)| |(_) ((_) ((_)| |(_)|__ \ 
\ V  V /| ' \ / _ \/ _ \| / /   /_/ 
 \_/\_/ |_||_|\___/\___/|_\_\  (_)  

{Fore.YELLOW}> 1 - Webhook spammer
{Fore.YELLOW}> 2 - Webhook deleter
{Fore.YELLOW}> 3 - Exit

"""

print(intro)


def send_message(webhook_url, message):
    """
    Sends messages continuously to the specified webhook URL.
    """
    while True:
        data = {
            "content": message,
            "username": "31/69",
            "avatar_url": "https://cdn.discordapp.com/attachments/1077997573702434897/1102553541081567372/a_a2fa891c3c386b45381ca8af9316fc02.gif"
        }

        json_data = json.dumps(data)

        response = requests.post(webhook_url, data=json_data, headers={"Content-Type": "application/json"})

        if response.status_code == 204:
            print(f"[+]Sent")
        else:
            print(f"[-] Rate!")
        
        
        time.sleep(1)


while True:
    choice = input(f"{Fore.RED}Enter your choice: {Fore.YELLOW}")
    if choice == "1":

        print(f"{Fore.GREEN}You have selected the webhook spammer.")
        while True:
            webhook_url = input(f"{Fore.RED}Please enter the Discord webhook URL (press q to back): {Fore.YELLOW}")
            if webhook_url == "q":
                break

            try:
                response = requests.get(webhook_url)
                if not response.ok:
                    raise ValueError("Invalid webhook URL!")
            except Exception as e:
                print(f"Invalid webhook URL! Error message: {str(e)}")
                continue

            while True:
                message = input("Please enter the message to be sent: ")
                if message == "q":
                    break

               
                threads = []
                for i in range(10):  
                    thread = threading.Thread(target=send_message, args=(webhook_url, "@everyone " + message))
                    threads.append(thread)
                    thread.start()

    elif choice == "2":

        print(f"{Fore.GREEN}You have selected the webhook deleter.")
        while True:
            webhook_url = input(f"{Fore.RED}Please enter the Discord webhook URL you want to delete (press q to back): {Fore.YELLOW}")
            if webhook_url == "q":
                break

            try:
                response = requests.head(webhook_url)
                assert response.status_code == 200
            except:
                print(f"{Fore.RED}Invalid webhook URL! Please try again.")
                continue

            response = requests.delete(webhook_url)

            if response.status_code == 204:
                print(f"{Fore.GREEN}The webhook has been successfully deleted.")
            else:
                print(f"{Fore.RED}Error deleting webhook: {response.status_code}")
    elif choice == "3":
        print("Exiting program...")
        sys.exit()
    else:
        print(f"{Fore.RED}Invalid choice! Please try again.")