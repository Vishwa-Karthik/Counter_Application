import flet
from flet import icons,Page,TextField,IconButton,Row

def main(page: Page):
    page.title = "Counter App"
    page.vertical_alignment = 'center'

    txt_field = TextField(value='0',width=100,text_align='right')

    def minus(e):
        txt_field.value = int(txt_field.value) - 1
        page.update()

    def plus(e):
        txt_field.value = int(txt_field.value) + 1
        page.update()

    page.add(
        Row(
        [
            IconButton(icons.REMOVE, on_click=minus),
            txt_field,
            IconButton(icons.ADD,on_click=plus)
        ],alignment='center'
    ))

flet.app(target=main)