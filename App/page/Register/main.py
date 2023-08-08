
from iback import IBackRegister
from tela import Tela
import PySimpleGUI as sg

class Main(IBackRegister):
    
    def __init__(self) -> None:
        self.window = Tela()._front_end()
    
    def _main(self):
        
        while True:
            event, values = self.window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break

            if event == "btn_back":
                print("voltar")
            if event == "btn_help":
                print("Ajudar")
                
                
    
if __name__ == "__main__":
    Main()._main()