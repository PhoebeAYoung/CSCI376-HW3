from nicegui import ui

with ui.row():
    with ui.card():
        input_field = ui.input(
            on_change = lambda e: result.set_text(e.value.lower())
        )
        result = ui.label()
ui.run(port=8081)