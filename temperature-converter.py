from nicegui import ui

ui.colors(
      primary='#ff6e6e',
      secondary='#691818',
      accent='#481f66',
      positive='#481f66',
      negative='#a81c00',
      info='#701f6b',
      warning='#f2c037',
      background= '#facdcd',
      sliderbackground='#edd4ff'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: changes the color of the text to the hex code defined as "positive"
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: changes the color of the text ot the hex code definied as "negative"
def convertslider():
    try: 
        temp = float(slider_field.value)
        if sliderconversion_type.value == "Celsius to Fahrenheit":
            sliderresult_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            sliderresult_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        sliderresult_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: changes the color of the text to the hex code defined as "positive"
    except ValueError:
        sliderresult_label.set_text("Please enter a valid number.")
        sliderresult_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: changes the color of the text ot the hex code definied as "negative"
with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-sliderbackground border-4 border-black"):
        ui.label("Sliding Temperature Converter").classes("text-2xl font-mono uppercase font-bold text-accent mb-4 pb-6")
        slider_field = ui.slider(min=0, max=100, value=50).props('label-always').classes("pb-8")
        #ui.label().bond_text_from(slider,'value')
        sliderconversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convertslider).classes("text-white font-bold py-2 px-4 rounded ")
        sliderresult_label = ui.label("").classes("text-lg mt-4 py-1 ")
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-background border-4 border-black"):
        # w-100: Set element width to be fixed at 100
        # p-6: Set element to have padding width of 6 
        # shadow-xl: set element to have a shadow size of xl (extra large)
        # mx-auto: sets the element to automatically have an equal margin on either side, and between elements
        # mt-10: sets the element to have a margin of 10 on top
        # rounded-xl: sets the elements corners to have a xl (extra large) rounded border size (more rounded)
        ui.label("Temperature Converter").classes("font-mono uppercase text-2xl font-bold text-accent mb-4")
        # text-2xl: Sets the font size to be 20 px and and the line height to be 1.75/1.25
        # font-bold: Sets the font weight to bold
        # text-accent: Setes the text color to be the color defined by accent
        # mb-4: Sets the bottom margin of the text to be 4
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg text-negative text-bold border rounded")
        # w-full: Sets element width to be the full width of the screen
        # border: Sets border width of element to be 1 px
        # rounded: Sets element corners to be rounded to default rounded border size
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded ")
        # text-white: Sets text color to be white
        # py-2: Sets element to have vertical padding of 2 px
        # px-4: Sets element to have horizontal padding of 4 px
        result_label = ui.label("").classes("text-lg mt-4")

ui.run(port=8082)