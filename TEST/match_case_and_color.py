from colorama import init, Fore, Style   #Цвет и курсив

init(autoreset=True)

while True:
    print('\nStart Game:')
    print('1: Choose the language')
    print('2: Stop')
    print('3: Select chapter')
    print('4: Select level')
    print('5: Go to preferences')
    print('6: Exit')
    act=input('>')
    match act:
        case '1':
            print('English, Deutch, Ukrainian')
        case '2':
            print(Fore.RED + 'Stop Game' + Style.RESET_ALL )
        case '3':
            print('1, 2, 3, 4')
        case '4':
            print('first, second, third')            
        case '5':
            print('Video, audio, game settings')    
        case '6':
            print(Fore.GREEN + 'Good Bye ;)' + Style.RESET_ALL)
            break
        case _:
        	print(Fore.YELLOW + 'Dont do this' + Style.RESET_ALL)
print("\033[3mDone\033[0m") # Курсив по инит         


""" 
from colorama import init, Fore, Back, Style

init(autoreset=True)

# Жирный текст
print("\033[1mЭто жирный текст\033[0m")

# Подчеркнутый текст
print("\033[4mЭто подчеркнутый текст\033[0m")

# Мигающий текст (поддерживается не везде)
print("\033[5mЭто мигающий текст\033[0m")

# Красный текст с желтым фоном
print(Fore.RED + Back.YELLOW + "Красный текст с желтым фоном")

# Зелёный текст курсивом
print(Fore.GREEN + "\033[3mЗелёный текст курсивом\033[0m")

print("\033[5m" + Fore.RED + "Это мигающий текст, если поддерживается терминалом" + "\033[0m")

print(Fore.YELLOW + 'Dont do this' + Style.RESET_ALL) """

