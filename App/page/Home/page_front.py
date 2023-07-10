from interface_front import InterfaceHomeFront
import PySimpleGUI as sg


class PageFront(InterfaceHomeFront):
    __slots__ = ["__color"]

    def __init__(self) -> None:
        self.__color = "white"
        sg.theme_background_color(self.__color)

    def _front_end(self):
        barra_notificacao = [sg.Image(filename="App//img//barra de notificacao.png")]

        logo = [
            sg.Image(
                filename="App//img//logo.png",
                background_color=self.__color,
                pad=(70, (0, 0)),
            )
        ]

        welcome_back = [
            sg.Text(
                "Welcome back",
                font="Jaldi 20 bold",
                background_color=self.__color,
                text_color="#FFA620",
                pad=(20, (0, 20)),
            )
        ]

        email = [
            [
                sg.Image(
                    filename="App//img//email.png",
                    background_color=self.__color,
                    pad=(20, (0, 5)),
                ),
                sg.Input(
                    "E-mail/Phone Number",
                    size=(31, 10),
                    background_color=self.__color,
                    font="Jaldi 13",
                    pad=(0, (0, 5)),
                    border_width=0,
                    text_color="#535353",
                ),
            ],
            [sg.HSep(pad=(20, (0, 0)))],
        ]
        password = [
            [
                sg.Image(
                    filename="App//img//password.png",
                    background_color=self.__color,
                    pad=(20, (0, 5)),
                ),
                sg.Input(
                    "",
                    size=(25, 10),
                    password_char="*",
                    background_color=self.__color,
                    font="Jaldi 13",
                    pad=(0, (0, 5)),
                    border_width=0,
                    text_color="#535353",
                ),
                sg.Image(
                    filename="App//img//password-closed.png",
                    background_color=self.__color,
                    pad=(30, (0, 5)),
                ),
            ],
            [sg.HSep(pad=(20, (0, 0)))],
        ]
        remember_me_and_forget_password = []
        login = []
        social_media = [
            [],
            [
                sg.Image(
                    filename="App//img//facebook 1.png",
                    background_color=self.__color,
                    pad=(0, (0, 0)),
                ),
                sg.Image(
                    filename="App//img//instagram 1.png",
                    background_color=self.__color,
                    pad=(0, (0, 0)),
                ),
                sg.Image(
                    filename="App//img//linkedin.png",
                    background_color=self.__color,
                    pad=(0, (0, 0)),
                ),
            ],
        ]
        rodape_sign_up = []

        layout = [
            barra_notificacao,
            logo,
            welcome_back,
            email,
            password,
            remember_me_and_forget_password,
            login,
            social_media,
            rodape_sign_up,
        ]

        window = sg.Window("Solmed", layout=layout, size=(390, 844))

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break


if __name__ == "__main__":
    PageFront()._front_end()
