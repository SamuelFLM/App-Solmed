from .iback import IBackLogin
import PySimpleGUI as sg
from .tela import Tela

class MainLogin(IBackLogin):
    
    def __init__(self, conexao) -> None:
        self.window = Tela()._front_end()
        self.conexao = conexao
        
    def _main(self, tela_register):
        
        while True:
            event, values = self.window.read(timeout=1)
              

            if event == sg.WIN_CLOSED:
                break
            
            # check box remember email
            if values['chk-remember-me'] and event == 'btn-login':
                with open('App\data\dt-temp.txt', 'w') as arquivo:
                    arquivo.write(f"{values['email']}\n")          
                              
            # validação login

            # validação esqueceu senha
            if event == "forget-password":
                print('esqueci senha')

            # validação cadastro
            if event == "sign-up":
                self.window.close()
                tela_register._main()
                break

            # validação open/closed senha
            if event == "btn-password-closed":
                self.window["btn-password-closed"].update(visible=False)
                self.window["btn-password-open"].update(visible=True)
                self.window["password"].update(password_char="")

            if event == "btn-password-open":
                self.window["btn-password-open"].update(visible=False)
                self.window["btn-password-closed"].update(visible=True)
                self.window["password"].update(password_char="*")

if __name__ == "__main__":
    MainLogin()._main()
    
    