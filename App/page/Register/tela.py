from ifront import IFrontRegister
import PySimpleGUI as sg


class Tela(IFrontRegister):
    __slots__ = ["__color"]

    def __init__(self) -> None:
        self.__color = "white"
        sg.theme_background_color(self.__color)

    def _front_end(self):
        bar_notification = [
            sg.Image(filename="App//img//barra de notificacao.png", pad=(0, (0, 50)))
        ]

        back_and_help = [
            sg.Image(filename="", pad=(0,(0,0)), background_color=self.__color),
            sg.Image(filename="", pad=(0,(0,0)), background_color=self.__color)
        ]

        create_account = []

        name = []
        email = []
        phone = []
        password = []
        confirm_password = []
        btn_create_account = []
        already_have_a_account_login = []
        layout = [
            bar_notification,
            back_and_help,
            create_account,
            name,
            email,
            phone,
            password,
            confirm_password,
            btn_create_account,
            already_have_a_account_login,
        ]
        window = sg.Window(
            "Solmed",
            layout=layout,
            size=(390, 844),
            element_justification="c",
            icon="App//img//sol.ico",
        )
        
        while True:
            event, values = window.read(timeout=1)
            
            if event == sg.WIN_CLOSED:
                break
            
if __name__ == "__main__":
    Tela()._front_end()