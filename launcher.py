import phonenumbers
import time
from os import name, system
from phonenumbers import timezone, geocoder, carrier
from colorama import Fore

if name == 'nt':
	system("title PhonSearch")


def clear():
	system("cls") if name == 'nt' else system("clear")

clear()

print(Fore.LIGHTBLUE_EX + """
██╗███╗   ██╗███████╗ ██████╗ ███╗   ██╗██╗   ██╗███╗   ███╗
██║████╗  ██║██╔════╝██╔═══██╗████╗  ██║██║   ██║████╗ ████║
██║██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║██║   ██║██╔████╔██║
██║██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║██║   ██║██║╚██╔╝██║
██║██║ ╚████║██║     ╚██████╔╝██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
                                                            """)

print()
reg = input(Fore.YELLOW + "Entrer le numéro de la région > " + Fore.RESET)

num = input(Fore.YELLOW + "Entrer le numéro de téléphone > " + Fore.RESET)

clear()

N = phonenumbers.parse(reg + num)

Z = timezone.time_zones_for_number(N)

carrier = carrier.name_for_number(N, 'fr')

R = geocoder.description_for_number(N, 'fr')

time.sleep(0.5)
print(Fore.RED + str(N))
time.sleep(0.5)
print("Ville:" + str(Z))
time.sleep(0.5)
print("Service : " + carrier)
time.sleep(0.5)
print("Pay: " + R)

print()

input(Fore.YELLOW + "Appuyer 3  fois pour quitter...")
input(Fore.YELLOW + "Appuyer 2  fois pour quitter...")
input(Fore.YELLOW + "Appuyer 1  fois pour quitter...")
time.sleep(0.1)
exit()
