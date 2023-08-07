from ifront import IFrontRegister
import PySimpleGUI as sg


class Tela(IFrontRegister):
    __slots__ = ["__color"]

    def __init__(self) -> None:
        self.__color = "white"
        sg.theme_background_color(self.__color)

    def _front_end(self):
        barra_notificacao = [
            sg.Image(filename="App//img//barra de notificacao.png", pad=(0, (0, 50)))
        ]