from colorama import init, Fore, Back, Style

class Log_manager:
    def __init__(self, output_file="/logfiles/log.txt"):
        # Метод для colorama
        init()
        
        # TODO: Добавить создание/перезапись лог-файла
        
    def info(self, message="Не задано сообщение", color=Fore.WHITE):
        print(color + message)
        self.reset_style()
    
    def errors(self, message="Не задано сообщение", color=Fore.RED):
        print(color + message)
        self.reset_style()
        
    def reset_style(self):
        print(Style.RESET_ALL)