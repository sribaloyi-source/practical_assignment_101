import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    name_field = ft.TextField(
        label="Your name",
        hint_text="Enter your name",
        width=300,
    )

    greeting_text = ft.Text("", size=20)

    def greet_click(e):
        name = name_field.value.strip()

        if name:
            greeting_text.value = f"Hello, {name}!"
        else:
            greeting_text.value = "Please enter your name."

        page.update()

    greet_button = ft.ElevatedButton(
        text="Greet Me",
        on_click=greet_click,
    )

    page.add(
        ft.Column(
            controls=[
                name_field,
                greet_button,
                greeting_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )


if __name__ == "__main__":
    ft.run(main)
