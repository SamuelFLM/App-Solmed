
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
            
            if event == "btn-password-closed":
                self.window["btn-password-closed"].update(visible=False)
                self.window["btn-password-open"].update(visible=True)
                self.window["password"].update(password_char="")

            if event == "btn-password-open":
                self.window["btn-password-open"].update(visible=False)
                self.window["btn-password-closed"].update(visible=True)
                self.window["password"].update(password_char="*")
                
            if event == "btn-password-closed-confirm":
                self.window["btn-password-closed-confirm"].update(visible=False)
                self.window["btn-password-open-confirm"].update(visible=True)
                self.window["password-confirm"].update(password_char="")

            if event == "btn-password-open-confirm":
                self.window["btn-password-open-confirm"].update(visible=False)
                self.window["btn-password-closed-confirm"].update(visible=True)
                self.window["password-confirm"].update(password_char="*")
            
            if event == "btn_back":
                print("voltar")
            if event == "btn_help":
                print("Ajudar")
                
                
    
if __name__ == "__main__":
    MainRegister("")._main()