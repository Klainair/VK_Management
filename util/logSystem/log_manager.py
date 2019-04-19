from colorama import init, Fore, Back, Style

class Log_manager:
    @staticmethod
    def initialize(output_file="/logfiles/log.txt"):
        # Метод для colorama
        init()

        # TODO: Добавить создание/перезапись лог-файла

    @staticmethod
    def info(self, message="Не задано сообщение", color=Fore.WHITE):
        print(color + message)
        self.reset_style()

    @staticmethod
    def errors(self, message="Не задано сообщение", color=Fore.RED):
        print(color + message)
        self.reset_style()
        
    @staticmethod
    def reset_style():
        print(Style.RESET_ALL)