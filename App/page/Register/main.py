
from .iback import IBackRegister
from .tela import Tela
import PySimpleGUI as sg

class MainRegister(IBackRegister):
    
    def __init__(self, conexao) -> None:
        self.window = Tela()._front_end()
        self.conexao = conexao
    
    def _main(self, tela_login):
        
        while True:
            event, values = self.window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break
            
            name = values["input_name"]
            email = values["input_email"]
            phone = values["input_phone"]
            password = values["password"]
            password_confirm = values["password-confirm"]
            
            if event == "btn-create-account":
                validacao = ""
                if bool(name):
                    if bool(email):
                        if bool(phone):
                            if bool(password):
                                if bool(password_confirm):
                                    validacao = "V"
                else: return False
                
                if validacao == "V":
                    self.conexao.registro(name, email, phone, password)
            
            if event == "btn_back":
                print("voltar")
            if event == "btn_help":
                print("Ajudar")
                
                
    
if __name__ == "__main__":
    MainRegister("")._main()