from pyfiglet import figlet_format
from functions_and_menus import clearsc, main_menu
import keyboard
import time

clearsc()
print(figlet_format("          HardOrganizer", font="slant", justify="center"))
print("     Presione <S> para iniciar la aplicacion.")
while True:
    if keyboard.read_key() == "s":
        time.sleep(1)
        clearsc()
        break
main_menu()