import flet as ft
def image_idioma(png):
    return ft.Image(
        src = f'image/{png}.svg',
        fit = ft.BoxFit.CONTAIN
    )