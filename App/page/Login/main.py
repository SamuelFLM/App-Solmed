from .iback import IBackLogin
import PySimpleGUI as sg
from .tela import Tela
import re
import pyautogui as bot


class MainLogin(IBackLogin):
    def __init__(self, conexao, tela_register) -> None:
        self.window = Tela()._front_end()
        self.tela_register = tela_register
        self.conexao = conexao

    def _main(self):
        while True:
            event, values = self.window.read(timeout=1)

            if event == sg.WIN_CLOSED:
                break

            email = str(values["email"]).strip()
            password = str(values["password"]).strip()

            # check box remember email
            if values["chk-remember-me"] and event == "btn-login":
                with open("App\data\dt-temp.txt", "w") as arquivo:
                    arquivo.write(f"{values['email']}\n")

            # validação login
            if bool(email) and bool(password):
                padrao = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$"
                resultado = re.match(padrao, email)
                if bool(resultado):
                    dados = self.conexao.login_sistema(email)
                    if bool(dados) and event == "btn-login":
                        if (email == str(dados[0][0]).strip()) and (password == str(dados[0][1].strip())):
                            bot.confirm(
                                title="SUCESS",
                                text=f"BEM VINDO AO SISTEMA {str(dados[0][2]).title()}",
                                buttons=["OK"],
                            )
                        else:bot.confirm(
                                title="ERRO",
                                text="EMAIL OU SENHA INCORRETOS",
                                buttons=["OK"],
                            )
               
            # validação esqueceu senha
            if event == "forget-password":
                print("esqueci senha")

            # validação cadastro
            if event == "sign-up":
                self.window.close()
                self.tela_register._main(MainLogin(self.conexao, self.tela_register))
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
